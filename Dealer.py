from CardStack import CardStack

class Dealer:

    def __init__(self, deck):

        self.stop_play = False
        self.cards = []
        self.hand_value_1 = 0
        self.hand_value_2 = 0
        self.best_value = 0

        self.bust_number = 0
        self.bj_number = 0
        self.more_than_nineteen_streak = 0


    def update_values(self):

        self.hand_value_1 = 0
        self.hand_value_2 = 0
        
        for card in self.cards:
            value = card.value
            self.hand_value_1 += value
            if card.number == 1:
                self.hand_value_2 += 11
            else:
                self.hand_value_2 += value

        if self.hand_value_2 > 16 and self.hand_value_2 < 22:
            self.best_value = self.hand_value_2
            self.stop_play = True
        elif self.hand_value_1 > 16 and self.hand_value_1 < 22:
            self.stop_play = True
            self.best_value = self.hand_value_1
        elif self.hand_value_1 > 21 and self.hand_value_2 > 21:
            self.best_value = 0
            self.stop_play = True


    def isBJ(self):

        if len(self.cards) == 2 and self.best_value == 21:
            return True
        else:
            return False

    def reset_hand(self):
        if self.best_value > 18 and self.best_value < 22:
            self.more_than_nineteen_streak += 1
        else:
            self.more_than_nineteen_streak = 0
        self.stop_play = False
        self.cards = []
        self.hand_value_1 = 0
        self.hand_value_2 = 0
        self.best_value = 0