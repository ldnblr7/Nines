from the_deck import The_Deck
from player import Player

'''Make a Card class with two elements, front and back.
ex. Class Card:
        __init__(self, value)
        self.front = value
        self.back = "#"
        '''

def divide_deck(deck, num_players):
    '''
    :param deck: class The_Deck, containing all the cards.
    :param num_players: integer, number of players
    :return: list of the players, each of a Player class
    '''
    players = []
    for i in range(num_players):
        i = Player()
        players.append(i)
    for j in range(9):
        for player in players:
            player.temp_list.append(deck.draw())
    for player in players:
        player.initialize_grid(player.temp_list)
    return players


def user_turn(player, deck):
    """
    The player will grab a card from the deck or discard pile.
    :param player:
    :return: true if the player lays out all of their cards, false otherwise.
    """
    status = False
    card = deck.draw()
    print("Your hand:\n")
    player.print()
    a_card = deck.draw()
    a_card.flip()
    print(f"Top of deck: {a_card.showing}")
    print("Select an option [type number]")
    move = input("1. Swap into my cards\n2. Discard\n")
    if move == "1":
        coordinates = input("Which coordinates do you want to place it at?").split(',')
        card_in_hand = player.cards.swap(a_card, coordinates[0], coordinates[1])
        deck.discard = card_in_hand

    return status

def start_the_game(players, deck):
    """
    A while loop that only returns false
    :param players:
    :param deck:
    :return:
    """
    counter = 0
    ultimate_counter = 0
    # boolean = True
    while ultimate_counter < 30 * len(players):
        if user_turn(players[counter], deck):
            ultimate_counter = 29 * len(players)
        counter = (counter + 1) % 3
        ultimate_counter += 1

def main():
    deck = The_Deck()
    num_players = int(input("How many players? "))
    if num_players > 3:
        second_deck = The_Deck()
        deck.double(second_deck)
    players = divide_deck(deck, num_players)
    start_the_game(players, deck)


if __name__ == '__main__':
    main()