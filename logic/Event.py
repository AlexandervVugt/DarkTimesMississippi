class Event:
    def __init__(self, name: str, target, effect, description: str):
        self.__name = name
        self.__target = target
        self.__effect = effect
        self.__description = description

    def toString(self) -> str:
        """Returns a human-readable String representation of this Event."""

        return self.__description

    def objectify(self, chunk: list) -> self:
        """Takes a chunk of data and returns an Event Object related to the data."""

        return self.__init__(chunk.name, chunk.target, chunk.effect, chunk.description)

    def equals(self, other: Event) -> bool:
        """Takes another Object and returns True iff other is an Event and equal to this Event."""

        if not isinstance(other, Event):
            return False
        return self.__name == other.__name and self.__description == other.__description