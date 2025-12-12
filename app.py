from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, GameResult, MoneyRequest
from game_logic import RouletteGame
import os

app = Flask(__name__)
# Use environment variable for secret key, fallback to default for development
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'index'
login_manager.init_app(app)

# Initialize Game Logic
game = RouletteGame()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin'))
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        action = request.form.get('action')

        if action == 'register':
            user = User.query.filter_by(username=username).first()
            if user:
                flash('Username already exists.', 'error')
            else:
                new_user = User(username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash('Registration successful! Please login.', 'success')
                return redirect(url_for('index'))
        
        elif action == 'login':
            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash('Invalid username or password.', 'error')
        
        elif action == 'admin_login':
            user = User.query.filter_by(username=username).first()
            if user and user.is_admin and check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('admin'))
            else:
                flash('Invalid admin credentials.', 'error')

    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/home')
@login_required
def home():
    if current_user.is_admin:
        return redirect(url_for('admin'))
    return render_template('home.html', user=current_user)

@app.route('/game')
@login_required
def game_view():
    return render_template('game.html', user=current_user, is_admin=current_user.is_admin)

@app.route('/spin', methods=['POST'])
@login_required
def spin():
    data = request.json
    bet_type = data.get('bet_type')
    bet_value = data.get('bet_value')
    bet_amount = float(data.get('bet_amount'))

    if bet_amount > current_user.balance:
        return jsonify({'error': 'Insufficient balance'}), 400

    # Determine if we are in tweaked mode (could be global or per user/session)
    # For this project, let's say the game is always "Tweaked" if the admin set it so.
    # Or we can just use the current state of the game object.
    # Let's assume the game runs in "Tweaked" mode if weights are not default.
    is_tweaked = game.tweaked_weights != game.fair_weights

    outcome = game.spin(is_tweaked=True) # Always use the current configuration (which might be fair or tweaked)
    
    # Wait, spin(is_tweaked=True) uses tweaked_weights. 
    # If we want to switch between Fair and Tweaked, we need a flag.
    # Let's assume the Admin sets the "Active Mode".
    # For now, let's pass a flag from the game instance if we had one.
    # I'll add a property to the game instance in a bit, or just use a global variable.
    # Let's use a simple global for now.
    use_tweaked = app.config.get('USE_TWEAKED', False)
    
    outcome = game.spin(is_tweaked=use_tweaked)
    payout = game.calculate_payout(bet_type, bet_value, bet_amount, outcome)
    
    # Update User Balance
    current_user.balance += (payout - bet_amount) # Payout includes the original bet if win? 
    # My logic in game_logic: 
    # Number: 13x (Profit 12). So if I bet 10, payout is 130. Balance change: +130 - 10 = +120. Correct.
    # Loss: Payout 0. Balance change: 0 - 10 = -10. Correct.
    
    db.session.commit()

    # Log Result
    result = GameResult(
        user_id=current_user.id,
        bet_type=bet_type,
        bet_value=str(bet_value),
        bet_amount=bet_amount,
        outcome_number=outcome,
        outcome_color=game.get_color(outcome),
        payout=payout,
        is_tweaked=use_tweaked
    )
    db.session.add(result)
    db.session.commit()

    return jsonify({
        'outcome_number': outcome,
        'outcome_color': game.get_color(outcome),
        'payout': payout,
        'new_balance': current_user.balance
    })

@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        return redirect(url_for('home'))
    
    users = User.query.filter_by(is_admin=False).all()
    pending_requests = MoneyRequest.query.filter_by(status='pending').all()
    
    return render_template('admin.html', 
                         weights=game.tweaked_weights, 
                         use_tweaked=app.config.get('USE_TWEAKED', False),
                         users=users,
                         pending_requests=pending_requests)

@app.route('/admin/update_settings', methods=['POST'])
@login_required
def update_settings():
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.json
    weights = data.get('weights') # List of 13 integers
    use_tweaked = data.get('use_tweaked')
    
    if weights and len(weights) == 13:
        game.tweaked_weights = [int(w) for w in weights]
    
    app.config['USE_TWEAKED'] = use_tweaked
    
    return jsonify({'status': 'success'})

@app.route('/admin/reset_game', methods=['POST'])
@login_required
def reset_game():
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized'}), 403
    
    game.tweaked_weights = [1] * 13
    app.config['USE_TWEAKED'] = False
    
    return jsonify({'status': 'success'})

@app.route('/admin/simulate', methods=['POST'])
@login_required
def simulate():
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized'}), 403
    
    n_runs = int(request.json.get('n_runs', 1000))
    
    # Run Fair Simulation
    fair_results = game.simulate_runs(n_runs, is_tweaked=False)
    
    # Run Tweaked Simulation
    tweaked_results = game.simulate_runs(n_runs, is_tweaked=True)
    
    return jsonify({
        'fair': fair_results,
        'tweaked': tweaked_results
    })

@app.route('/request_money', methods=['POST'])
@login_required
def request_money():
    data = request.json
    amount = float(data.get('amount', 0))
    
    if amount <= 0:
        return jsonify({'error': 'Invalid amount'}), 400
    
    new_request = MoneyRequest(user_id=current_user.id, amount=amount)
    db.session.add(new_request)
    db.session.commit()
    
    return jsonify({'status': 'success', 'message': 'Request sent to admin'})

@app.route('/admin/handle_request/<int:request_id>/<action>', methods=['POST'])
@login_required
def handle_request(request_id, action):
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized'}), 403
    
    money_request = MoneyRequest.query.get(request_id)
    if not money_request:
        return jsonify({'error': 'Request not found'}), 404
    
    if action == 'approve':
        money_request.status = 'approved'
        user = User.query.get(money_request.user_id)
        user.balance += money_request.amount
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Request approved'})
    
    elif action == 'reject':
        money_request.status = 'rejected'
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Request rejected'})
    
    return jsonify({'error': 'Invalid action'}), 400

@app.route('/admin/update_balance', methods=['POST'])
@login_required
def update_balance():
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.json
    user_id = int(data.get('user_id'))
    new_balance = float(data.get('balance'))
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    user.balance = new_balance
    db.session.commit()
    
    return jsonify({'status': 'success'})

@app.route('/admin/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized'}), 403
    
    user = User.query.get(user_id)
    if not user or user.is_admin:
        return jsonify({'error': 'Cannot delete this user'}), 400
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'status': 'success'})

def create_admin():
    user = User.query.filter_by(username='admin').first()
    if not user:
        hashed_pw = generate_password_hash('administration', method='pbkdf2:sha256')
        admin_user = User(username='admin', password=hashed_pw, is_admin=True)
        db.session.add(admin_user)
        db.session.commit()
        print("Default admin created.")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_admin()
    app.run(debug=True)
