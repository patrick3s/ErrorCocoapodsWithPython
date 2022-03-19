from abc import ABC,abstractmethod

class Problem(ABC):
    solutions=[]
    def __init__(self) -> None:
        self.gerate_solution()
        self.solutions=[]
    @abstractmethod
    def gerate_solution(self):
        pass