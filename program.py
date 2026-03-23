import json
from player import Player

board_size = 9
starting_balance = 16
starting_position = 0

with open('board.json', 'r') as file:
    board = json.load(file)

with open('rolls_1.json', 'r') as file:
    rolls_1 = json.load(file)


Player1 = Player("Peter", starting_balance, starting_position)
Player2 = Player("Billy", starting_balance, starting_position)
Player3 = Player("Charlotte", starting_balance, starting_position)
Player4 = Player("Sweedal", starting_balance, starting_position)

curr_player = Player1

for roll in rolls_1:
    space = curr_player.move(roll, board_size)
    print(f"{curr_player.name} landed on {board[space]['name']}")

    if curr_player == Player1:
        curr_player = Player2
    elif curr_player == Player2:
        curr_player = Player3
    elif curr_player == Player3:
        curr_player = Player4
    elif curr_player == Player4:
        curr_player = Player1

# space = Player1.move(rolls_1[0], 9)
# print(board[space]['name'])

# space = Player1.move(rolls_1[1], 9)
# print(board[space]['name'])


# print(json.dumps(board, indent=4))