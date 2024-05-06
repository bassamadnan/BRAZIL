from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Parent (virtual?) class, methods to be implemented on inherited shapes. We assume 
    a line as a shape, even though it is technically wrong, it helps for code uniformity.
    """
    @abstractmethod
    def boundingRect(self):
        pass

    @abstractmethod
    def distance(self):
        pass

    @abstractmethod
    def export(self):
        pass
