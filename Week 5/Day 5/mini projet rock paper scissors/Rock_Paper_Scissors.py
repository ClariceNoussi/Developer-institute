class RockPaperScissors():
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.play_game() 
    def get_moves_from_players(self):
        player1_move = input("player1_move: What move do you want to do? (R P S): ")
        player2_move = input("player2_move: What move do you want to do? (R P S): ")
        return player1_move,player2_move 
    def evaluate_play(self,player_1_move, player_2_move):
        if player_1_move == player_2_move:
            return "Draw"
            if player_1_move == "R":
                if player_2_move =="P":
                    return f"player2_move"#rock wins to scissors #rock looses to paper
        if player_2_move == "S":
                return f"player1_move" #rock wins to scissors
        if player_1_move == "P":
            if player_2_move =="R":
                return f"player1_move"#paper wins to rock
            if player_2_move == "S":
                return f"player2_move"#paper looses to scissors
            if player_1_move == "S":
                if player_2_move =="P":
                    return f"player1_move"#scissors wins to paper
            if player_2_move == "R":
                return f"player2_move"#scissors looses to rock
    def keep_score(self,winner):
        if winner == "player1_move":
            self.score1 += 1
        if winner == "player2_move":
            self.score2 += 1
    def game_running(self):
        if self.score1 == 3 or self.score2 == 3:
            return False
        return True
    def play_game(self):
        while self.game_running():
            player_1_move, player_2_move = self.get_moves_from_players() #taking the return from the fuction and storing it in a variable so I can use the information outisde of the function
            winner = self.evaluate_play(player_1_move, player_2_move) 
            self.keep_score(winner)
            print(f"Score: Player 1: {self.score1} - {self.score2} Player 2") 
        else:
            if self.score1 == 3:
                print(f"Player 1 wins!")
            else:
                print(f"Player 2 wins!")
                
RockPaperScissors()