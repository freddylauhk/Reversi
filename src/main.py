from Gameboard import Gameboard
from Player import Player

def main():

    gameboard = Gameboard()
    gameboard.printBoard()

    whiteSidePlayer = Player(True)
    blackSidePlayer = Player(False)

    while not gameboard.isGameOver():
        try:
            # No available moves pass
            availableMovesList = gameboard.getAvaliableMove(gameboard.getCurrentSide())
            if(len(availableMovesList) == 0):
                print("No available moves, pass!")
                gameboard.switchSide()
                continue

            print("Whiteside" if gameboard.getCurrentSide() == 1 else "Blackside", "available Move: " , availableMovesList)
            userInput = input(("white" if gameboard.getCurrentSide() == 1 else "black") + " turn (split with comma): ")
            position = userInput.split(",")
            position = [int(position[0]), int(position[1])]
            if(position not in availableMovesList):
                print("Invalid move: ", position)
                continue
            gameboard.placePiece(int(position[0]), int(position[1]))
            gameboard.printBoard()

        except Exception as e:
            print(e)


    print(gameboard.getWinner())

if __name__ == "__main__":
    main()