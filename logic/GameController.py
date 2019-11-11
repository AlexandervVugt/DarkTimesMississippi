from Game import Game
from Player import Player

class GameController:
    def __init__(self, game: Game = Game()):
        global turn
        turn = 0
        self.__game = game

    def nextPlayer(self) -> Player:
        """Selects the next player who is at turn."""

        global turn
        turn += 1
        players = self.__game.getPlayers
        index = turn % len(players)
        return players[index]