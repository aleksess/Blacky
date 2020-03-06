class Card:
    def __init__(self, Color, Figure, Value):
        self.color = Color
        self.figure = Figure
        self.value = Value

    def swapValue(self):
        if self.figure == 'ace':
            if self.value == 11:
                self.value = 1
            else:
                self.value = 11
