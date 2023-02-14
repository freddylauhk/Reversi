class Player:
    def __init__(self, whiteside: bool) -> None:
        if whiteside:
            self.piece_type = 1
            self.cursor_position = (3, 3)
            print("White side player initialized")
        else:
            self.piece_type = 2
            self.cursor_position = (3, 4)
            print("Black side player initialized")

    def get_piece_type(self) -> int:
        return self.piece_type

    def get_cursor_position(self) -> tuple[int, int]:
        color = "White" if self.piece_type == 1 else "Black"
        row, col = self.cursor_position
        print(f"{color} Position is [{row}, {col}]")
        return self.cursor_position

    def set_cursor_position(self, row: int, col: int) -> None:
        self.cursor_position = (row, col)
