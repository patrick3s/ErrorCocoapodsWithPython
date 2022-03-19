from src.models.solution import Solution
import os

class RubyGlobalSolution(Solution):
    def execute(self):
        self.run= True
        command = """
       echo 'export PATH="/usr/local/opt/ruby/bin:$PATH"' >> /Users/user_name/.bash_profile &&
        echo 'export LDFLAGS="-L/usr/local/opt/ruby/lib"' >> ~/.bash_profile &&
        echo 'export CPPFLAGS="-I/usr/local/opt/ruby/include"' >> ~/.bash_profile &&
        source ~/.bash_profile
        """
        response_system = os.system(command)
        if response_system != 0:
            self.error = True
            self.error ='Sorry have an error in {self}'
            self.erro_code = response_system
            raise Exception(self.error)
    def __repr__(self) -> str:
        return "Ruby Global Solution"