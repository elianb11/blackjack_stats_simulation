from Card import Card
import random

class CardStack:

    def new_stack(self):
        cards = []
        for _ in range(8):
            for i in range(1,14):
                for j in range(1,5):
                    card = Card(i,j)
                    cards.append(card)
        random.shuffle(cards)
        return cards

    def __init__(self):
        self.cards = self.new_stack()
        self.used_cards = []
        self.red_card = random.randint(150,300)

    def draw(self):
        card = self.cards.pop(0)
        self.used_cards.append(card)
        return card

    def shuffle(self):
        if len(self.cards) < self.red_card:
            self.cards.extend(self.used_cards)
            random.shuffle(self.cards)
            self.used_cards = []
