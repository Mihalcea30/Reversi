import math
from copy import deepcopy

import reversi
from Nod import Nod


class Bot:

  def bot_move(self, table, turn, depth = 4):
    bestMove = None
    current_state = Nod(table.matrix, (0,0), turn)
    if(turn == 0):
      bestScore = -math.inf
      for succesor in current_state.succesori():
        score = self.MiniMax(succesor, depth, -math.inf, math.inf, True)
        if score > bestScore:
          bestScore = score
          bestMove = succesor
    else:
      bestScore = math.inf
      for succesor in current_state.succesori():
        score = self.MiniMax(succesor, depth, -math.inf, math.inf, False)
        if score < bestScore:
          bestScore = score
          bestMove = succesor
    return bestMove
  def MiniMax(self, nod, depth, alpha, beta, isMaximizing):
    if depth == 0 or nod.terminal_node():
      return nod.value

    if isMaximizing:
      bestScore = -math.inf
      for node in nod.succesori():
        score = self.MiniMax(node, depth - 1, alpha, beta, False)
        bestScore = max(bestScore, score)
        alpha = max(alpha, score)
        if beta <= alpha:
          break
      return bestScore
    else:
      bestScore = math.inf
      for node in nod.succesori():
        score = self.MiniMax(node, depth - 1, alpha, beta, True)
        bestScore = min(bestScore, score)
        beta = min(beta, score)
        if beta <= alpha:
          break
      return bestScore
