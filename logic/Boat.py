class Boat:
    def __init__(self, load: int = 0, capacity: int = 10, sellPrice: int = 2):
        if load > capacity:
            raise ValueError
        self.__load = load
        self.__capacity = capacity
        self.__sellPrice = sellPrice

    def load(self, amount: int) -> bool:
        if amount + self.__load > self.__capacity:
            return False
        else:
            self.__load += amount
            return True
        
    def unload(self, amount: int):
        self.__load -= amount
        if self.__load < 0:
            self.__load = 0
        
    def getLoad(self) -> int:
        return self.__load
    
    def getCapacity(self) -> int:
        return self.__capacity

    def getSellPrice(self) -> int:
        return self.__sellPrice

    def equals(self, other) -> bool:
        if not isinstance(other, Boat):
            return False
        return self.__load == other.__load and self.__capacity == other.__capacity and self.__sellPrice == other.__capacity

    def toString(self) -> str:
        template = "Boat:\nCapacity: {0:d}\nLoad:{1:d}\nSell price: {2:d}"
        return template.format(self.__capacity, self.__load, self.__sellPrice)