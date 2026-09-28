ROWS, COLS = 8, 8

class square:
    def __init__(self, position):
        self.position = position
        self.piece = None
        self.occupied = False



    def set_piece(self, piece):
        self.piece = piece
        piece.position = self.position
        self.occupied = True

    def remove_piece(self):
        self.piece = None
        self.occupied = False

    def get_piece(self):
        return self.piece