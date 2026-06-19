class Player:
    def __init__(self, username):
        self.username = username
        self.games_played = 0
        self.games_won = 0

    def record_win(self):
        self.games_played += 1
        self.games_won += 1

    def record_loss(self):
        self.games_played += 1