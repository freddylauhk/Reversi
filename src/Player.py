class Player:

    __pieceType = 0
    __rowCursor = 0
    __columnCursor = 0

    def __init__(self, whiteside):
        if whiteside:
            self.__pieceType = 1
            self.__rowCursor = 3
            self.__columnCursor = 3
            print("White side player initialized")
        else:
            self.__pieceType = 2
            self.__rowCursor = 3
            self.__columnCursor = 4
            print("Black side player initialized")

    def getPieceType(self):
        return self.__pieceType

    def getCursorPosition(self):
        print("White" if self.__pieceType == 1 else "Black" , "Position is [", self.__rowCursor, ",", self.__columnCursor, "]")
        return [self.__rowCursor, self.__columnCursor]
    
    def setCursorPosition(self, row, column):
        self.__rowCursor = row
        self.__columnCursor = column