import logic.Boat as Boat

class Player:
    def __init__(self, name, wheat = 10, gold = 3, boat = None):
        self.__name = name
        self.__wheat = wheat
        self.__gold = gold
        self.__boat = boat if boat != None else Boat.Boat()
        # boat.getLoad()
    
    def mutateWheat(self, mutation = 1):
        """
        Takes a mutation value as input.
        Adds positive mutations, subtracts negative mutations.
        Returns True if the mutation succeeded, False otherwise.
        """

        if mutation < 0 and self.__wheat + mutation < 0:
            return False
        else:
            self.__wheat += mutation
            return True
        
    def mutateGold(self, mutation):
        """
        Takes a mutation value as input.
        Adds positive mutations, subtracts negative mutations.
        Returns True if the mutation succeeded, False otherwise.
        """

        if mutation < 0 and self.__gold + mutation < 0:
            return False
        else:
            self.__gold += mutation
            return True

    
    def getWheat(self):
        """Returns the amount of wheat this Player posesses."""

        return self.__wheat

    
    def getGold(self):
        """Returns the amount of gold this Player posesses."""

        return self.__gold

    
    def hasBoat(self):
        """Returns whether this Player has a Boat or not."""

        return self.__boat != None

    def destroyBoat(self):
        """Destroys this Player's Boat."""

        self.__boat = None
    
    def assignBoat(self, boat = Boat.Boat()):
        """Assigns a Boat to this Player."""

        print("creating boat")

        if self.hasBoat():
            return False
        self.__boat = boat
        print(self.__boat.toString())
        return self.__boat == boat

    def getBoat(self):
        return self.__boat

    def getName(self):
        """Returns the name of this Player."""

        return self.__name

    def sellBoat(self):
        """Sells this players Boat and transfers money into bank account"""

        self.__gold += self.__boat.sell()
        self.destroyBoat()
    
    def toString(self):
        """Returns a human-readable String representation of this Player."""

        template = "Player: {0:s}\n\tGold: {1:d}\n\tWheat: {2:d}\n\t{3:s}"
        return template.format(self.__name, self.__gold, self.__wheat, self.__boat.toString() if self.hasBoat() else "No boat")

    
    def equals(self, other):
        """Checks whether the provided Object is a Player and equal to this player."""

        if not isinstance(other, Player):
            return False
        if other.__name != self.__name or other.__gold != self.__gold or other.__wheat != self.__wheat \
                    or not self.__boat.equals(other.__boat):
            return False
        return True