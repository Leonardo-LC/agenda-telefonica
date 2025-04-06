from packages.agenda import Agenda
from packages.contato import Contato

# Criando a agenda
agenda = Agenda()

# Solicitando entrada do usuário
nome = input('Digite seu nome: ')
telefone = input('Digite seu telefone: ')

# Adicionando o contato na agenda
agenda.criar_contato(nome, telefone)

# Adicionando contatos fixos
agenda.criar_contato('jose', '123')
agenda.criar_contato('napoleao', '456')

# Listando todos os contatos
agenda.listar_contatos()
