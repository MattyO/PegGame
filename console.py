import Game

Game.defaultBoard.print_board()
    
Game.play(Game.defaultBoard)

for winningGame in Game.winningGames:
    print winningGame
