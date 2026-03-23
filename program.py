import json
from player import Player

with open('board.json', 'r') as file:
    board = json.load(file)

with open('rolls_1.json', 'r') as file:
    rolls_1 = json.load(file)


Player1 = Player("Peter", 16, 0)
Player2 = Player("Billy", 16, 0)
Player3 = Player("Charlotte", 16, 0)
Player4 = Player("Sweedal", 16, 0)

space = Player1.move(rolls_1[0], 9)
print(board[space]['name'])

space = Player1.move(rolls_1[1], 9)
print(board[space]['name'])


# print(json.dumps(board, indent=4))