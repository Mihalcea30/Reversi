import sys
import time
import pygame

import bot
import reversi
class Game:
    def __init__(self):
        self.game = reversi.Reversi()


    def session(self, botturn = 0):
      # Main game loop
      self.game.menu.start_menu()
      # Draw the Reversi board
      self.game.table.draw_board()
      # Update the display
      pygame.display.flip()
      running = True
      bot_player = bot.Bot()
      turn = 0
      nomove = 0
      if(turn == botturn):
        self.game.table.matrix = bot_player.bot_move(self.game.table, turn)
      self.game.scoreboard(turn)
      self.game.explore(turn)
      while running:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
          elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
              self.game.table.refresh_table()
              # Get the mouse position
              mouse_x, mouse_y = pygame.mouse.get_pos()
              row = (mouse_y - reversi.STARTY) // (reversi.SQUARE_SIZE)
              col = (mouse_x - reversi.STARTX) // (reversi.SQUARE_SIZE)
              if self.game.table.Inside(row, col) and self.game.make_move(row, col, turn) != -1:
                # turn = 1 - turn
                if (1-turn == botturn):
                  print("%")
                  self.game.table.matrix = bot_player.bot_move(self.game.table, 1-turn).matrix
                  self.game.table.refresh_table()
                  self.game.scoreboard(turn)
                  self.game.explore(turn)
                elif (self.game.explore(1 - turn)):
                  nomove = 0
                  turn = 1 - turn

                else:
                  nomove += 1
                  if (not self.game.explore(turn)):
                    nomove += 1

        if (nomove == 2 or self.game.full_table()):  # two consecutive no move rounds or table is full -> the game is over
          self.game.result()

      # Quit Pygame
      pygame.quit()
      sys.exit()
