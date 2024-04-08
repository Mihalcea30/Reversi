import time

import pygame
import sys
import copy

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

    # Function to add a circle  in a given square
    def add_circle(self, column, row, color, type):
        pygame.draw.circle(self.screen, color,
                           (column * SQUARE_SIZE + SQUARE_SIZE // 2 + STARTX,
                            row * SQUARE_SIZE + SQUARE_SIZE // 2 + STARTY),
                           SQUARE_SIZE // 2 - (15 * type))

    # Function that checks if a position is inside the table
    def Inside(self, i, j):
      return i >= 0 and i < ROWS and j >= 0 and j < COLS

    # Function to check if the matrix had changed and color the table accordingly

    def refresh_table(self, old_board):
      for i in range(ROWS):
        for j in range(COLS):
          if(self.matrix[i][j] == -1):
            self.add_circle(j, i, GREEN, 1)
      pygame.display.flip()
      for i in range(ROWS):
        for j in range(COLS):
          if self.matrix[i][j] != old_board[i][j]:
            if self.matrix[i][j] == 1:
              self.add_circle(j, i, BLACK, 1)
              time.sleep(0.05)
              pygame.display.flip()
            elif self.matrix[i][j] == 0:
              self.add_circle(j, i, WHITE, 1)
              time.sleep(0.05)
              pygame.display.flip()

    # Function that refreshes a single element of the table, so the move can be seen
    def refresh_element(self, i):
      if(self.matrix[i[0]][i[1]] == -1):
        self.add_circle(i[1], i[0], GREEN, 1)
      elif self.matrix[i[0]][i[1]] == 1:
        self.add_circle(i[1], i[0], BLACK, 1)
      elif self.matrix[i[0]][i[1]] == 0:
        self.add_circle(i[1], i[0], WHITE, 1)
      pygame.display.flip()




    # Function to draw the Reversi board
    def draw_board(self):
      # Fill the background
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

      empty_matrix = [[-1 for i in range(8)] for j in range(8)]
      self.refresh_table(empty_matrix)
      pygame.display.flip()


