from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def boundingRect(self):
        pass

    @abstractmethod
    def distance(self):
        pass

    @abstractmethod
    def export(self):
        pass
