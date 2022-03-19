from src.models.solution import Solution
import os
class TryInstallCocoapods(Solution):
    def execute(self):
        self.run= True
        command = """
       sudo gem install -n /usr/local/bin cocoapods
        """
        response_system = os.system(command)
        if response_system != 0:
            self.error = True
            self.error ='Sorry have an error in {self}'
            self.erro_code = response_system
            raise Exception(self.error)
    def __repr__(self) -> str:
        return "Try Install Cocoapods Solution"