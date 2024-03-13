import pygame
import sys

import scoreboard

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
TABLE_WIDTH = 600
TABLE_HEIGHT = 600
STARTX = 100
STARTY = 150


ROWS = 8
COLS = 8
SQUARE_SIZE = TABLE_HEIGHT // COLS

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
        self.scoreboard = scoreboard.Scoreboard()
        pygame.display.set_caption("Reversi")
        # Calculate the starting position to center the table
        self.start_x = 0
        self.start_y = 0

    # Function to add a circle to add a circle in a given square
    def add_circle(self, column, row, color, type):

        pygame.draw.circle(self.screen, color,
                           (column * SQUARE_SIZE + SQUARE_SIZE // 2 + STARTX,
                            row * SQUARE_SIZE + SQUARE_SIZE // 2 + STARTY),
                           SQUARE_SIZE // 2 - (15 * type))

    # Function that checks if a position is inside the table
    def Inside(self, i, j):
      return i >= 0 and i < ROWS and j >= 0 and j < COLS
    # Function to check the matrix and color the table accordingly

    def refresh_table(self):
      for i in range(ROWS):
        for j in range(COLS):
          if self.matrix[i][j] == 1:
            self.add_circle(j, i, BLACK, 1)
          elif self.matrix[i][j] == 0:
            self.add_circle(j, i, WHITE, 1)
          else:
            self.add_circle(j, i, GREEN, 1)



    # Function to draw the Reversi board
    def draw_board(self):

      """ for row in range(ROWS):
                  for col in range(COLS):
                      pygame.draw.rect(self.screen, GREEN,
                                       (self.start_x + col * SQUARE_SIZE, self.start_y + row * SQUARE_SIZE,
                                        SQUARE_SIZE, SQUARE_SIZE))"""
      pygame.draw.rect(self.screen, GREEN, (STARTX, STARTY, TABLE_WIDTH, TABLE_HEIGHT))
      # Draw the grid lines
      for i in range(ROWS + 1):
            pygame.draw.line(self.screen, BLACK, (STARTX, STARTY + i * SQUARE_SIZE),
                             (STARTX + TABLE_WIDTH, STARTY + i * SQUARE_SIZE))
      for j in range(COLS + 1):
            pygame.draw.line(self.screen, BLACK, (STARTX + j * SQUARE_SIZE, STARTY),
                             (STARTX + j * SQUARE_SIZE, STARTY+ TABLE_HEIGHT))

      # Initialize the first pieces
      middle_row = ROWS // 2 - 1
      middle_col = COLS // 2 - 1
      self.matrix[middle_row][middle_col] = 0
      self.matrix[middle_row + 1][middle_col] = 1
      self.matrix[middle_row][middle_col + 1] = 1
      self.matrix[middle_row + 1][middle_col + 1] = 0
      """self.add_circle(middle_col, middle_row, BLACK)
      self.add_circle(middle_col + 1, middle_row, WHITE)
      self.add_circle(middle_col, middle_row + 1, WHITE)
      self.add_circle(middle_col + 1, middle_row + 1, BLACK)"""
      self.refresh_table()
      pygame.display.flip()
      """self.add_circle(middle_col + 1, middle_row + 1, BLACK)
      pygame.draw.circle(self.screen, GREY,
                           ((middle_col + 2) * SQUARE_SIZE + SQUARE_SIZE // 2,
                            (middle_row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2),
                           SQUARE_SIZE // 2 - 15)"""

