class Grid:
    def __init__(self):
        row1 = [None, None, None]
        row2 = [None, None, None]
        row3 = [None, None, None]
        self.cards = [row1, row2, row3]

    def swap(self, card, column, row):
        temp = self.cards[column][row]
        self.cards[column][row] = card
        return temp

    def set(self, card, column, row):
        self.cards[column][row] = card

    def print(self):
        print("Your cards:")
        try:
            for row in self.cards:
                print(f"{row[0].showing} {row[1].showing} {row[2].showing}")
        except:
            print("Your deck has exploded.")
            exit()