import logic.Player as Player
import logic.Event as Event
import json
import random

class Game:
    EVENT_SOURCE = ""   #The path to the file that contains the event data
    DEFAULT_PLAYERLIST = [Player.Player("Player1"), Player.Player("Player2"), Player.Player("Player3"), Player.Player("Player4")]

    def __init__(self, players = DEFAULT_PLAYERLIST, sourcefile = EVENT_SOURCE):
        self.__players = players
        self.__events = self.__readEvents(sourcefile)
    
    def __readEvents(self, path):
        """Reads in the events from the provided file."""

        events = []

        datafile = open(path, "r")
        jsondata = datafile.read()
        data = json.loads(jsondata)

        for chunk in data:
            events.append(Event.Event(*chunk))

        return events

    def getPlayers(self):
        """Returns the list of players participating in this game."""

        return self.__players

    def randEvent(self):
        return self.__events[random.randrange(0, len(self.__events))]