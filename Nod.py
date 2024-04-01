from copy import copy, deepcopy
import numpy as np
import reversi


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

  def succesori(self):
    ''' Calculeaza lista succesorilor directi ai starii curente.

    :return: lista starilor admisibile
    '''
    succesori = []
    if (self.terminal_node()):
      return succesori
    r = reversi.Reversi()
    r.table.matrix = self.matrix
    for i in range(0, 8):
      for j in range(0, 8):
        cpy = reversi.Reversi()
        cpy.table.matrix = deepcopy(r.table.matrix)
        if (cpy.make_move(i, j, self.turn) != -1):
          if cpy.table.matrix == r.table.matrix:
            continue
          succesori.append(Nod(cpy.table.matrix, 1 - self.turn, self))
    return succesori




