from copy import copy, deepcopy
import numpy as np
import table
import reversi
dx = [0,1,1,1,0,-1,-1, -1]
dy = [-1,-1,0,1,1,1,0, -1]
ROWS = 8
COLS = 8

class Nod:

  def __init__(self, matrix, turn = 0, father = None) :
    self.turn = turn
    self.matrix = matrix
    self.father = father
    self.succesors = []
    self.value = 0
    for i in range(0, 8):
      for j in range(0, 8):
        if(self.matrix[i][j] == 0):
          self.value += 1

  def __eq__(self, cls):
     return self.matrix == cls.matrix

  #verificam daca starea in care suntem este una terminala
  def terminal_node(self):
    return not (any(-1 in line for line in self.matrix))

  def drumRadacina(self):
    ''' Calculeaza lista nodurilor de la radacina pana la nodul curent. '''
    if self.father is None:
      return [self]
    return self.father.drumRadacina() + [self]

  def vizitat(self):
    ''' Returneaza True daca nodul curent a fost deja vizitat, False altfel. '''
    return len([1 for nod in self.drumRadacina() if nod == self]) > 1

  def Inside(self, i, j):
    return i >= 0 and i < ROWS and j >= 0 and j < COLS

  # Function to check the matrix and color the table accordingly
  def check_element(self, x, y, val):
    if not (self.Inside(x, y)):
      return False
    return self.matrix[x][y] == val
  def check_line(self, x, y, direction, searched_value,
                 last_element):  # last_element - what we want to find on the last positions to
    # differenciate the checking for exploring and making a move

    i = x + dx[direction]
    j = y + dy[direction]
    if self.check_element(i, j, searched_value) == False:
      return -1
    while (self.Inside(i, j) and self.check_element(i, j,
                                                          searched_value)):  # Checking if we are inside the table and have a continous line of the searched value
      i = i + dx[direction]
      j = j + dy[direction]
    if self.check_element(i, j, last_element) and self.Inside(i, j):
      return (i, j)
    else:
      return -1

  def color_line(self, x, y, direction, searched_value):

    i = x + dx[direction]
    j = y + dy[direction]
    if self.check_element(i, j, searched_value) == False:
      return -1

    while (self.Inside(i, j) and self.check_element(i, j,
                                                          searched_value)):  # Checking if we are inside the table and have a continous line of the searched value
      self.matrix[i][j] = 1 - searched_value
      i = i + dx[direction]
      j = j + dy[direction]

    self.matrix[i][j] = 1 - searched_value

  def make_move(self, x, y, turn):
    if self.matrix[x][y] != -1:
      return -1  # if we choose an invalid position (one with a piece already on the table) we don t make a move

    ok = False
    for direction in range(8):
      if (self.check_line(x, y, direction, 1 - turn, turn) != -1):
        ok = True
        self.color_line(x, y, direction, 1 - turn)
    if ok == False:
      return -1
    if self.matrix[x][y] != turn and ok == True:
      self.matrix[x][y] = turn
  def succesori(self):
    ''' Calculeaza lista succesorilor directi ai starii curente.

    :return: lista starilor admisibile
    '''
    succesori = []
    if (self.terminal_node()):
      return succesori
  #r = Nod(self.matrix, self.turn, self.father)
    for i in range(0, 8):
      for j in range(0, 8):
        cpy_matrix = deepcopy(self.matrix)
        cpy = Nod(cpy_matrix, self.turn, self.father)
        #cpy.table.matrix = deepcopy(r.table.matrix)
        if (cpy.make_move(i, j, self.turn) != -1):
          if cpy.matrix == self.matrix:
            continue
          succesori.append(cpy)
    return succesori




