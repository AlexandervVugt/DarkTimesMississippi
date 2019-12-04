class Turn:
    def __init__(self):
        self.__steps = -1

    def getSteps(self):
        return self.__steps

    def setSteps(self, amount):
        self.__steps = amount