#python-chess import
#https://github.com/niklasf/python-chess
import chess

from random import randint

#set the board to its initial position
#corresponding to: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
board = chess.Board()

#print the board on the console
print(board)

#side to play
#0 for White to play
#1 for Blxk to play
side = 0

#iterate on all the moves and play until the game is over
while not board.is_game_over():

    if side == 0:
        print("White to play")
        
        #change the side to move for next move
        side = 1
    else:
        print("Black to play")
        
        #change the side to move for next move
        side = 0
        
    #get all the possible moves
    moves = board.legal_moves
    
    #get a move randomly
    move = list(moves)[randint(0, len(list(moves))-1)]

    #play the move
    board.push(move)
    
    #display the board
    print(board)
    
#the game is over
print("Game over")

