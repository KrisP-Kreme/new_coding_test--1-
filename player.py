class Player:
    def __init__(self, name, balance, curr_space):
        self.name = name
        self.balance = balance
        self.curr_space = 0

    def move(self, steps, board_size):
        old_position = self.curr_space
        self.curr_space = (self.curr_space + steps) % board_size

        return self.curr_space