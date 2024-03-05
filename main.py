import pygame
import sys
import table
import menu
# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
ROWS = 8
COLS = 8
SQUARE_SIZE = SCREEN_WIDTH // COLS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
GREY = (169, 169, 169)
BLUE = (0, 0, 255)
FONT_SIZE = 40
matrix = [[-1 for x in range(COLS)] for y in range(ROWS)]


# Set up the game window
class Reversi:
    def __init__(self):
      self.menu = menu.Menu()
      self.table = table.Table()
      #self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
      pygame.display.set_caption("Reversi")



    def game(self):
        # Main game loop
        self.menu.start_menu()
        # Draw the Reversi board
        self.table.draw_board()
        # Update the display
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                      # Get the mouse position
                      mouse_x, mouse_y = pygame.mouse.get_pos()
                      row = mouse_y // (SQUARE_SIZE )
                      col = mouse_x //  (SQUARE_SIZE)
                      # Draw a circle where the mouse was clicked
                      self.table.add_circle(col, row, BLACK)
                      pygame.display.flip()

        # Quit Pygame
        pygame.quit()
        sys.exit()

# Create an instance of the Reversi class and start the game
R = Reversi()
R.game()
