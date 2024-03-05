import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
ROWS = 8
COLS = 8
SQUARE_SIZE = SCREEN_WIDTH // COLS
TABLE_WIDTH = SQUARE_SIZE * COLS
TABLE_HEIGHT = SQUARE_SIZE * ROWS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
GREY = (169, 169, 169)
BLUE = (0, 0, 255)
FONT_SIZE = 40

class Table:

    def __init__(self):
        # Initialize both the matrix and the corresponding screen
        self.matrix = [[-1 for x in range(COLS)] for y in range(ROWS)]
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Reversi")
        # Calculate the starting position to center the table
        self.start_x = 0
        self.start_y = 0

    # Function to add a circle to add a circle in a given square
    def add_circle(self, column, row, color):
        pygame.draw.circle(self.screen, color,
                           (column * SQUARE_SIZE + SQUARE_SIZE // 2 + self.start_x,
                            row * SQUARE_SIZE + SQUARE_SIZE // 2 + self.start_y),
                           SQUARE_SIZE // 2 - 15)

    # Function to draw the Reversi board
    def draw_board(self):


        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(self.screen, GREEN,
                                 (self.start_x + col * SQUARE_SIZE, self.start_y + row * SQUARE_SIZE,
                                  SQUARE_SIZE, SQUARE_SIZE))

        # Draw the grid lines
        for i in range(ROWS + 1):
            pygame.draw.line(self.screen, BLACK, (self.start_x, self.start_y + i * SQUARE_SIZE),
                             (self.start_x + TABLE_WIDTH, self.start_y + i * SQUARE_SIZE))
        for j in range(COLS + 1):
            pygame.draw.line(self.screen, BLACK, (self.start_x + j * SQUARE_SIZE, self.start_y),
                             (self.start_x + j * SQUARE_SIZE, self.start_y + TABLE_HEIGHT))

        # Initialize the first pieces
        middle_row = ROWS // 2 - 1
        middle_col = COLS // 2 - 1
        self.add_circle(middle_col, middle_row, BLACK)
        self.add_circle(middle_col + 1, middle_row, WHITE)
        self.add_circle(middle_col, middle_row + 1, WHITE)
        self.add_circle(middle_col + 1, middle_row + 1, BLACK)
        pygame.display.flip()
        """self.add_circle(middle_col + 1, middle_row + 1, BLACK)
        pygame.draw.circle(self.screen, GREY,
                           ((middle_col + 2) * SQUARE_SIZE + SQUARE_SIZE // 2,
                            (middle_row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2),
                           SQUARE_SIZE // 2 - 15)"""

