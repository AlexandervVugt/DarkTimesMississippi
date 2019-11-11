class Event:
    def __init__(self, name: str, target, effect, description: str):
        self.__name = name
        self.__target = target
        self.__effect = effect
        self.__description = description

    def toString(self) -> str:
        """Returns a human-readable String representation of this Event."""

        return self.__description