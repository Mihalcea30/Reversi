import sys
import time
import pygame
import copy

import bot
import reversi
from Nod import Nod


class Game:
    def __init__(self):
        self.game = reversi.Reversi()

    # Function that gets the difficulty set by the human player
    def get_difficulty(self, difficulty):
        if difficulty == 'Easy':
            return (2, 0)
        elif difficulty == 'Medium':
            return (3, 0)
        else:
            return (4, 1)
    # Function that gets the color (white/black) set by the human player
    def get_bot_symbol(self, symbol):
        if symbol == 'White':
            return 1
        else:
            return 0

    # Main game
    def session(self):
      # Initialize the parameters of the game
      input = self.game.menu.start_menu()
      botturn = self.get_bot_symbol(input[1])
      depth = self.get_difficulty(input[0])[0]
      type = self.get_difficulty(input[0])[1] # 0 for weaker evaluation, 1 for stronger evaluation

      self.game.table.draw_board()
      pygame.display.flip()
      running = True
      bot_player = bot.Bot()
      turn = 0 # current turn, 0 for white, 1 for black
      nomove = 0 # number of consecutive no move rounds, if it reaches 2, the game is over

      while running:

        if turn == botturn: # bot's turn
          self.game.scoreboard(turn)
          bot_moved = bot_player.bot_move(self.game.table, turn, depth, type)
          if bot_moved is None:
            # the bot has no possible moves, we move on to the next player
            nomove += 1
            if nomove >= 2:
              self.game.result()
              time.sleep(5)
              running = False
          else:
            nomove = 0
            old_board = copy.deepcopy(self.game.table.matrix)
            self.game.table.matrix = copy.deepcopy(bot_moved.matrix)
            self.game.table.refresh_element(bot_moved.poz)
            time.sleep(0.5)
            self.game.table.refresh_table(old_board)
          turn = 1 - turn
        else:
          self.game.scoreboard(turn)
          if self.game.explore(turn) == 0:
            turn = 1 - turn
            nomove += 1
            # the bot has no possible moves, we move on to the next player
            if nomove >= 2:
              self.game.result()
              time.sleep(5)
              running = False

          else:
            for event in pygame.event.get():
              #print("@")
              if event.type == pygame.QUIT:
                running = False
              elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                  # Get the mouse position
                  mouse_x, mouse_y = pygame.mouse.get_pos()
                  row = (mouse_y - reversi.STARTY) // (reversi.SQUARE_SIZE)
                  col = (mouse_x - reversi.STARTX) // (reversi.SQUARE_SIZE)

                  old_board = copy.deepcopy(self.game.table.matrix)
                  if self.game.table.Inside(row, col) and self.game.make_move(row, col, turn) != -1:
                    # turn = 1 - turn
                    nomove = 0
                    self.game.table.refresh_table(self.game.table.matrix)
                    self.game.table.refresh_element((row, col))
                    time.sleep(0.5)
                    self.game.table.refresh_table(old_board)
                    turn = 1 - turn


      if (nomove >= 2 or self.game.full_table()):  # two consecutive no move rounds or table is full -> the game is over
        self.game.result()

      # Quit Pygame
      pygame.quit()
      sys.exit()
