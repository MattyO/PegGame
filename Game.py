from Board import Board
import copy

VERBOSE = False	
defaultBoard = Board(15)
GameSolutionsToFindLimit = 3;

winningGames = []

def validMoves(board, fromRow, fromIndex):
	allMoves = _genericMoves(fromRow, fromIndex)
	rValidMoves = []
	for row, index, jumpsOver in allMoves: 
		jumpedOverRow, jumpedOverIndex = jumpsOver 
		if board.isValidBoardPosition(row, index) and board.isSpace(row, index) and board.isPeg(jumpedOverRow, jumpedOverIndex):
			rValidMoves.append( [(fromRow, fromIndex),(row, index), jumpsOver] )
	return rValidMoves

def play(board):
	
	if  len(winningGames) >= GameSolutionsToFindLimit :
		return
	if board.numPegs() == 1: 
		winningGames.append(board.moves)
		if VERBOSE == True:
			print "number of winning games found " + str(len(winningGames))
	else: 
		for row, index in board:
			if board.isPeg(row, index): 
				someValidMoves = validMoves(board, row, index)
				for aValidMove in someValidMoves: 
					newBoard = copy.deepcopy(board)
					newBoard.move(aValidMove)
					play(newBoard)


	
def _genericMoves(row, index):
	#takes the form of endRow, endIndex, jumpover tuples
	return [(row,     index - 2, (row,     index -1 )),
			(row,     index + 2, (row,     index + 1)),
			(row - 2, index,     (row -1,  index    )),
			(row - 2, index - 2, (row -1,  index -1 )),
			(row + 2, index ,    (row + 1, index)   ),
			(row + 2, index + 2, (row + 1, index+1  ))]

