class Card:
    def __init__(self, value):
        self.face = value
        self.back = '#'
        self.showing = self.back

    def flip(self):
        if self.showing == self.face:
            self.showing = self.back
        else:
            self.showing = self.face
