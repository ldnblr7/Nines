# Nines
Ever since I was little my mom would gather us kids around the kitchen table to play this game. As we've aged, we play less and less as siblings move out for college and careers. Now that the distances between us span over 1,242 miles, this lifelong tradition is falling to the wayside. In honor of my mother and the hours of bonding over the kitchen table, I'm building this game to span the gap and unite the family once again.

Overview: A card game coded using python and object-oriented programming.

nines.py: The control center, houses the functions detailing the win condition, each user's turn, and dividing the deck amongst the players.

the_deck.py: A class representing a deck of cards. Creates a deck of 'card' objects, custom shuffles the cards, and defines methods to interact with the deck.

card.py: A class representing a card with a front, back and flip method.

player.py: A class representing a player object, with their card objects in a layout from the grid class.

grid.py: A 3x3 grid class, represents the cards laid out in front of the player.
