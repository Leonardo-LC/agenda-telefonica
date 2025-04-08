from packages.contato import Contato
from packages.agenda import Agenda

agenda = Agenda()

def menu():
    print("\n====== MENU AGENDA ======")
    print("1 - Criar contato")
    print("2 - Listar contatos")
    print("3 - Editar contato")
    print("4 - Remover contato")
    print("5 - Sair")
    print("=========================")

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone: ')
        agenda.criar_contato(nome, telefone)

    elif opcao == '2':
        agenda.listar_contato()

    elif opcao == '3':
        novo_nome = input('Digite o novo nome: ')
        novo_telefone = input('Digite o novo telefone: ')
        agenda.editar_contato(novo_nome, novo_telefone)

    elif opcao == '4':
        agenda.remover_contato(None)  # passando None porque o nome é solicitado dentro da função

    elif opcao == '5':
        print("Encerrando a agenda...")
        break

    else:
        print("Opção inválida. Tente novamente.")