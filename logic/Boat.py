class Boat:
    def __init__(self, load: int = 0, capacity: int = 10, sellPrice: int = 2):
        if load > capacity:
            raise ValueError
        self.__load = load
        self.__capacity = capacity
        self.__sellPrice = sellPrice

    def load(self, amount: int) -> bool:
        """
        Adds an amount to the load of this Boat.
        Returns False if the added load would exceed the capacity, True otherwise.
        """

        if amount + self.__load > self.__capacity:
            return False
        else:
            self.__load += amount
            return True
        
    def unload(self, amount: int):
        """
        Subtracts an amount from the load of this Boat.
        If the amount is bigger than the load, the load is set to 0.
        """

        self.__load -= amount
        if self.__load < 0:
            self.__load = 0
        
    def getLoad(self) -> int:
        """Returns the load of this Boat."""

        return self.__load
    
    def getCapacity(self) -> int:
        """Returns the capacity of this Boat."""

        return self.__capacity

    def getSellPrice(self) -> int:
        """Returns the sell price of this Boat."""

        return self.__sellPrice

    def equals(self, other) -> bool:
        """Returns true if and only if other is a Boat and equal to this Boat."""

        if not isinstance(other, Boat):
            return False
        return self.__load == other.__load and self.__capacity == other.__capacity and self.__sellPrice == other.__capacity

    def toString(self) -> str:
        """Returns a human-readable String representation of this Boat"""

        template = "Boat:\n\tCapacity: {0:d}\n\tLoad:{1:d}\n\tSell price: {2:d}"
        return template.format(self.__capacity, self.__load, self.__sellPrice)