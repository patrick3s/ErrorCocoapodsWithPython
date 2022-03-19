import os
from resources.solutions.add_in_your_path import AddInYourPathSolution
from resources.solutions.ruby_global_solution import RubyGlobalSolution
from resources.solutions.try_install_cocoapods import TryInstallCocoapods
from src.models.problem import Problem
from src.resources.solutions.check_version_ruby_solution import CheckVersionRubySolution
from src.resources.solutions.for_compilers_to_find_ruby_solution import ForCompilersToFindRubySolution
class Cocoapods(Problem):
    def gerate_solution(self):
        error = ''
        try:
            self.get_dependencies()
            self.execute()
        except Exception as e:
            error = 'Error: '+ str(e)
        self.logs()
        print(error)
    
    def get_dependencies(self):
        self.solutions.append(CheckVersionRubySolution())
        self.solutions.append(AddInYourPathSolution())
        self.solutions.append(ForCompilersToFindRubySolution())
        self.solutions.append(RubyGlobalSolution())
        self.solutions.append(TryInstallCocoapods())

    def execute(self):
        for solution in self.solutions:
            self.logs()
            solution.execute()
            print(f'{str(solution)} Executing...')

    def logs(self):
        os.system('clear')
        print('Steps of Problem')
        for position in range(len(self.solutions)):
            solution = self.solutions[position]
            status = 'pending..' if not solution.run else 'Ok' if not solution.error else 'Erro'
            print(f'{position+1}º Step: \n {str(solution)} : {status} ')

     