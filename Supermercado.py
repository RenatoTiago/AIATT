import sys
from Cliente import Cliente
from Funcionario import Funcionario
from Produto import Produto

cliente1 = Cliente('Renato', '45478759612', 'av a 123')
cliente2 = Cliente('Vitor', '85212345678', 'rua 9 41a')
cliente3 = Cliente('Ramir', '78945612300', 'rua dez 10')

print(cliente1.nome)


class Supermercado:

    def _init_(self, Cliente, Funcionario, Produto):
        self.Cliente = Cliente
        self.Funcionario = Funcionario
        self.Produto = Produto
