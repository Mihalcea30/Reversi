import math
from copy import deepcopy

import reversi
from Nod import Nod


class Bot:

  def bot_move(self, table, turn, depth = 3):
    bestScore = -math.inf
    bestMove = None
    current_state = Nod(table.matrix, turn)
    if(turn == 0):
      for succesor in current_state.succesori():
        score = self.MiniMax(succesor, depth, True)
        if score > bestScore:
          bestScore = score
          bestMove = succesor
    else:
      for succesor in current_state.succesori():
        score = self.MiniMax(succesor, depth, False)
        if score < bestScore:
          bestScore = score
          bestMove = succesor
    return bestMove
  def MiniMax(self, nod, depth, isMaximizing):
    if depth == 0 or nod.terminal_node():
      return nod.value

    if isMaximizing:
      bestScore = -math.inf
      for node in nod.succesori():
        score = self.MiniMax(node, depth - 1, False)
        bestScore = max(bestScore, score)
      return bestScore
    else:
      bestScore = math.inf
      for node in nod.succesori():
        score = self.MiniMax(node, depth - 1, True)
        bestScore = min(bestScore, score)
      return bestScore
