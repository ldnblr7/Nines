import random
from card import Card
class The_Deck:
    def __init__(self):
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['Spade', 'Diamond', 'Heart', 'Club']
        cards_ordered = [Card(value + " " + suit) for suit in suits for value in values]
        cards_ordered.append(Card("Joker"))
        cards_ordered.append(Card("Joker"))
        card_dictionary = {}
        self.deck = []
        self.discard = ''
        for i in range(54):
            card = random.choice(cards_ordered)
            card_dictionary[i] = card
            cards_ordered.remove(card)
        for i in range(54):
            self.deck.append(card_dictionary[i])

    def draw(self):
        the_card = self.deck[-1]
        self.deck.remove(the_card)
        return the_card

    def double(self, other_deck):
        self.deck = self.deck + other_deck.deck
        self.shuffle()

    def shuffle(self):
        dictionary = {}
        num_cards = len(self.deck)
        for i in range(num_cards):
            card = random.choice(self.deck)
            dictionary[i] = card
            self.deck.remove(card)
        for j in range(num_cards):
            self.deck.append(dictionary[j])



