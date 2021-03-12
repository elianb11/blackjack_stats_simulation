from CardStack import CardStack
from Dealer import Dealer
from Player import Player
from Proba import best_action
import sys

class Gameboard:

    def __init__(self):

        self.deck = CardStack()
        self.players = [Player(1000), Player(1000), Player(1000)]
        self.dealer = Dealer(self.deck)


    def cards_distribution(self):

        for player in self.players:
            player.cards.append(self.deck.draw())
    
        self.dealer.cards.append(self.deck.draw())

        for player in self.players:
            player.cards.append(self.deck.draw())

        self.dealer.cards.append(self.deck.draw())

        print("\nDealer first card : \n{}\nValue : {}\n".format(self.dealer.cards[0], self.dealer.cards[0].value))

        i = 0
        for player in self.players:
            print("Player {} cards :".format(i))
            ace = False
            for card in player.cards:
                print(card)
                if card.number == 1:
                    ace = True
            player.update_values()
            if ace and player.hand_value_2 < 22:
                print("Value : {}/{}\n".format(player.hand_value_1, player.hand_value_2))
            else:
                print("Value : {}\n".format(player.hand_value_1))

            if player.hand_value_2 > player.hand_value_1 and player.hand_value_2 < 22:
                player.best_value = player.hand_value_2
            elif player.hand_value_1 < 22:
                player.best_value = player.hand_value_1

            i += 1

    
    def player_action(self, player, state, split_play):

        if not(split_play) and (player.bet > 0) and not(player.stop_play):
            if state == 1:
                player.stop_play = True
            elif state == 2:
                player.cards.append(self.deck.draw())
            elif state == 3 and ((player.cash - player.bet) >= 0):
                player.cash -= player.bet
                player.bet *= 2
                player.cards.append(self.deck.draw())
                player.stop_play = True
            elif state == 4 and ((player.cash - player.bet) >= 0):
                if (len(player.cards) == 2) and (player.cards[0].number == player.cards[1].number):
                    player.cards_split.append(player.cards.pop())
                    player.cards.append(self.deck.draw())
                    player.cards_split.append(self.deck.draw())
                    player.cash -= player.bet
                    player.split_bet = player.bet
                    player.stop_play_split = False
            else:
                sys.exit("pb 1st hand")
        elif split_play and (player.split_bet > 0) and not(player.stop_play_split):
            if state == 1:
                player.stop_play_split = True
            elif state == 2:
                player.cards_split.append(self.deck.draw())
            elif state == 3 and ((player.cash - player.split_bet) >= 0):
                player.cash -= player.split_bet
                player.split_bet *= 2
                player.cards_split.append(self.deck.draw())
                player.stop_play_split = True
            else:
                sys.exit("pb split hand")
        else:
            sys.exit("pb no action")

        player.update_values()


    def players_turn(self):

        i=0
        for player in self.players:
            while not player.stop_play:
                if player.split_bet == 0:
                    action = best_action(player.cards, player.hand_value_1, player.hand_value_2, player.best_value, self.dealer.cards[0].value, False)
                else:
                    action = best_action(player.cards, player.hand_value_1, player.hand_value_2, player.best_value, self.dealer.cards[0].value, True)
                print("BEST ACTION: "+str(action))
                self.player_action(player, action, False)
                print("\nPlayer {} cards :".format(i))
                ace = False
                for card in player.cards:
                    print(card)
                    if card.number == 1:
                        ace = True
                player.update_values()
                if ace and player.hand_value_2 < 22:
                    print("Value : {}/{}\n".format(player.hand_value_1, player.hand_value_2))
                else:
                    print("Value : {}\n".format(player.hand_value_1))

            while not player.stop_play_split:
                print("\nPlayer {} cards (split):".format(i))
                ace = False
                for card in player.cards_split:
                    print(card)
                    if card.number == 1:
                        ace = True
                player.update_values()
                if ace and player.hand_split_value_2 < 22:
                    print("Value : {}/{}\n".format(player.hand_split_value_1, player.hand_split_value_2))
                else:
                    print("Value : {}\n".format(player.hand_split_value_1))
                action = best_action(player.cards_split, player.hand_split_value_1, player.hand_split_value_2, player.best_split_value, self.dealer.cards[0].value, True)
                print("BEST ACTION: "+str(action))
                self.player_action(player, action, True)
            
            i += 1


    def dealer_draw(self):

        print("Dealer cards :")
        ace = False
        for card in self.dealer.cards:
                print(card)
                if card.number == 1:
                    ace = True
        self.dealer.update_values()
        if ace and self.dealer.hand_value_2 < 22:
            print("Value : {}/{}\n".format(self.dealer.hand_value_1, self.dealer.hand_value_2))
        else:
            print("Value : {}\n".format(self.dealer.hand_value_1))

        while not self.dealer.stop_play:
            self.dealer.cards.append(self.deck.draw())
            for card in self.dealer.cards:
                print(card)
                if card.number == 1:
                    ace = True
            self.dealer.update_values()
            if ace and self.dealer.hand_value_2 < 22:
                print("Value : {}/{}\n".format(self.dealer.hand_value_1, self.dealer.hand_value_2))
            else:
                print("Value : {}\n".format(self.dealer.hand_value_1))
        
        if self.dealer.hand_value_1 > 21:
            print("Dealer busted !\n")
            self.dealer.bust_number += 1
        elif self.dealer.hand_value_2 < 22:
            print("Dealer ends with : {}\n".format(self.dealer.hand_value_2))
        else:
            print("Dealer ends with : {}\n".format(self.dealer.hand_value_1))


    def check_results(self):

        if self.dealer.isBJ():
            self.dealer.bj_number += 1

        for player in self.players:
            if self.dealer.isBJ():
                player.lose(isSplit=False)
                player.lose(isSplit=True)
                player.lose_number += 1
                player.lose_streak += 1
                player.win_streak = 0
            else:
                if player.isBJ(isSplit=False):
                    player.win(isSplit=False, isBJ=True)
                    player.win_number += 1
                    player.win_streak += 1
                    player.lose_streak = 0
                elif self.dealer.best_value > player.best_value:
                    player.lose(isSplit=False)
                    player.lose_number += 1
                    player.lose_streak += 1
                    player.win_streak = 0
                elif self.dealer.best_value == player.best_value:
                    player.push(isSplit=False)
                    player.push_number += 1
                elif self.dealer.best_value < player.best_value:
                    player.win(isSplit=False, isBJ= False)
                    player.win_number += 1
                    player.lose_streak = 0
                    player.win_streak += 1

                if player.split_bet > 0:
                    if player.isBJ(isSplit=True):
                        player.win(isSplit=True, isBJ=True)
                        player.win_number += 1
                        player.win_streak += 1
                        player.lose_streak = 0
                    elif self.dealer.best_value > player.best_split_value:
                        player.lose(isSplit=True)
                        player.lose_number += 1
                        player.lose_streak += 1
                        player.win_streak = 0
                    elif self.dealer.best_value == player.best_split_value:
                        player.push(isSplit=True)
                        player.push_number += 1
                    elif self.dealer.best_value < player.best_split_value:
                        player.win(isSplit=True, isBJ = False)
                        player.win_number += 1
                        player.win_streak += 1
                        player.lose_streak = 0

        self.dealer.reset_hand()


    def play_game(self):

        i=0
        for player in self.players:
            print("Player {} cash: {}".format(i, player.cash))
            bet = player.init_bet
            if bet > player.max_bet:
                player.max_bet = bet
            if player.win_streak > player.max_win_streak:
                player.max_win_streak = player.win_streak
            if player.lose_streak > player.max_lose_streak:
                player.max_lose_streak = player.lose_streak
            player.select_bet(bet)
            print("Player {} bet: {}".format(i, player.bet))
            i += 1

        self.cards_distribution()

        self.players_turn()

        self.dealer_draw()

        self.check_results()

        self.deck.shuffle()


    def get_stats(self):
        print("# SESSION END #\n")
        i=0
        for player in self.players:
            print("Player {}:".format(i))
            print("* Balance: {}".format(player.cash))
            player.profit = player.cash - player.init_balance
            print("* Profit: {}".format(player.profit))
            print("* Max bet: {}".format(player.max_bet))
            print("* Max win streak: {}".format(player.max_win_streak))
            print("* Max lose streak: {}".format(player.max_lose_streak))
            print("* {} wins (including {} BJ)".format(player.win_number, player.bj_number))
            print("* {} pushs".format(player.push_number))
            print("* {} loses\n".format(player.lose_number))
            i+=1