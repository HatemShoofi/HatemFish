import pygame

WHITE_PIECE_COLOR = (30, 90, 200)
BLACK_PIECE_COLOR = (200, 20, 20) 
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS



class piece:
    def __init__(self, piece_type, color, position):
        self.piece_type = piece_type
        self.color = color
        self.position = position
        self.has_moved = False
        self.dragging = False  # New attribute to track dragging state

    def draw_piece(self, screen, position):
        if self is not None:
            font = pygame.font.Font(None, 48)
            match self.piece_type:
                case "pawn":
                    symbol = "P"
                case "rook":
                    symbol = "R"
                case "knight":
                    symbol = "N"
                case "bishop":
                    symbol = "B"
                case "queen":
                    symbol = "Q"
                case "king":
                    symbol = "K"

            symbol_color = WHITE_PIECE_COLOR if self.color == "white" else BLACK_PIECE_COLOR
            text_surface = font.render(symbol, True, symbol_color)

            if self.dragging:
                x,y = position
            else:
                row, col = position
                x= col * SQUARE_SIZE + SQUARE_SIZE // 2 - text_surface.get_width() // 2
                y= row * SQUARE_SIZE + SQUARE_SIZE // 2 - text_surface.get_height() // 2
            
            screen.blit(text_surface, (x, y))
