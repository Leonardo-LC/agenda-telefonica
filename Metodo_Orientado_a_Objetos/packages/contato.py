class Contato: #Cria um contato
    def __init__(self, nome, contato):
        self.nome = nome
        self.contato = contato
    def __str__(self): #Faz com que a informação exibida seja legível ao dar print em um objeto desta classe
        return f'Nome: {self.nome.title()}, Número: {self.contato}'
