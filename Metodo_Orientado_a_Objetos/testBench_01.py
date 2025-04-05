from packages.agenda import Agenda
from packages.contato import Contato

agenda = Agenda()
nome = input('Digite seu nome: ')
telefone = input('Digite sua telefone: ')
contato = Contato(nome, telefone)

print(contato)
