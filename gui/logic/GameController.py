import Game as Game
import Player as Player
import Turn as Turn

class GameController:
    def __init__(self, game = Game.Game()):
        self.__turn = 0
        self.__game = game
        self.__player = game.getPlayers()[0]
        self.__turninfo = None

    def getPlayer(self):
        """Returns the current player."""
        
        return self.__player

    def nextPlayer(self):
        """Selects the next player who is at turn."""

        self.__turn += 1
        players = self.__game.getPlayers()
        index = self.__turn % len(players)
        self.__player = players[index]
        return self.__player

    def startTurn(self, player):
        """Performs actions on the start of the players turn. Uses the current player if None is passed as argument."""

        if player == None:
            player = self.__player

        player.mutateWheat()
        self.__turninfo = Turn.Turn()

    def getTurnInfo(self):
        return self.__turninfo