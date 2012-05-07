import Game

Game.defaultBoard.printBoard()
    
Game.play(Game.defaultBoard)

for winningGame in Game.winningGames:
    print winningGame
