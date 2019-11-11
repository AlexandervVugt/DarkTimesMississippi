

class Player:
    def __init__(self, name: str, wheat: int = 10, gold: int = 3, boat):
        self.__name = name
        self.__wheat = wheat
        self.__gold = gold
        self.__boat = boat
    
    '''
    Takes a mutation value as input.
    Adds positive mutations, subtracts negative mutations.
    Returns True if the mutation succeeded, False otherwise.
    '''
    def mutateWheat(self, mutation: int = 1) -> bool:
        if mutation < 0 and self.__wheat + mutation < 0:
            return False
        else:
            self.__wheat += mutation
            return True
        
    '''
    Takes a mutation value as input.
    Adds positive mutations, subtracts negative mutations.
    Returns True if the mutation succeeded, False otherwise.
    '''
    def mutateGold(self, mutation: int) -> bool:
        if mutation < 0 and self.__gold + mutation < 0:
            return False
        else:
            self.__gold += mutation
            return True

    '''
    Returns the amount of wheat this Player posesses.
    '''
    def getWheat(self) -> int:
        return self.__wheat

    '''
    Returns the amount of gold this Player posesses.
    '''
    def getGold(self) -> int:
        return self.__gold

    '''
    Returns whether this Player has a Boat or not.
    '''
    def hasBoat(self) -> bool:
        return self.__boat != None

    '''
    Destroys this Player's Boat.
    '''
    def destroyBoat(self):
        self.__boat = None
    
    '''
    Assigns a Boat to this Player.
    '''
    def assignBoat(self, boat) -> bool:
        if self.hasBoat:
            return False
        self.__boat = boat
        return self.__boat == boat

    '''
    Returns the name of this Player.
    '''
    def getName(self) -> str:
        return self.__name

    '''
    Returns a human-readable String representation of this Player.
    '''
    def toString(self) -> str:
        template = "Player: {0:s}\nGold: {1:d}\nWheat: {2:d}\nBoat: {3:s}"
        return template.format(self.__name, self.__gold, self.__wheat, self.__boat)

    '''
    Checks whether the provided Object is a Player and equal to this player.
    '''
    def equals(self, other):
        if not isinstance(other, Player):
            return False
        if other.__name != self.__name or other.__gold != self.__gold or other.__wheat != self.__wheat:
            return False
        return True