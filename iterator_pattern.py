from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def isDone(self):
        pass

    @abstractmethod
    def currentItem(self):
        pass


class Rottweiler:
    def __init__(self):
        self._dogs = ["Dog 1", "Dog 2", "Dog 3", "Dog 4", "Dog 5"]
        self._current = 0

    def getIterator(self):
        return RottweilerIterator(self)


class Doberman:
    def __init__(self):
        self._dogs = ["Dog A", "Dog B", "Dog C"]
        self._current = 0

    def getIterator(self):
        return DobermanIterator(self)


class RottweilerIterator(Iterator):
    def __init__(self, rottweiler):
        self._rottweiler = rottweiler

    def first(self):
        self._rottweiler._current = 0

    def next(self):
        self._rottweiler._current += 1

    def isDone(self):
        return self._rottweiler._current >= len(self._rottweiler._dogs)

    def currentItem(self):
        if self.isDone():
            return None
        return self._rottweiler._dogs[self._rottweiler._current]


class DobermanIterator(Iterator):
    def __init__(self, doberman):
        self._doberman = doberman

    def first(self):
        self._doberman._current = 0

    def next(self):
        self._doberman._current += 1

    def isDone(self):
        return self._doberman._current >= len(self._doberman._dogs)

    def currentItem(self):
        if self.isDone():
            return None
        return self._doberman._dogs[self._doberman._current]


# Usage example
rottweiler = Rottweiler()
rottweilerIterator = rottweiler.getIterator()

print("Rottweiler Dogs:")
rottweilerIterator.first()
while not rottweilerIterator.isDone():
    print(rottweilerIterator.currentItem())
    rottweilerIterator.next()

print()

doberman = Doberman()
dobermanIterator = doberman.getIterator()

print("Doberman Dogs:")
dobermanIterator.first()
while not dobermanIterator.isDone():
    print(dobermanIterator.currentItem())
    dobermanIterator.next()
