from Gameboard import Gameboard
from Player import Player

def main():
    gameboard = Gameboard()
    gameboard.printBoard()

    whiteSidePlayer = Player(True)
    blackSidePlayer = Player(False)

    whiteSidePlayer.getCursorPosition()
    blackSidePlayer.getCursorPosition()

main()