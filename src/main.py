from Gameboard import Gameboard
from Player import Player

def main():
    gameboard = Gameboard()
    gameboard.printBoard()

    whiteSidePlayer = Player(True)
    blackSidePlayer = Player(False)

    while not gameboard.isGameOver():
        try:
            userInput = input(("white" if gameboard.getCurrentSide() == 1 else "black") + " turn (split with comma): ")
            position = userInput.split(",")
            gameboard.placePiece(int(position[0]), int(position[1]))
            gameboard.printBoard()
        except Exception as e:
            print(e)
    print("someone win")
    #whiteSidePlayer.getCursorPosition()
    #blackSidePlayer.getCursorPosition()

main()