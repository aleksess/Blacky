import random
import Card


class Game:
    def __init__(self):
        self.cards = []

        colors = ['club', 'diamond', 'heart', 'spade']
        figures = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        i = 0
        j = 0

        while i < 4:
            while j < 13:
                x = Card(colors[i], figures[j], value[j])
                self.cards.append(x)
                j = j + 1
            i = i + 1
