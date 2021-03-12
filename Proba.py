from Card import Card

ACTIONS = {
    1 : "STAY",
    2 : "HIT",
    3 : "DOUBLE",
    4 : "SPLIT"
}

PROBA_ARRAY = [
   #[2,3,4,5,6,7,8,9,10,A] 
    [1,1,1,1,1,1,1,1,1,1], #17+
    [1,1,1,1,1,2,2,2,2,2], #16
    [1,1,1,1,1,2,2,2,2,2], #15
    [1,1,1,1,1,2,2,2,2,2], #14
    [1,1,1,1,1,2,2,2,2,2], #13
    [2,2,1,1,1,2,2,2,2,2], #12
    [3,3,3,3,3,3,3,3,3,2], #11
    [3,3,3,3,3,3,3,3,2,2], #10
    [2,3,3,3,2,2,2,2,2,2], #9
    [2,2,2,2,2,2,2,2,2,2], #5 -> 8
    [1,1,1,1,1,1,1,1,1,1], #A-8 -> A-10
    [1,3,3,3,3,1,1,2,2,2], #A-7
    [2,3,3,3,3,2,2,2,2,2], #A-6
    [2,2,3,3,3,2,2,2,2,2], #A-5
    [2,2,3,3,3,2,2,2,2,2], #A-4
    [2,2,2,3,3,2,2,2,2,2], #A-3
    [2,2,2,3,3,2,2,2,2,2], #A-2
    [4,4,4,4,4,4,4,4,4,4], #A-A / 8-8
    [1,1,1,1,1,1,1,1,1,1], #10-10
    [4,4,4,4,4,1,4,4,1,1], #9-9
    [4,4,4,4,4,4,2,2,2,2], #7-7
    [4,4,4,4,4,2,2,2,2,2], #6-6
    [3,3,3,3,3,3,3,3,2,2], #5-5
    [2,2,2,4,4,2,2,2,2,2], #4-4
    [4,4,4,4,4,4,2,2,2,2], #3-3
    [4,4,4,4,4,4,2,2,2,2], #2-2
]


def best_action(player_cards, hand_value_1, hand_value_2, best_value, dealer_card_value, isSplit):
    
    column = dealer_card_value - 2

    if best_value >= 17:
        line = 0
    elif best_value == 16:
        line = 1
    elif best_value == 15:
        line = 2
    elif best_value == 14:
        line = 3
    elif best_value == 13:
        line = 4
    elif best_value == 12:
        line = 5
    elif best_value == 11:
        line = 6
    elif best_value == 10:
        line = 7
    elif best_value == 9:
        line = 8
    elif best_value > 1 and best_value < 9:
        line = 9

    if hand_value_1 != hand_value_2:
        value_without_ace = hand_value_2 - 11
        if value_without_ace == 2:
            line = 16
        elif value_without_ace == 3:
            line = 15
        elif value_without_ace == 4:
            line = 14
        elif value_without_ace == 5:
            line = 13
        elif value_without_ace == 6:
            line = 12
        elif value_without_ace == 7:
            line = 11
        elif value_without_ace > 7 and value_without_ace < 11:
            line = 10
    
    if (len(player_cards) == 2) and (player_cards[0].number == player_cards[1].number):
        if (player_cards[0].number == 1) or (player_cards[0].number == 8):
            if player_cards[0].number == 1 and isSplit:
                line = 9
            elif player_cards[0].number == 8 and isSplit:
                line = 1
            else:
                line = 17
        if player_cards[0].number == 10:
            line = 18
        if player_cards[0].number == 9:
            if isSplit:
                line = 0
            else:
                line = 19
        if player_cards[0].number == 7:
            if isSplit:
                line = 3
            else:
                line = 20
        if player_cards[0].number == 6:
            if isSplit:
                line = 5
            else:
                line = 21
        if player_cards[0].number == 5:
            line = 22
        if player_cards[0].number == 4:
            if isSplit:
                line = 9
            else:
                line = 23
        if player_cards[0].number == 3:
            if isSplit:
                line = 9
            else:
                line = 24
        if player_cards[0].number == 2:
            if isSplit:
                line = 9
            else:
                line = 25

    action = PROBA_ARRAY[line][column]

    if isSplit or len(player_cards) > 2:
        if action == 3:
            action = 2

    return action

            






