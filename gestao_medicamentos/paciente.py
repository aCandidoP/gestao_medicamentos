from plano import *
from pessoa import *

class Paciente(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.plano = escolha_plano()
    
    def __str__(self):
        return self.nome + ' ' + self.plano



      
    


      
    

    