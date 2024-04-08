import math
from copy import deepcopy

import reversi
from Nod import Nod


class Bot:

  # the bot_move function will return the best move for the bot, by calling the MiniMax algorithm for every succesor of the current state
  def bot_move(self, table, turn, depth, type ):
    bestMove = None
    current_state = Nod(table.matrix, (0,0), turn)
    if(turn == 0):
      bestScore = -math.inf
      for succesor in current_state.succesori():
        score = self.MiniMax(succesor, depth, -math.inf, math.inf, True, type)
        if score > bestScore:
          bestScore = score
          bestMove = succesor
    else:
      bestScore = math.inf
      for succesor in current_state.succesori():
        score = self.MiniMax(succesor, depth, -math.inf, math.inf, False, type)
        if score < bestScore:
          bestScore = score
          bestMove = succesor
    return bestMove


  # the MiniMax algorithm with alpha-beta pruning for the bot, that will return the best move from moves above a certain depth,
  # for a specific node this algorithm will compare the best (highest or lowest depending on the turn) score from the possible moves (sons) and choose it accordingly
  # for the states that are terminal, the algorithm will return the number of white pieces on the board
  # and for the intermediate states, the algorithm will go by the number or white pieces on the board or keeping track of the occupied corners
  # alpha and beta are the values that will help the algorithm to prune the tree, so it will not explore the entire tree

  def MiniMax(self, nod, depth, alpha, beta, isMaximizing, type):
    if nod.terminal_node():
      return nod.value
    if depth == 0:
      if type == 0:
        return nod.value
      else:
        return nod.value2

    if isMaximizing:
      bestScore = -math.inf
      for node in nod.succesori():
        score = self.MiniMax(node, depth - 1, alpha, beta, False, type)
        bestScore = max(bestScore, score)
        alpha = max(alpha, score)
        if beta <= alpha:
          break
      return bestScore
    else:
      bestScore = math.inf
      for node in nod.succesori():
        score = self.MiniMax(node, depth - 1, alpha, beta, True, type)
        bestScore = min(bestScore, score)
        beta = min(beta, score)
        if beta <= alpha:
          break
      return bestScore
