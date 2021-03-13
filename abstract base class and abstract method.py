from abc import abstractmethod , ABC
class shape(ABC):
    @abstractmethod
    def printdetails(self):
        return 0
class rectangle(shape):
    def __init__(self,length , breadth):
        self.length =length
        self.breadth = breadth
    def printdetails(self):
        return self.length * self.breadth


r1 = rectangle(12,12)
print(r1.printdetails())
