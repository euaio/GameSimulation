import random

class RouletteGame:
    def __init__(self):
        # Simplified Roulette: 0-12
        self.numbers = list(range(13))
        # Colors distributed independently from parity
        self.red_numbers = {1, 2, 5, 6, 9, 10}
        self.black_numbers = {3, 4, 7, 8, 11, 12}
        
        # Default weights (Fair-ish, equal probability for all numbers)
        self.fair_weights = [1] * 13
        
        # Tweaked weights (Admin can adjust this)
        # Example: Double the chance of 0 (Green)
        self.tweaked_weights = [1] * 13
        self.tweaked_weights[0] = 3 # Make 0 three times as likely

    def get_color(self, number):
        if number == 0:
            return 'green'
        elif number in self.red_numbers:
            return 'red'
        else:
            return 'black'

    def get_parity(self, number):
        if number == 0:
            return 'none'
        return 'odd' if number % 2 != 0 else 'even'

    def spin(self, is_tweaked=False, custom_weights=None):
        weights = self.fair_weights
        if is_tweaked:
            weights = custom_weights if custom_weights else self.tweaked_weights
        
        # random.choices returns a list, we take the first element
        outcome = random.choices(self.numbers, weights=weights, k=1)[0]
        return outcome

    def calculate_payout(self, bet_type, bet_value, bet_amount, outcome):
        outcome_color = self.get_color(outcome)
        outcome_parity = self.get_parity(outcome)
        
        win = False
        payout_multiplier = 0

        if bet_type == 'number':
            if int(bet_value) == outcome:
                win = True
                payout_multiplier = 12 # 12:1 payout (plus original bet back usually? No, 12:1 means profit 12. Total 13.)
                # Let's use standard casino terminology: "Pays 12 to 1". 
                # If I bet 10, I get 120 profit + 10 back = 130.
                # So multiplier for total return is 13.
                payout_multiplier = 13 
        
        elif bet_type == 'color':
            if bet_value == outcome_color:
                win = True
                payout_multiplier = 2 # 1:1 payout (Profit 1, Total 2)
        
        elif bet_type == 'parity':
            if bet_value == outcome_parity:
                win = True
                payout_multiplier = 2 # 1:1 payout

        if win:
            return bet_amount * payout_multiplier
        else:
            return 0

    def simulate_runs(self, n_runs, bet_type='color', bet_value='red', bet_amount=10, 
                     is_tweaked=False, custom_weights=None, seed=None):
        """
        Enhanced simulation with detailed statistics and tracking.
        
        Args:
            n_runs: Number of simulations to run
            bet_type: 'number', 'color', or 'parity'
            bet_value: Specific value for the bet type
            bet_amount: Amount to bet per simulation
            is_tweaked: Whether to use tweaked weights
            custom_weights: Optional custom weight distribution
            seed: Optional random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)
        
        total_bet = 0
        total_payout = 0
        wins = 0
        cumulative_profits = []
        outcome_distribution = {str(i): 0 for i in range(13)}
        running_profit = 0
        
        for _ in range(n_runs):
            outcome = self.spin(is_tweaked, custom_weights)
            payout = self.calculate_payout(bet_type, bet_value, bet_amount, outcome)
            
            total_bet += bet_amount
            total_payout += payout
            
            # Track profit/loss
            profit_this_round = payout - bet_amount
            running_profit += profit_this_round
            cumulative_profits.append(running_profit)
            
            # Track outcome distribution
            outcome_distribution[str(outcome)] += 1
            
            if payout > 0:
                wins += 1
        
        losses = n_runs - wins
        house_profit = total_bet - total_payout
        house_edge_percent = (house_profit / total_bet) * 100 if total_bet > 0 else 0
        win_rate = (wins / n_runs) * 100 if n_runs > 0 else 0
        loss_rate = (losses / n_runs) * 100 if n_runs > 0 else 0
        net_profit = total_payout - total_bet
        roi = (net_profit / total_bet) * 100 if total_bet > 0 else 0
        profit_per_bet = net_profit / n_runs if n_runs > 0 else 0
        expected_value_per_bet = net_profit / n_runs if n_runs > 0 else 0
        
        return {
            'runs': n_runs,
            'bet_type': bet_type,
            'bet_value': str(bet_value),
            'bet_amount': bet_amount,
            'total_bet': total_bet,
            'total_payout': total_payout,
            'house_profit': house_profit,
            'house_edge_percent': house_edge_percent,
            'wins': wins,
            'losses': losses,
            'win_rate': win_rate,
            'loss_rate': loss_rate,
            'net_profit': net_profit,
            'roi': roi,
            'profit_per_bet': profit_per_bet,
            'expected_value_per_bet': expected_value_per_bet,
            'cumulative_profits': cumulative_profits,
            'outcome_distribution': outcome_distribution
        }
