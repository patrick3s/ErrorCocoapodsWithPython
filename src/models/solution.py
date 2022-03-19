from abc import ABC, abstractmethod


class Solution(ABC):
    run = False
    error = False
    error_msg = ''
    erro_code = None
    @abstractmethod 
    def __repr__(self) -> str:
        pass
    @abstractmethod
    def execute(self):
        pass
  