from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    balance = db.Column(db.Float, default=1000.0)
    is_admin = db.Column(db.Boolean, default=False)
    
    # Relationship to game results
    results = db.relationship('GameResult', backref='player', lazy=True)
    # Relationship to money requests
    money_requests = db.relationship('MoneyRequest', backref='user', lazy=True)

class GameResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bet_type = db.Column(db.String(50), nullable=False)  # 'number', 'color', 'parity'
    bet_value = db.Column(db.String(50), nullable=False) # '5', 'red', 'odd'
    bet_amount = db.Column(db.Float, nullable=False)
    outcome_number = db.Column(db.Integer, nullable=False)
    outcome_color = db.Column(db.String(20), nullable=False)
    payout = db.Column(db.Float, nullable=False) # Positive for win, 0 or negative for loss (usually 0 if we just deduct bet first)
    is_tweaked = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class MoneyRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'approved', 'rejected'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
