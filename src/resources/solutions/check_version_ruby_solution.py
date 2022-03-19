from src.models.solution import Solution
import os

class CheckVersionRubySolution(Solution):
    def execute(self):
        self.run= True
        response_system = os.system('ruby -v')
        if response_system != 0:
            self.error = True
            self.error ='You need ruby installed on machine'
            self.erro_code = response_system
            raise Exception(self.error)
    def __repr__(self) -> str:
        return "Check Version Ruby"
    
    
