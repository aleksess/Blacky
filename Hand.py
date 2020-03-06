import Card


class Hand:
    def __init__(self):
        self.cards = []
        self.numberOfCards = 0

    def pushCard(self, Card):
        self.cards.append(Card)
        self.numberOfCards = self.numberOfCards + 1

    def SplitHand(self):
        if self.numberOfCards == 2 and self.cards[0] == self.cards[1]:
            return Hand().cards.append(self.cards.pop(1))
