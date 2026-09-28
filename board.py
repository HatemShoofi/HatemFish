from square import square
from piece import piece
ROWS, COLS = 8, 8

class board:
    def __init__(self):
        self.board = [[square((row, col)) for col in range(COLS)] for row in range(ROWS)]
        self.set_initial_configuration(self)


    def set_initial_configuration(self):

        for row in range(ROWS):
            for col in range(COLS):
                position = (row, col)
                self.board[row][col] = square(position)

        for col in range(COLS):

            self.board[1][col].set_piece(piece("pawn", "black", (1, col)))
            self.board[6][col].set_piece(piece("pawn", "white", (6, col)))

        for col in range(COLS):

            if col == 0 or col == 7:
                self.board[0][col].set_piece(piece("rook", "black", (0, col)))
                self.board[7][col].set_piece(piece("rook", "white", (7, col)))
            elif col == 1 or col == 6:
                self.board[0][col].set_piece(piece("knight", "black", (0, col)))
                self.board[7][col].set_piece(piece("knight", "white", (7, col)))
            elif col == 2 or col == 5:
                self.board[0][col].set_piece(piece("bishop", "black", (0, col)))
                self.board[7][col].set_piece(piece("bishop", "white", (7, col)))
            elif col == 3:
                self.board[0][col].set_piece(piece("queen", "black", (0, col)))
                self.board[7][col].set_piece(piece("queen", "white", (7, col)))
            elif col == 4:
                self.board[0][col].set_piece(piece("king", "black", (0, col)))
                self.board[7][col].set_piece(piece("king", "white", (7, col)))


    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        if(self.check_legal_move(self, start_pos, end_pos) == False):
            return False  # Move is not legal
        
        moving_piece = self.board[start_row][start_col].get_piece()

        # Move the piece to the new square
        self.board[end_row][end_col].set_piece(moving_piece)
        self.board[start_row][start_col].remove_piece()
        moving_piece.has_moved = True  # Mark the piece as having moved
        return True

    def check_legal_move(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        moving_piece = self.board[start_row][start_col].get_piece()

        if moving_piece is None:
            return False  # No piece to move

        return True  # For now, we will assume all moves are legal. You can implement specific rules later.