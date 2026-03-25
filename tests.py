from player import Player
from space import Space
from program import handle_land_on_property, board, colour_groups, players

def test_pass_go():
    print("Testing passing GO...")
    p = Player("Test1", 10, 7)
    p.move(3, 9)
    assert p.balance == 11
    assert p.curr_space == 1

def test_no_pass_go():
    print("Testing not passing GO...")
    p = Player("Test2", 10, 5)
    p.move(2, 9)
    assert p.balance == 10
    assert p.curr_space == 7

def test_buy_property():
    print("Testing buying property...")
    p = Player("Test", 10, 0)
    space = Space("TestSpace", 3, "Red", "property")
    board = [space]
    colour_groups = {"Red": [space]}

    handle_land_on_property(p, 0, board, colour_groups)

    assert p.balance == 7
    assert board[0].owner == p

def test_pay_rent():
    print("Testing paying rent...")
    owner = Player("Test", 10, 0)
    tenant = Player("Test", 10, 0)
    
    space1 = Space("TestSpace1", 3, "Red", "property")
    space2 = Space("TestSpace2", 3, "Red", "property")
    space1.owner = owner

    board = [space1, space2]
    colour_groups = {"Red": [space1, space2]}

    handle_land_on_property(tenant, 0, board, colour_groups)

    assert tenant.balance == 7
    assert owner.balance == 13
    assert board[0].owner == owner

def test_pay_double_rent():
    print("Testing paying double rent...")
    owner = Player("Owner", 10, 0)
    tenant = Player("Tenant", 10, 0)

    space1 = Space("TestSpace1", 3, "Red", "property")
    space2 = Space("TestSpace2", 3, "Red", "property")

    space1.owner = owner
    space2.owner = owner

    board = [space1, space2]
    colour_groups = {"Red": [space1, space2]}

    handle_land_on_property(tenant, 0, board, colour_groups)

    assert tenant.balance == 4
    assert owner.balance == 16




test_pass_go()
test_no_pass_go()
test_buy_property()
test_pay_rent()
test_pay_double_rent()