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
            space.get('colour'),
            space['type']
        )
        for space in json.load(file)
    ]

with open('rolls_1.json', 'r') as file:
    rolls_1 = json.load(file)

with open('rolls_2.json', 'r') as file:
    rolls_2 = json.load(file)

# group spaces by colour in dictionary
colour_groups = {}
for space in board:
    if space.colour is not None:
        if space.colour not in colour_groups:
            colour_groups[space.colour] = []
        colour_groups[space.colour].append(space)


# initialize four players
Player1 = Player("Peter", starting_balance, starting_position)
Player2 = Player("Billy", starting_balance, starting_position)
Player3 = Player("Charlotte", starting_balance, starting_position)
Player4 = Player("Sweedal", starting_balance, starting_position)

players = [Player1, Player2, Player3, Player4]

# handle landing on property spaces
def handle_land_on_property(player, space):
    if board[space].owner is None:
        # player lands on unowned property and must buy it
        player.balance -= board[space].price
        board[space].owner = player
        print(f"{player.name} bought {board[space].name} for {board[space].price} and has a balance of {player.balance}")
    else:
        # player lands on owned property and must pay rent to owner
        if board[space].owner != player:
            # rent is doubled if all properties of the same colour are owned by the same player
            if all(s.owner == board[space].owner for s in colour_groups[board[space].colour]):
                rent = board[space].price * 2
            else:
                rent = board[space].price
            player.balance -= rent
            owner = board[space].owner
            owner.balance += rent
            print(f"{player.name} landed on {board[space].name}, paid {rent} rent to {board[space].owner.name} and has a balance of {player.balance}")
        # player lands on their own property and does nothing
        elif board[space].owner == player:
            print(f"{player.name} landed on their own property {board[space].name} and has a balance of {player.balance}")

# handle end game when a player goes bankrupt
def handle_end_game(bankrupt_player):
    max_balance = players[0].balance
    winner = players[0]
    for player in players:
        if player.balance > max_balance:
            max_balance = player.balance
            winner = player
    print("Final Outcome: ")
    print(f"{bankrupt_player.name} has gone bankrupt. {winner.name} wins.")
    for player in players: 
        if player.balance < 0:
            print(f"{player.name} is bankrupt and finished on {board[player.curr_space].name}.")           
        else:
            print(f"{player.name} has a balance of {player.balance} and finished on {board[player.curr_space].name}.")
    exit()


# loop for simulating game 
curr_index = 0
for roll in rolls_1:
    curr_player = players[curr_index]
    space = curr_player.move(roll, board_size)

    # check if a player has landed on a property space and handle accordingly
    if board[space].type == "property":
        handle_land_on_property(curr_player, space)

    # check if player has gone bankrupt and end game if so
    if curr_player.balance < 0:
        handle_end_game(curr_player)
    
    curr_index = (curr_index + 1) % len(players)
