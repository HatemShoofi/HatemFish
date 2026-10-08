import pygame
from square import square
from piece import piece

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
WHITE_PIECE_COLOR = (30, 90, 200)
BLACK_PIECE_COLOR = (200, 20, 20) 
Light = (240, 217, 181)
Dark = (181, 136, 99)
White = (255, 255, 255)


class board:
    def __init__(self):
        self.board = [[square((row, col)) for col in range(COLS)] for row in range(ROWS)]
        self.set_initial_configuration()
        self.initial_pos = None
        self.final_pos = None


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

def set_piece(self, position, piece):

    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        if(self.check_legal_move(start_pos, end_pos) == False):
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

    def get_piece_at(self, position):
        row, col = position
        return self.board[row][col].get_piece()

    def draw_board(self, screen, Mouse_Attached_Piece=None):
        screen.fill(White) # Fill the screen with white color
        
        for row in range(ROWS):
            for col in range(COLS):
                color = Light if (row + col) % 2 == 0 else Dark
                square_background = pygame.Rect(col * 100, row * 100, 100, 100)
                pygame.draw.rect(screen, color, square_background)


        for row in range(ROWS):
            for col in range(COLS):
                piece = self.get_piece_at((row, col))
                if piece is not None:
                    if not piece.dragging:
                        piece.draw_piece(screen, piece.position) 

        if Mouse_Attached_Piece is not None:
            Mouse_Attached_Piece.draw_piece(screen, Mouse_Attached_Piece.position) 
        pygame.display.flip()

    def handle_mouse_down(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        board_x, board_y = mouse_x // SQUARE_SIZE, mouse_y // SQUARE_SIZE
        piece = self.get_piece_at((board_y, board_x))
        if piece is not None:
            piece.dragging = True
            self.initial_pos = (board_y, board_x)
            self.final_pos = None
            print(f"Mouse down on piece at: {self.initial_pos}")

    def handle_mouse_movement(self, mouse_pos, Mouse_Attached_Piece):
        mouse_x, mouse_y = mouse_pos
        print(f"Mouse moved to: ({mouse_x}, {mouse_y})")
            

    def handle_mouse_up(self, mouse_pos, Mouse_Attached_Piece):
        mouse_x, mouse_y = mouse_pos
        board_x, board_y = mouse_x // SQUARE_SIZE, mouse_y // SQUARE_SIZE
        self.board[board_y][board_x].set_piece(Mouse_Attached_Piece)
        self.board[self.initial_pos[0]][self.initial_pos[1]].remove_piece()
        self.initial_pos = None
        Mouse_Attached_Piece.position = (board_y, board_x)
        Mouse_Attached_Piece.dragging = False
        print(f"Mouse released on piece at: ({board_y}, {board_x})")
        self.final_pos = (board_y, board_x)