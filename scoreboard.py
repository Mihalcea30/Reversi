import pygame
BLACK = (0, 0, 0)

class Scoreboard:
  def __init__(self):
    self.black = 2
    self.white = 2
  def update_score(self, matrix):
    black = 0
    white = 0
    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
          if(matrix[i][j] == 0):
            white += 1
          elif matrix[i][j] == 1:
            black += 1
    self.black = black
    self.white = white
