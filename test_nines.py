from the_deck import The_Deck
from nines import *
from grid import Grid
from card import Card
def test_divide_deck():
    num_players = 4
    deck = The_Deck()
    divide_deck(deck, num_players)

def test_print():
    the_grid = Grid()
    the_grid.cards = [[Card(1), Card(2), Card(3)],[Card(4), Card(5), Card(6)],[Card(7), Card(8), Card(9)]]
    the_grid.print()


if __name__ == '__main__':
    test_print()
    # pass