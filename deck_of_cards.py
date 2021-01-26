from random import shuffle


class Card:
    # Each instance is a card with a value and a suit.
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    # Calls on the Cards class to create a deck of 52 unique cards.
    def __init__(self):
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = ("A", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K")
        self.cards = [Card(value, suit) for value in values for suit in suits]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        # Returns number of remaining cards in deck.
        return len(self.cards)

    def _deal(self, num):
        # returns a number of cards based on the deal_card and
        # deal_hand methods and removes those cards from the deck.
        deck_count = self.count()
        draw = min([deck_count, num])
        if count == 0:
            raise ValueError("All cards have been dealt.")
        hand = self.cards[-draw:]
        self.cards = self.cards[:-draw]
        return hand

    def deal_card(self):
        # deals and returns 1 card.
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        # deals and returns a specified number of cards.
        return self._deal(hand_size)

    def shuffle(self):
        # shuffles a full deck of cards.
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled.")
        shuffle(self.cards)
        return self
