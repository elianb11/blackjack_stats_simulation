from Gameboard import Gameboard

gameboard = Gameboard()

for i in range(10000):
    print("# GAME {} #".format(i))
    gameboard.play_game()

gameboard.get_stats()