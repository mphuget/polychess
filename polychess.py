#python-chess import
#https://github.com/niklasf/python-chess
import chess

#set the board to its initial position
#corresponding to: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
board = chess.Board()

#print the board on the console
print(board)

#SVG render for the board is possible in Jupyter Notebook
#board

#get all the legal moves for the current position
moves = board.legal_moves

#how many moves are available?
print(moves.count())

#iterate over all the moves
for move in moves: 
    
    #display the move
    print(move)
    
    #save the current position
    current_board = board
    
    #do the move
    board.push(move)
    
    #display the board
    print(board)
    
    #number of black moves
    print("Black moves:" + str(board.legal_moves.count()))
    
    #undo the move
    board.pop()
    
    #do we have a winner?
    if (board.is_game_over()):
        print("The game is over")
        print(board.result())
    
