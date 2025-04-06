from Metodo_Orientado_a_Objetos.packages.contato import Contato


class Agenda:
    def __init__(self):
        self.contatos = {}

    def criar_contato(self,nome,telefone):
        nome = nome.upper()
        if nome not in self.contatos:
            self.contatos[nome] = Contato(nome,telefone)
            print(f'Contato criado com sucesso!')
        else:
            print("O contato já existe")

    def listar_contatos(self):
        if self.contatos:
            print("Os contatos salvos são:")
            for contato in self.contatos.values():
                print(contato)
        else:
            print("Sua agenda não possui contatos salvos")



    
