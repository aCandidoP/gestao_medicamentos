class Pessoa():

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome
    
    @property
    def nome(self):
        return self.nome
    
    def __str__(self):
        return self.nome