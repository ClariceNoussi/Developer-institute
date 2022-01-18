import random
class Game():
	possible_choices = ['r','p','s']
	def get_user_item(self):
		while True:
			user_choice = input("Select (r)ock, (p)aper, or (s)cissors: ").strip().lower()
			if user_choice not in self.possible_choices:
				print("Invalid input, try again")
			else:
				return user_choice
def get_computer_item(self):
        randint = random.randint(0,2)
		# computer_item = random.choice(self.possible_choices)
        return self.possible_choices[randint]
def get_game_result(self, user_item, computer_item):
		if user_item == computer_item:
			return 'draw'
		elif (user_item == 'r' and computer_item == 's') or (user_item == 'p' and computer_item == 'r') or (user_item == 's' and computer_item == 'p'):
			return 'win'
		else: 
			return 'loss'
def play(self):
		user_item = self.get_user_item()
		computer_item = self.get_computer_item()
		result = self.get_game_result(user_item, computer_item)
		print(f"You chose {user_item}, the computer chose {computer_item}, the result is : '{result}'")
		return result