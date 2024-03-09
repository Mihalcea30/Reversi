import pygame
import sys
import table
import menu
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
SQUARE_SIZE = TABLE_WIDTH // COLS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
GREY = (169, 169, 169)
BLUE = (0, 0, 255)
FONT_SIZE = 40
matrix = [[-1 for x in range(COLS)] for y in range(ROWS)]

#direction vectors(N, NE, E, SE, S, SW, W, NW)
dx = [0,1,1,1,0,-1,-1, -1]
dy = [-1,-1,0,1,1,1,0, -1]


# Set up the game window
class Reversi:
    def __init__(self):
      self.menu = menu.Menu()
      self.table = table.Table()
      #self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
      pygame.display.set_caption("Reversi")

    def check_element(self, x, y, val):
      return self.table.matrix[x][y] == val

    # Function that if a move can be made from the chosen point in a specific direciton
    def check_line(self, x, y, direction, searched_value):
      i = x + dx[direction]
      j = y + dy[direction]
      if self.check_element(i, j, searched_value) == False:
        return -1

      while(self.table.Inside(i, j) and self.check_element(i, j, searched_value)): # Checking if we are inside the table and have a continous line of the searched value
        i = i + dx[direction]
        j = j + dy[direction]
      if self.check_element(i, j, -1) and self.table.Inside(i, j):
        return(i , j)
      else:
        return -1

    #Function  that colors a line in a valid move

    def color_line(self, x, y, direction, searched_value):
      i = x + dx[direction]
      j = y + dy[direction]
      if self.check_element(i, j, searched_value) == False:
        return -1

      while (self.table.Inside(i, j) and self.check_element(i, j,
                                                            searched_value)):  # Checking if we are inside the table and have a continous line of the searched value
        self.table.matrix[i][j] = 1 - searched_value
        i = i + dx[direction]
        j = j + dy[direction]

      self.table.matrix[i][j] = 1 - searched_value
      self.table.refresh_table()

    #Function to explore possible moves from a specific position

    def check_posibilities(self, x, y):

      for direction in range(8):
        poz = self.check_line(x, y, direction, 1 - self.table.matrix[x][y])
        if(poz != -1):
          self.table.add_circle(poz[1], poz[0], GREY, 0)

    def explore(self, turn): # check all possible moves for the current turn

      for i in range (ROWS):
        for j in range (COLS):
          if self.check_element(i, j, turn):
            self.check_posibilities(i, j)

    #Function that makes a move in the game, picking a position coloring the valid lines
    def make_move(self, x, y, turn):

      for direction in range(8):
        if(self.check_line(x, y, direction, 1 - turn) != -1):
          self.color_line(x, y, direction, 1 - turn)



    def game(self):
        # Main game loop
        self.menu.start_menu()
        # Draw the Reversi board
        self.table.draw_board()
        # Update the display
        pygame.display.flip()
        running = True
        turn = 0
        self.explore(turn)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                      # Get the mouse position
                      mouse_x, mouse_y = pygame.mouse.get_pos()
                      row = (mouse_y - STARTY) // (SQUARE_SIZE )
                      col = (mouse_x - STARTX) //  (SQUARE_SIZE)
                      self.make_move(row, col, turn)
                      turn = 1 - turn
                      self.explore(turn)
                      """"
                      if(row >= 0 and col >= 0):
                        self.table.add_circle(col, row, BLACK)
                        pygame.display.flip()"""

        # Quit Pygame
        pygame.quit()
        sys.exit()

# Create an instance of the Reversi class and start the game

