class Boat:
    def __init__(self, load = 0, capacity = 10, sellPrice = 2):
        if load > capacity:
            raise ValueError
        self.__load = load
        self.__capacity = capacity
        self.__sellPrice = sellPrice

    def load(self, amount):
        """
        Adds an amount to the load of this Boat.
        Returns False if the added load would exceed the capacity, True otherwise.
        """

        if amount < 0:
            self.unload(-amount)
            return True
        elif amount + self.__load > self.__capacity:
            return False
        else:
            self.__load += amount
            return True
        
    def unload(self, amount):
        """
        Subtracts an amount from the load of this Boat.
        If the amount is bigger than the load, the load is set to 0.
        """

        if amount < 0:
            self.load(-amount)
            return
        self.__load -= amount
        if self.__load < 0:
            self.__load = 0
        
    def getLoad(self):
        """Returns the load of this Boat."""

        return self.__load
    
    def getCapacity(self):
        """Returns the capacity of this Boat."""

        return self.__capacity

    def getSellPrice(self):
        """Returns the sell price of this Boat."""

        return self.__sellPrice

    def equals(self, other):
        """Returns true if and only if other is a Boat and equal to this Boat."""

        if not isinstance(other, Boat):
            return False
        
        print(self..getLoad() == other.getLoad())
        print(self.__capacity == other.__load)
        print(self.__load == other.__load)
        print(self.__load == other.__load and self.__capacity == other.__capacity and self.__sellPrice == other.__sellPrice)

        return self.__load == other.__load and self.__capacity == other.__capacity and self.__sellPrice == other.__sellPrice

    def toString(self):
        """Returns a human-readable String representation of this Boat"""

        template = "Boat:\n\tCapacity: {0:d}\n\tLoad: {1:d}\n\tSell price: {2:d}"
        return template.format(self.__capacity, self.__load, self.__sellPrice)