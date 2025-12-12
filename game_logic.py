import random

class RouletteGame:
    def __init__(self):
        # Simplified Roulette: 0-12
        self.numbers = list(range(13))
        self.red_numbers = {1, 3, 5, 7, 9, 11}
        self.black_numbers = {2, 4, 6, 8, 10, 12}
        
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

    def simulate_runs(self, n_runs, is_tweaked=False, custom_weights=None):
        results = []
        # Simulation assumes a mix of bets or a specific strategy.
        # For simplicity, let's simulate a player betting 10 units on 'Red' every time.
        bet_type = 'color'
        bet_value = 'red'
        bet_amount = 10
        
        total_bet = 0
        total_payout = 0
        wins = 0
        
        for _ in range(n_runs):
            outcome = self.spin(is_tweaked, custom_weights)
            payout = self.calculate_payout(bet_type, bet_value, bet_amount, outcome)
            
            total_bet += bet_amount
            total_payout += payout
            if payout > 0:
                wins += 1
                
        house_profit = total_bet - total_payout
        house_edge_percent = (house_profit / total_bet) * 100 if total_bet > 0 else 0
        
        return {
            'runs': n_runs,
            'total_bet': total_bet,
            'total_payout': total_payout,
            'house_profit': house_profit,
            'house_edge_percent': house_edge_percent,
            'wins': wins,
            'losses': n_runs - wins
        }
