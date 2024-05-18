#Attaullah Abbasi

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

import random

class RockPaperScissors:
    choices = ['rock', 'paper', 'scissors']
    
    def __init__(self, human_players=1):
        self.human_players = human_players
        self.results = {'wins': 0, 'losses': 0, 'ties': 0}
        
    def get_choice(self, player, simulated_choice=None):
        if self.human_players >= player:
            if simulated_choice:
                return simulated_choice
            else:
                return random.choice(self.choices)  # Simulating input for testing
        else:
            return random.choice(self.choices)
        
    def determine_winner(self, p1, p2):
        if p1 == p2:
            return 'tie'
        elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
            return 'win'
        else:
            return 'loss'
        
    def play_once(self, p1_simulated_choice=None):
        p1_choice = self.get_choice(1, p1_simulated_choice)
        p2_choice = self.get_choice(2)
        print(f'Player 1 chose {p1_choice}, Player 2 chose {p2_choice}')
        
        result = self.determine_winner(p1_choice, p2_choice)
        if result == 'win':
            self.results['wins'] += 1
            print('Player 1 wins!')
        elif result == 'loss':
            self.results['losses'] += 1
            print('Player 2 wins!')
        else:
            self.results['ties'] += 1
            print('It\'s a tie!')
        
    def play_loop(self, rounds, simulated_choices=None):
        for i in range(rounds):
            p1_simulated_choice = simulated_choices[i] if simulated_choices else None
            self.play_once(p1_simulated_choice)
            
    def get_results(self):
        return self.results

# Test the code
game = RockPaperScissors(human_players=1)
game.play_once('rock')  # Simulating Player 1 choosing 'rock'
print(game.get_results())

game.play_loop(5, ['rock', 'paper', 'scissors', 'rock', 'paper'])  # Simulating multiple rounds
print(game.get_results())
