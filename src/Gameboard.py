from matplotlib.style import available


class Gameboard:
    
    __boardsize = 8
    __maxboardsizeIndex = __boardsize - 1
    __currentSide = 2
    __board = []

    def __init__(self):
        for row in range(self.__boardsize):
            temparray = []
            for column in range(self.__boardsize):
                temparray.append(0)
            
            self.__board.append(temparray)

        self.__board[3][3] = 1
        self.__board[3][4] = 2
        self.__board[4][3] = 2
        self.__board[4][4] = 1

        print("Gameboard initialized")

    def placePiece(self, row, column):

        nullpiece = 0
        enermyPiece = 2 if self.getCurrentSide() == 1 else 1
        if self.__board[row][column] != 0:
            raise Exception("Not empty position")
        self.__board[row][column] = self.getCurrentSide()

        # flip pieces

        # Horizontal
        # Horizontal Left
        horizontalFliper = column
        if(column != 0):
            for horizontalChecker in range(column - 1, 0 , -1):
                if self.__board[row][horizontalChecker] == enermyPiece:
                    continue
                elif self.__board[row][horizontalChecker] == self.getCurrentSide():
                    horizontalFliper = horizontalChecker
                    break
                elif self.__board[row][horizontalChecker] == nullpiece:
                    break

        if(horizontalFliper < column):
            for fliper in range(horizontalFliper + 1, column):
                self.flipPiece(row,fliper)

        # Horizontal Right
        horizontalFliper = column
        if(column != self.__maxboardsizeIndex):
            for horizontalChecker in range(column + 1, self.__boardsize):
                if self.__board[row][horizontalChecker] == enermyPiece:
                    continue
                elif self.__board[row][horizontalChecker] == self.getCurrentSide():
                    horizontalFliper = horizontalChecker
                    break
                elif self.__board[row][horizontalChecker] == nullpiece:
                    break
        
        if(horizontalFliper > column):
            for fliper in range(column + 1 , horizontalFliper):
                self.flipPiece(row,fliper)


        # Vertical
        # Vertical Left
        verticalFliper = row
        if(row != 0):
            for verticalChecker in range(row - 1, 0 , -1):
                if self.__board[verticalChecker][column] == enermyPiece:
                    continue
                elif self.__board[verticalChecker][column] == self.getCurrentSide():
                    verticalFliper = verticalChecker
                    break
                elif self.__board[verticalChecker][column] == nullpiece:
                    break

        if(verticalFliper < row):
            for fliper in range(verticalFliper + 1, row):
                self.flipPiece(fliper,column)

        # Vertical Right
        verticalFliper = row
        if(row != self.__maxboardsizeIndex):
            for verticalChecker in range(row + 1, self.__boardsize):
                if self.__board[verticalChecker][column] == enermyPiece:
                    continue
                elif self.__board[verticalChecker][column] == self.getCurrentSide():
                    verticalFliper = verticalChecker
                    break
                elif self.__board[verticalChecker][column] == nullpiece:
                    break
        
        if(verticalFliper > row):
            for fliper in range(row + 1 , verticalFliper):
                self.flipPiece(fliper, column)

        # Diagonal
        # Top left
        diagonalFliper = 0
        if(row != 0 and column != 0):
            for diagonalChecker in range(1, (row if row < column else column) + 1):
                if self.__board[row - diagonalChecker][column - diagonalChecker] == enermyPiece:
                    continue
                elif self.__board[row - diagonalChecker][column - diagonalChecker] == self.getCurrentSide():
                    diagonalFliper = diagonalChecker
                    break
                elif self.__board[row - diagonalChecker][column - diagonalChecker] == nullpiece:
                    break

        if diagonalFliper > 0:
            for fliper in range(1, diagonalFliper):
                self.flipPiece(row - fliper, column - fliper)

        # Top right
        diagonalFliper = 0
        if(row != 0 and column != self.__maxboardsizeIndex):
            for diagonalChecker in range(1, (row if row < self.__maxboardsizeIndex - column else self.__maxboardsizeIndex - column) + 1):
                if self.__board[row - diagonalChecker][column + diagonalChecker] == enermyPiece:
                    continue
                elif self.__board[row - diagonalChecker][column + diagonalChecker] == self.getCurrentSide():
                    diagonalFliper = diagonalChecker
                    break
                elif self.__board[row - diagonalChecker][column + diagonalChecker] == nullpiece:
                    break

        if diagonalFliper > 0:
            for fliper in range(1, diagonalFliper):
                self.flipPiece(row - fliper, column + fliper)

        # Bottom left
        diagonalFliper = 0
        if(row != self.__maxboardsizeIndex and column != 0):
            for diagonalChecker in range(1, (self.__maxboardsizeIndex - row if self.__maxboardsizeIndex - row < column else column) + 1):
                if self.__board[row + diagonalChecker][column - diagonalChecker] == enermyPiece:
                    continue
                elif self.__board[row + diagonalChecker][column - diagonalChecker] == self.getCurrentSide():
                    diagonalFliper = diagonalChecker
                    break
                elif self.__board[row + diagonalChecker][column - diagonalChecker] == nullpiece:
                    break

        if diagonalFliper > 0:
            for fliper in range(1, diagonalFliper):
                self.flipPiece(row + fliper, column - fliper)

        # Bottom right
        diagonalFliper = 0
        if(row != self.__maxboardsizeIndex and column != self.__maxboardsizeIndex):
            for diagonalChecker in range(1, (self.__maxboardsizeIndex - row if row > column else self.__maxboardsizeIndex - column) + 1):
                if self.__board[row + diagonalChecker][column + diagonalChecker] == enermyPiece:
                    continue
                elif self.__board[row + diagonalChecker][column + diagonalChecker] == self.getCurrentSide():
                    diagonalFliper = diagonalChecker
                    break
                elif self.__board[row + diagonalChecker][column + diagonalChecker] == nullpiece:
                    break

        if diagonalFliper > 0:
            for fliper in range(1, diagonalFliper):
                self.flipPiece(row + fliper, column + fliper)
        
        self.switchSide()
            

    def flipPiece(self, row, column):
        if self.__board[row][column] == 1:
            self.__board[row][column] = 2
        elif self.__board[row][column] == 2:
            self.__board[row][column] = 1


    def getAvaliableMove(self, pieceType):

        nullpiece = 0
        enermyPiece = 2 if pieceType == 1 else 1

        availableMoveList = []

        for row in range(self.__boardsize):
            for column in range(self.__boardsize):
                if(self.__board[row][column] == pieceType):

                    # Horizontal
                    # Horizontal Left
                    horizontalPointer = column
                    if(column != 0):
                        for horizontalChecker in range(column - 1, 0 , -1):
                            if self.__board[row][horizontalChecker] == enermyPiece:
                                continue
                            elif self.__board[row][horizontalChecker] == pieceType:
                                break
                            elif self.__board[row][horizontalChecker] == nullpiece:
                                horizontalPointer = horizontalChecker
                                break

                    if(horizontalPointer < column - 1):
                        availableMoveList.append([row,horizontalPointer])

                    # Horizontal Right
                    horizontalPointer = column
                    if(column != self.__maxboardsizeIndex):
                        for horizontalChecker in range(column + 1, self.__boardsize):
                            if self.__board[row][horizontalChecker] == enermyPiece:
                                continue
                            elif self.__board[row][horizontalChecker] == pieceType:
                                break
                            elif self.__board[row][horizontalChecker] == nullpiece:
                                horizontalPointer = horizontalChecker
                                break
                    
                    if(horizontalPointer > column + 1):
                        availableMoveList.append([row,horizontalPointer])
                    
                    # Vertical
                    # Vertical Top
                    verticalPointer = row
                    if(row != 0):
                        for verticalChecker in range(row - 1, 0 , -1):
                            if self.__board[verticalChecker][column] == enermyPiece:
                                continue
                            elif self.__board[verticalChecker][column] == pieceType:
                                break
                            elif self.__board[verticalChecker][column] == nullpiece:
                                verticalPointer = verticalChecker
                                break

                    if(verticalPointer < row - 1):
                        availableMoveList.append([verticalPointer,column])

                    # Vertical Bottom
                    verticalPointer = row
                    if(row != self.__maxboardsizeIndex):
                        for verticalChecker in range(row + 1, self.__boardsize):
                            if self.__board[verticalChecker][column] == enermyPiece:
                                continue
                            elif self.__board[verticalChecker][column] == pieceType:
                                break
                            elif self.__board[verticalChecker][column] == nullpiece:
                                verticalPointer = verticalChecker
                                break
                    
                    if(verticalPointer > row + 1):
                        availableMoveList.append([verticalPointer,column])

                    # Diagonal
                    # Top Left
                    diagonalPointer = 0
                    if(row != 0 and column != 0):
                        for diagonalChecker in range(1, (row if row < column else column) + 1):
                            if self.__board[row - diagonalChecker][column - diagonalChecker] == enermyPiece:
                                continue
                            elif self.__board[row - diagonalChecker][column - diagonalChecker] == pieceType:
                                break
                            elif self.__board[row - diagonalChecker][column - diagonalChecker] == nullpiece:
                                diagonalPointer = diagonalChecker
                                break

                    if diagonalPointer > 1:
                        availableMoveList.append([row - diagonalPointer, column - diagonalPointer])

                    # Top Right
                    diagonalPointer = 0
                    if(row != 0 and column != self.__maxboardsizeIndex):
                        for diagonalChecker in range(1, (row if row < self.__maxboardsizeIndex - column else self.__maxboardsizeIndex - column) + 1):
                            if self.__board[row - diagonalChecker][column + diagonalChecker] == enermyPiece:
                                continue
                            elif self.__board[row - diagonalChecker][column + diagonalChecker] == pieceType:
                                break
                            elif self.__board[row - diagonalChecker][column + diagonalChecker] == nullpiece:
                                diagonalPointer = diagonalChecker
                                break

                    if diagonalPointer > 1:
                        availableMoveList.append([row - diagonalPointer, column + diagonalPointer])

                    # Bottom left
                    # Bottom left
                    diagonalPointer = 0
                    if(row != self.__maxboardsizeIndex and column != 0):
                        for diagonalChecker in range(1, (self.__maxboardsizeIndex - row if self.__maxboardsizeIndex - row < column else column) + 1):
                            if self.__board[row + diagonalChecker][column - diagonalChecker] == enermyPiece:
                                continue
                            elif self.__board[row + diagonalChecker][column - diagonalChecker] == pieceType:
                                break
                            elif self.__board[row + diagonalChecker][column - diagonalChecker] == nullpiece:
                                diagonalPointer = diagonalChecker
                                break

                    if diagonalPointer > 1:
                        availableMoveList.append([row + diagonalPointer, column - diagonalPointer])

                    # Bottom right
                    diagonalPointer = 0
                    if(row != self.__maxboardsizeIndex and column != self.__maxboardsizeIndex):
                        for diagonalChecker in range(1, (self.__maxboardsizeIndex - row if row > column else self.__maxboardsizeIndex - column) + 1):
                            if self.__board[row + diagonalChecker][column + diagonalChecker] == enermyPiece:
                                continue
                            elif self.__board[row + diagonalChecker][column + diagonalChecker] == pieceType:
                                break
                            elif self.__board[row + diagonalChecker][column + diagonalChecker] == nullpiece:
                                diagonalPointer = diagonalChecker
                                break

                    if diagonalPointer > 1:
                        availableMoveList.append([row + diagonalPointer ,column + diagonalPointer])
        
        # remove duplicate
        availableMoveList = set(map(tuple, availableMoveList))

        return list(map(list, availableMoveList))


    def countPiecesOnBoard(self, pieceType):
        count = 0
        for row in range(self.__boardsize):
            for column in range(self.__boardsize):
                if(self.__board[row][column] == pieceType):
                    count += 1
        
        return count

    def getWinner(self):
        print("Number of White pieces on board: %d" % self.countPiecesOnBoard(1))
        print("Number of Black pieces on board: %d" % self.countPiecesOnBoard(2))

        if(self.countPiecesOnBoard(1) == self.countPiecesOnBoard(2)):
            print("Tie!")
        elif(self.countPiecesOnBoard(1) > self.countPiecesOnBoard(2)):
            print("White wins!")
        else:
            print("Black wins!")

    def getBoard(self):
        return self.__board

    def printBoard(self):
        for i in self.__board:
            print(i)

    def switchSide(self):
        if self.__currentSide == 1:
            self.__currentSide = 2
        else:
            self.__currentSide = 1

    def isGameOver(self):
        if(len(self.getAvaliableMove(1)) == 0 and len(self.getAvaliableMove(2)) == 0):
            return True
        else:
            return False

    def getCurrentSide(self):
        return self.__currentSide

    def resetBoard(self):
        for row in range(self.__boardsize):
            temparray = []
            for column in range(self.__boardsize):
                temparray.append(0)
        
        self.__board[3][3] = 1
        self.__board[3][4] = 2
        self.__board[4][3] = 2
        self.__board[4][4] = 1

        print("Gameboard reset completed")
