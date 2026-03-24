import json
from player import Player
from space import Space

board_size = 9
starting_balance = 16
starting_position = 0

with open('board.json', 'r') as file:
    board = [
        Space(
            space['name'],
            space.get('price'),
            space.get('rent'),
            space['type']
        )
        for space in json.load(file)
    ]

with open('rolls_1.json', 'r') as file:
    rolls_1 = json.load(file)


Player1 = Player("Peter", starting_balance, starting_position)
Player2 = Player("Billy", starting_balance, starting_position)
Player3 = Player("Charlotte", starting_balance, starting_position)
Player4 = Player("Sweedal", starting_balance, starting_position)

players = [Player1, Player2, Player3, Player4]


curr_index = 0

for roll in rolls_1:
    curr_player = players[curr_index]
    space = curr_player.move(roll, board_size)

    print(f"{curr_player.name} rolled {roll} and landed on {board[space].name} and has a balance of {curr_player.balance}")

    if board[space].name == "GO":
        curr_player.balance += 1

    if board[space].type == "property":
        if board[space].owner is None:
            # player lands on unowned property and must buy it
            curr_player.balance -= board[space].price
            board[space].owner = curr_player.name
            print(f"{curr_player.name} bought {board[space].name} for {board[space].price} and has a balance of {curr_player.balance}")
        else:
            # player lands on owned property and must pay rent to owner
            if board[space].owner != curr_player.name:
                curr_player.balance -= board[space].rent
                for player in players:
                    if player.name == board[space].owner:
                        player.balance += board[space].rent
                print(f"{curr_player.name} paid {board[space].rent} rent to {board[space].owner} and has a balance of {curr_player.balance}")
            # player lands on their own property and does nothing
            elif board[space].owner == curr_player.name:
                print(f"{curr_player.name} landed on their own property {board[space].name} and has a balance of {curr_player.balance}")
                

    curr_index = (curr_index + 1) % len(players)

# space = Player1.move(rolls_1[0], 9)
# print(board[space]['name'])

# space = Player1.move(rolls_1[1], 9)
# print(board[space]['name'])


# print(json.dumps(board, indent=4))