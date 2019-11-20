from . import Game
from . import Player

class GameController:
    def __init__(self, game: Game = Game()):
        global turn
        turn = 0
        self.__game = game
        self.__player = game.getPlayers()[0]

    def nextPlayer(self):
        """Selects the next player who is at turn."""

        global turn
        turn += 1
        players = self.__game.getPlayers()
        index = turn % len(players)
        return players[index]