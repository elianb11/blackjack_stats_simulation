
CARD_NAME = {
    1 : "ACE (A)",
    2 : "TWO (2)",
    3 : "THREE (3)",
    4 : "FOUR (4)",
    5 : "FIVE (5)",
    6 : "SIX (6)",
    7 : "SEVEN (7)",
    8 : "EIGHT (8)",
    9 : "NINE (9)",
    10 : "TEN (10)",
    11 : "JACK (J)",
    12 : "QUEEN (Q)",
    13 : "KING (K)"
}

CARD_COLOR = {
    1 : "CLUB",
    2 : "DIAMOND",
    3 : "HEART",
    4 : "SPADE"
}

CARD_VALUE = {
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 9,
    10 : 10,
    11 : 10,
    12 : 10,
    13 : 10
}

class Card:

    def __init__(self, number, color):
        self.number = number
        self.color_number = color
        self.value = CARD_VALUE[number]
        self.name = CARD_NAME[number]
        self.color = CARD_COLOR[color]

    def __str__(self):
        return "{}_{}".format(self.color, self.name)


