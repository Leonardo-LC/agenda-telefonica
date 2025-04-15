#importa a classe
from .contato import Contato


class Agenda:
    def __init__(self):
        self.opcoes = {
            'Criar' : self.criar_contato,
            'Listar' : self.listar_contato,
            'Editar' : self.editar_contato,
            'Remover' : self.remover_contato,
            'Sair' : self.sair
        }
        self.condicao = True
        self.contatos = {}
        self.menu()

    def menu(self):
        while self.condicao:
            input('Pressione enter para continuar...')
            print("====== MENU AGENDA ======")
            print("1 - Criar")
            print("2 - Listar")
            print("3 - Editar")
            print("4 - Remover")
            print("5 - Sair")
            print("=========================")
            self.option = input('Digite a ação por extenso: ').title()
            if self.option in self.opcoes:
                self.opcoes[self.option]()
            else:
                print("Opção inválida. Tente novamente.")


    def criar_contato(self):
        nome = input('Digite o nome do contato: ')
        nome = nome.upper()
        if nome not in self.contatos:
            telefone = input('Digite o telefone: ')
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

    def editar_contato(self):
        if self.contatos:
            nome_antigo = input(f'Qual contato deseja alterar? ').upper()
            if nome_antigo in self.contatos:
                novo_nome = input(f'Digite o novo nome: ')
                novo_telefone = input(f'Digite o novo telefone: ')
                self.contatos.pop(nome_antigo)
                self.contatos[novo_nome.upper()] = Contato(novo_nome, novo_telefone)
                print(f'O contato foi alterado com sucesso!')
            else:
                print(f'O contato não está listado na agenda')
        else:
            print('Não foi possível alterar contatos. Sua agenda está vazia. ')

    def  remover_contato(self):
        nome = input(f'Digite o nome do contato: ').upper()
        if nome in self.contatos:
            while True:
                confirmacao = input(f'O contato será excluido PERMANENTEMENTE. Deseja prosseguir? [s/n]: ')
                if confirmacao == 's':
                    del self.contatos[nome]
                    print(f'O contato foi excluido com sucesso!')
                    break
                elif confirmacao == 'n':
                    print(f'O contato não foi excluido')
                    break
                else:
                    print(f"É preciso digiat 's' para confirmar a exclusão ou 'n' para cancelar a exclusão")
        else:
                print('Não foi possível remover, este contato não existe.')
    def sair(self):
        print("Encerrando a agenda...")
        self.condicao = False





    
