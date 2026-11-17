from grid import Grid

class Player:
    def __init__(self):
        self.cards = Grid()
        self.temp_list = []

    def initialize_grid(self, deck):
        counter = 0
        for y in range(3):
            for x in range(3):
                self.cards.set(deck[counter], x, y)
                counter += 1

    def print(self):
        self.cards.print()

