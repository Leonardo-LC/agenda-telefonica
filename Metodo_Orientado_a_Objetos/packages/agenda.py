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

    def listar_contato(self):
        if self.contatos:
            print("Os contatos salvos são:")
            for contato in self.contatos.values():
                print(contato)
        else:
            print("Sua agenda não possui contatos salvos")

    def  remover_contato(self):
        del_contato = input(f'Digite o nome do contato que gostaria de remover: ').upper()
        if del_contato in self.contatos:
            while True:
                confirmacao = input(f'O contato será excluido PERMANENTEMENTE. Deseja prosseguir? [s/n]: ')
                if confirmacao == 's':
                    del self.contatos[del_contato]
                    print(f'O contato foi excluido com sucesso!')
                    break
                elif confirmacao == 'n':
                    print(f'O contato não foi excluido')
                    break
                else:
                    print(f"É preciso digitar 's' para confirmar a exclusão ou 'n' para cancelar a exclusão")

    def editar_contato(self):
        editar_contato = input(f'Qual contato deseja alterar? ').upper()
        if editar_contato in self.contatos:
            novo_nome = input(f'Digite o novo nome: ')
            novo_telefone = input(f'Digite o novo telefone: ')
            self.contatos.pop(editar_contato)
            self.contatos[novo_nome.upper()] = Contato(novo_nome, novo_telefone)
            print(f'O contato foi alterado com sucesso!')
        else:
            print(f'O contato não está listado na agenda')










    
