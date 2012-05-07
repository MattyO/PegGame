class BoardIterator():
	def __init__(self, indexMap): 
		self._index_map = indexMap
		self.current_possition = 0
	def __iter__(self):
		self.current_possition = 0
		return self
	def next(self):
		if self.current_possition >= len(self._index_map):
			raise StopIteration
		self.current_possition += 1
		return self._index_map[self.current_possition -1]
	
		
class Board():

	def __init__(self, size):
		self.PEG = True
		self.SPACE = False
		self._index_map=[]
		self.moves = []
		self._board = dict()
		
		self._initTriangleBoard(size)
		
	def _initTriangleBoard(self, size):
		currentRow = 0
		currentRowSize = 0
		currentRowMaxSize = 1
		
		for i in  range(0, size):
			if currentRowSize >= currentRowMaxSize:
				currentRowSize = 0
				currentRowMaxSize += 1
				currentRow += 1
			self._addPeg(currentRow, currentRowSize)
			self._index_map.append((currentRow, currentRowSize))
			currentRowSize += 1
		self._board[0][0] = False
		
	def printBoard(self):
		oldRow = 0
		for row, index in self:
			if oldRow != row:
				print
				oldRow = row
			if self.isPeg(row, index):
				print '+',
			else: 
				print '0',
		print
					
	def _addPeg(self, row, index):
		if  not self._board.has_key(row): 
			self._board[row] = dict()
		
		self._board[row][index] = self.PEG
	
	def __iter__(self):
		return BoardIterator(self._index_map)
	
	def move(self, move):
		#break down move into tuples
		fromTuple, toTuple, removeTuple = move

		#break down move tuples
		fromRow, fromIndex = fromTuple
		toRow, toIndex = toTuple
		removeRow, removeIndex = removeTuple
		
		self.moves.append((fromTuple, toTuple))
		
		self._board[fromRow][fromIndex] = self.SPACE 
		self._board[removeRow][removeIndex] = self.SPACE
		self._board[toRow][toIndex] = self.PEG 
		
	def numPegs(self):
		rNumPegs = 0
		for row, index in self: 
			if self.isPeg(row, index): 
				rNumPegs += 1
		return rNumPegs
	
	def isSpace(self, row, index):
		return self.isValidBoardPosition(row, index) and self.getContents(row, index) == self.SPACE
	def isPeg(self, row, index):
		return self.isValidBoardPosition(row, index) and self.getContents(row, index) == self.PEG
	def getContents(self, row, index): 
		return self._board[row][index] 
	def removePeg(self, row, index): 
		self._board[row][index] = False
	def isValidBoardPosition(self, row,index): 
		return self._board.has_key(row) and self._board[row].has_key(index)
	
