from src.models.solution import Solution
import os

class ForCompilersToFindRubySolution(Solution):
    def execute(self):
        self.run= True
        command = """
       export LDFLAGS="-L/usr/local/opt/ruby/lib" &&
        export CPPFLAGS="-I/usr/local/opt/ruby/include"
        """
        response_system = os.system(command)
        if response_system != 0:
            self.error = True
            self.error ='Sorry have an error in {self}'
            self.erro_code = response_system
            raise Exception(self.error)
    def __repr__(self) -> str:
        return "For Compilers To Find Ruby Solution"