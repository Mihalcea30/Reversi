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
        bot_moved = bot_player.bot_move(self.game.table, turn)
        old_board = copy.deepcopy(self.game.table.matrix)
        self.game.table.matrix = copy.deepcopy(bot_moved.matrix)
        self.game.table.refresh_element(bot_moved.poz)
        self.game.table.refresh_table(old_board)
        turn = 1 - turn
      self.game.scoreboard(turn)
      self.game.explore(turn)
      while running:
        if self.game.full_table():
          self.game.result()

        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
          elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
              #self.game.table.refresh_table()
              # Get the mouse position
              mouse_x, mouse_y = pygame.mouse.get_pos()
              row = (mouse_y - reversi.STARTY) // (reversi.SQUARE_SIZE)
              col = (mouse_x - reversi.STARTX) // (reversi.SQUARE_SIZE)
              old_board = copy.deepcopy(self.game.table.matrix)
              if self.game.table.Inside(row, col) and self.game.make_move(row, col, turn) != -1:
                # turn = 1 - turn
                self.game.scoreboard(1-turn)
                self.game.table.refresh_table(self.game.table.matrix)
                self.game.table.refresh_element((row, col))
                time.sleep(0.5)
                self.game.table.refresh_table(old_board)
                bot_move_copy = bot_player.bot_move(self.game.table, 1 - turn)
                if (1-turn == botturn and bot_move_copy is not None):
                  old_board = copy.deepcopy(self.game.table.matrix)
                  self.game.table.matrix = copy.deepcopy(bot_move_copy.matrix)
                  self.game.table.refresh_element(bot_move_copy.poz)
                  time.sleep(0.5)
                  self.game.table.refresh_table(old_board)
                  self.game.scoreboard(turn)
                  self.game.explore(turn)
                elif(1-turn == botturn and bot_move_copy == None):

                  #self.game.table.refresh_table()
                  self.game.scoreboard(turn)
                  self.game.explore(turn)
                else:
                  nomove += 1
                  if (not self.game.explore(turn)):
                    nomove += 1

        if (nomove == 2 or self.game.full_table()):  # two consecutive no move rounds or table is full -> the game is over
          self.game.result()

      # Quit Pygame
      pygame.quit()
      sys.exit()
