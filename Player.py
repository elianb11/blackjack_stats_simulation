from CardStack import CardStack
import sys

PLAYER_STATES = {
    1 : "STAY",
    2 : "HIT",
    3 : "DOUBLE",
    4 : "SPLIT"
}

class Player:

    def __init__(self,cash):

        self.init_balance = cash
        self.init_bet = 1
        self.last_bet = 0
        self.lose_streak = 0
        self.max_lose_streak = 0
        self.win_streak = 0
        self.max_win_streak = 0
        self.max_bet = 1
        self.cash = cash

        self.stop_play = False
        self.bet = 0
        self.cards = []
        self.hand_value_1 = 0
        self.hand_value_2 = 0
        self.best_value = 0

        self.stop_play_split = True
        self.split_bet = 0
        self.cards_split = []
        self.hand_split_value_1 = 0
        self.hand_split_value_2 = 0
        self.best_split_value = 0

        self.bj_number = 0
        self.win_number = 0
        self.lose_number = 0
        self.push_number = 0
        self.profit = 0

    
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
        
        if self.hand_value_2 > self.hand_value_1 and self.hand_value_2 < 22:
            self.best_value = self.hand_value_2
        elif self.hand_value_1 < 22:
            self.best_value = self.hand_value_1
        else:
            self.best_value = -1

        if self.hand_value_1 > 21:
            self.stop_play = True

        self.hand_split_value_1 = 0
        self.hand_split_value_2 = 0
        
        for card in self.cards_split:
            value = card.value
            self.hand_split_value_1 += value
            if card.number == 1:
                self.hand_split_value_2 += 11
            else:
                self.hand_split_value_2 += value

        if self.hand_split_value_2 > self.hand_split_value_1 and self.hand_split_value_2 < 22:
            self.best_split_value = self.hand_split_value_2
        elif self.hand_split_value_1 < 22:
            self.best_split_value = self.hand_split_value_1
        else:
            self.best_split_value = -1

        if self.hand_split_value_1 > 21:
            self.stop_play_split = True


    def select_bet(self, bet):
        if bet > self.cash:
            sys.exit("Not enough balance")
        else:
            self.cash -= bet
            self.bet = bet


    def win(self, isSplit, isBJ):

        if isSplit:
            if isBJ:
                self.bj_number += 1
                self.cash += 2.5*self.split_bet
            else:
                self.cash += 2*self.split_bet
            self.split_bet = 0
        else:
            if isBJ:
                self.bj_number += 1
                self.cash += 2.5*self.bet
            else:
                self.cash += 2*self.bet
            self.bet = 0
        self.reset_hand(isSplit)


    def push(self, isSplit):

        if isSplit:
            self.cash += self.split_bet
            self.split_bet = 0
        else:
            self.cash += self.bet
            self.bet = 0
        self.reset_hand(isSplit)


    def lose(self, isSplit):

        if isSplit:
            self.split_bet = 0
        else:
            self.bet = 0
        self.reset_hand(isSplit)


    def reset_hand(self, isSplit):
        if isSplit:
            self.stop_play_split = True
            self.cards_split = []
            self.hand_split_value_1 = 0
            self.hand_split_value_2 = 0
            self.best_split_value = 0
        else:
            self.stop_play = False
            self.cards = []
            self.hand_value_1 = 0
            self.hand_value_2 = 0
            self.best_value = 0


    def isBJ(self, isSplit):
        
        if isSplit:
            if len(self.cards_split) == 2 and self.best_split_value == 21:
                return True
            else:
                return False
        else:
            if len(self.cards) == 2 and self.best_value == 21:
                return True
            else:
                return False


            


    

