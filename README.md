# PolyChess

PolyChess (named polychess as Git repository) is a Chess engine written in Python and used as practicals for a course on project management at the engineering school Polytech Annecy-Chambéry. 

The aim of this repository is not to provide any complete Chess engine since students have to do it based on python-chess. As a consequence, persons interested in this project should check the different forks.

The required features for PolyChess are: 

* PolyChess is able to play against a user, or to play against itself (through UCI and Winboard on Windows, or Arena on Mac)
* The games played are stored in PGN format in a directory games, the PGN headers have to be filled
* PolyChess can render the board either in text (on the console) or in SVG (thanks to python-chess, in Jupyter Notebooks)
* PolyChess has an opening book (first as a Polyglot book, then using your own format)
* PolyChess is able to play on Lichess (and eventually FICS)
* PolyChess is modular, it is then easy to isolate a feature and to modify it
* PolyChess has an AI (easy to modify) that could play for the engine
* It is possible to enter a FEN position and obtain an evaluation from PolyChess

## Milestones for the project

Chapter 01 : the program plays randomly all the moves till game over, obviously the program finishes when
there is a draw due to insufficient material on the board
