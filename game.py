import pygame
import sys
import table
import menu
import time
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
font = pygame.font.Font(None, 36)
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
      if not(self.table.Inside(x, y)):
        return False
      return self.table.matrix[x][y] == val

    # Function that if a move can be made from the chosen point in a specific direciton
    def check_line(self, x, y, direction, searched_value, last_element): #last_element - what we want to find on the last positions to
                                                                        # differenciate the checking for exploring and making a move

      i = x + dx[direction]
      j = y + dy[direction]
      if self.check_element(i, j, searched_value) == False:
        return -1
      while(self.table.Inside(i, j) and self.check_element(i, j, searched_value)): # Checking if we are inside the table and have a continous line of the searched value
        i = i + dx[direction]
        j = j + dy[direction]
      if self.check_element(i, j, last_element) and self.table.Inside(i, j):
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
      ok = False
      for direction in range(8):
        poz = self.check_line(x, y, direction, 1 - self.table.matrix[x][y], -1)
        if(poz != -1):
          self.table.add_circle(poz[1], poz[0], GREY, 1.3)
          ok = True

      pygame.display.flip()
      return ok


    def explore(self, turn): # check all possible moves for the current turn

      ok = False
      for i in range (ROWS):
        for j in range (COLS):
          if self.check_element(i, j, turn):
            if self.check_posibilities(i, j) == True:
              ok = True
      return ok


    #Function that makes a move in the game, picking a position coloring the valid lines
    def make_move(self, x, y, turn):
      if self.table.matrix[x][y] != -1:
        return -1 # if we choose an invalid position (one with an piece already on the table) we don t make a move
      if self.table.matrix[x][y] != turn:
        self.table.matrix[x][y] = turn
      for direction in range(8):
        if(self.check_line(x, y, direction, 1 - turn, turn) != -1):

          self.color_line(x, y, direction, 1 - turn)

    #Function that shows the scoreboard with the current scores
    def scoreboard(self, turn):


      self.table.scoreboard.update_score(self.table.matrix)
      self.table.screen.fill(WHITE, rect=(0, 0, 2000 , 150))
      b = font.render("Black Score: " + str(self.table.scoreboard.black), True, BLACK)
      w = font.render("White Score: " + str(self.table.scoreboard.white), True, BLACK)
      blackturn = font.render("<-    Your Turn! ", True, BLACK)
      whiteturn = font.render("<-    Your Turn! ", True, BLACK)

      self.table.screen.blit(b, (20, 20))
      self.table.screen.blit(w, (20, 60))
      if(turn == 1):
        self.table.screen.blit(blackturn, (240, 20))
      else:
        self.table.screen.blit(whiteturn, (240, 60))

    #Function to determine the winner or if it's a tie
    def result(self):
      self.table.screen.fill(WHITE, rect=(0, 0, 2000, 150))
      b = font.render("Black Won! " , True, BLACK)
      w = font.render("White Won! " ,True, BLACK)
      t = font.render("Tie! ", True, BLACK)
      if(self.table.scoreboard.black > self.table.scoreboard.white):
        self.table.screen.blit(b, (240, 20))
      elif(self.table.scoreboard.black < self.table.scoreboard.white):
        self.table.screen.blit(w, (240, 20))
      else:
        self.table.screen.blit(t, (240, 20))
      pygame.display.flip()

      #Function to determine if the table is full to end the game
    def full_table(self):
      n = len(self.table.matrix)
      m = len(self.table.matrix[0])
      for i in range(n):
        for j in range(m):
          if self.table.matrix[i][j] != -1:
            return False
      return True

    def game(self):
        # Main game loop
        self.menu.start_menu()
        # Draw the Reversi board
        self.table.draw_board()
        # Update the display
        pygame.display.flip()
        running = True
        turn = 0
        nomove = 0

        self.scoreboard(turn)
        self.explore(turn)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                      self.table.refresh_table()
                      # Get the mouse position
                      mouse_x, mouse_y = pygame.mouse.get_pos()
                      row = (mouse_y - STARTY) // (SQUARE_SIZE )
                      col = (mouse_x - STARTX) //  (SQUARE_SIZE)
                      if self.table.Inside(row, col) and self.make_move(row, col, turn) != -1:
                        #turn = 1 - turn
                        self.scoreboard(turn)
                        if(self.explore(1 - turn)):
                          nomove = 0
                          turn = 1 - turn
                          self.explore(turn)
                        else:
                          nomove+=1
                          if(not self.explore(turn)):
                            nomove +=1

            if (nomove == 2 or self.full_table()):  # two consecutive no move rounds or table is full -> the game is over
              self.result()






        # Quit Pygame
        pygame.quit()
        sys.exit()

# Create an instance of the Reversi class and start the game

