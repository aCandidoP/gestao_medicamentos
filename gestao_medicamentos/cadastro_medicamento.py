class Medicamento():
    def __init__(self, nome, concentracao, volume):
        self.nome = nome
        self.concentracao = concentracao
        self.volume = volume

    @property
    def nome(self):
        return self.nome
        
    @property
    def concentracao(self):
        return self.concentracao
    
    @property
    def volume(self):
        return self.volume
    
    def __str__(self):
        return self.nome + ' ' + self.volume + ' ' + self.concentracao
    
    