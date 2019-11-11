from Player import Player
import json

class Game:
    EVENT_SOURCE = ""   #The path to the file that contains the event data
    DEFAULT_PLAYERLIST = [Player("Player1"), Player("Player2"), Player("Player3"), Player("Player4")]

    def __init__(self, players: list = DEFAULT_PLAYERLIST, events: list = __readEvents(EVENT_SOURCE)):
        self.__players = players
        self.__events = events
    
    def __readEvents(self, path: str) -> list:
        """Reads in the events from the provided file."""

        datafile = open(path, "r")
        jsondata = datafile.read()
        events = json.loads(jsondata)
        return events

    def getPlayers(self) -> list:
        """Returns the list of players participating in this game."""

        return self.__players