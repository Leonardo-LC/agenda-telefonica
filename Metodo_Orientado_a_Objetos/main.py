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
        agenda.criar_contato()

    elif opcao == '2':
        agenda.listar_contato()

    elif opcao == '3':
        agenda.editar_contato()

    elif opcao == '4':
        agenda.remover_contato()

    elif opcao == '5':
        print("Encerrando a agenda...")
        break

    else:
        print("Opção inválida. Tente novamente.")
    input("Pressione enter para continuar...")