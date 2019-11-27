import logic.Game as Game
import logic.Player as Player
import logic.Turn as Turn

class GameController:
    def __init__(self, game = Game.Game()):
        self.__turn = 0
        self.__game = game
        self.__player = game.getPlayers()[0]
        self.__turninfo = None

    def nextPlayer(self):
        """Selects the next player who is at turn."""

        self.__turn += 1
        players = self.__game.getPlayers()
        index = self.__turn % len(players)
        return players[index]

    def startTurn(self, player):
        """Performs actions on the start of the players turn."""

        player.mutateWheat()
        self.__turninfo = Turn.Turn()

    def getTurnInfo(self):
        return self.__turninfo