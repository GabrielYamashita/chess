
import chess
import chess.pgn

import io
import requests


def getChessBoard(gameID):
   URL = f"https://lichess.org/api/puzzle/{gameID}"
   r = requests.get(URL)
   data = r.json()

   PGN = data['game']['pgn']
   solution = data['puzzle']['solution']

   moves = PGN.split(" ")

   count = 1
   for i in range(len(moves)):
      if i % 2 == 0:
         moves[i] = f'{count}. {moves[i]}'
         count += 1

   PGN = " ".join(moves)

   pgn = io.StringIO(PGN)
   game = chess.pgn.read_game(pgn)

   board = game.board()
   for move in game.mainline_moves():
      board.push(move)

   FEN = board.fen()

   print(f"- Puzzle ID: {gameID}:")
   print(f"Game link: https://lichess.org/pt/training/{gameID}")
   print(f"Data link: {URL}\n")
   print(f"PGN: {PGN}")
   print(f"FEN: {FEN}")

   return board, solution


def makeMove(move, board):
   xxn = chess.Move.from_uci(move)
   board.push(xxn)

   return board


def solvePuzzle(solution, board):
   print(f"\nSolve: {(solution)}")

   for move in solution:
      makeMove(move, board)
      showBoard(board, turn)


def showBoard(board, whoPlays):
   if whoPlays in ['black', 'b', 'preto', 'p', False]:
      orientation = False
   
   elif whoPlays in ['white', 'w', 'branco', 'b', True]:
      orientation = True

   print("\nBoard:") 
   print(board.unicode(invert_color=True, orientation=orientation))

   if board.is_checkmate():
      print("Checkmate!")


gameID = 'A6pKa'

# Get Data and Board
board, solution = getChessBoard(gameID)
turn = board.turn
showBoard(board, turn)

# Solve the Board/Puzzle:
solvePuzzle(solution, board)

