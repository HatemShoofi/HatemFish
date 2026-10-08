import pygame
from board import board
from piece import piece


WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
White = (255, 255, 255)
Light = (240, 217, 181)
Dark = (181, 136, 99)

WHITE_PIECE_COLOR = (30, 90, 200)
BLACK_PIECE_COLOR = (200, 20, 20)    

SQUARE_SIZE = WIDTH // COLS


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HatemFish")
running = True
Board = board()
Mouse_Attached_Piece = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                print(f"Mouse clicked at: ({mouse_x}, {mouse_y})")
                board_x, board_y = mouse_x // SQUARE_SIZE, mouse_y // SQUARE_SIZE
                if Board.get_piece_at((board_y, board_x)) is not None:
                    Mouse_Attached_Piece = Board.get_piece_at((board_y, board_x))
                    Mouse_Attached_Piece.dragging = True
                    Board.handle_mouse_down((mouse_x, mouse_y), screen)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                print(f"Mouse released at: ({mouse_x}, {mouse_y})")
                if Mouse_Attached_Piece is not None:
                    Mouse_Attached_Piece.dragging = False
                    mouse_board_x, mouse_board_y = mouse_x // SQUARE_SIZE, mouse_y // SQUARE_SIZE
                    Mouse_Attached_Piece.position = (mouse_board_y, mouse_board_x)
                    ##Board.handle_mouse_up((mouse_board_x, mouse_board_y), screen)

                    Mouse_Attached_Piece = None


            
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            print(f"Mouse moved to: ({mouse_x}, {mouse_y})")
            if Mouse_Attached_Piece is not None:
                if Mouse_Attached_Piece.dragging:
                    Mouse_Attached_Piece.position = (mouse_x, mouse_y)
                    Board.handle_mouse_movement((mouse_x, mouse_y), screen, Mouse_Attached_Piece)



    Board.draw_board(screen, Mouse_Attached_Piece)




pygame.quit()