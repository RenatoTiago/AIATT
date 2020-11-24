import sys
from Cliente import Cliente
from Funcionario import Funcionario
from Produto import Produto

cliente1 = Cliente('Renato', '45478759612', 'av a 123')
cliente2 = Cliente('Vitor', '85212345678', 'rua 9 41a')
cliente3 = Cliente('Ramir', '78945612300', 'rua dez 10')

funcionario = Funcionario('Renato', '119122036', 'Aluno')


produto1 = Produto('Arroz 1kg', 'Grão', 'Prato Fino', '5,89')
produto2 = Produto('Feijão 1kg', 'Grão', 'Camil', '7,99')
produto3 = Produto('Macarrão Espaguete', 'Massa', 'Vilma', '3,75')
produto4 = Produto('Milho 1kg', 'Conservante', 'Quero', '5,89')
produto5 = Produto('Feijão 1kg', 'Grão', 'Camil', '7,99')
produto6 = Produto('Macarrão Espaguete', 'Massa', 'Vilma', '3,75')
produto7 = Produto('Arroz 1kg', 'Grão', 'Prato Fino', '5,89')
produto8 = Produto('Feijão 1kg', 'Grão', 'Camil', '7,99')
produto9 = Produto('Macarrão Espaguete', 'Massa', 'Vilma', '3,75')


def ListarProdutos():
    listProdutos = []
    aux = 0
    listProdutos.append(produto1)
    listProdutos.append(produto2)
    listProdutos.append(produto3)
    listProdutos.append(produto4)
    listProdutos.append(produto5)
    listProdutos.append(produto6)
    listProdutos.append(produto7)
    listProdutos.append(produto8)
    listProdutos.append(produto9)

    for prdt in listProdutos:
        frase = prdt.nome + " por " + prdt.preco
        print(frase)

    Log("Listagem de Produtos")
    return listProdutos


def Comprar():

    listProdutos = ListarProdutos()


def Pagamento(valor):
    FPag = input("Qual a forma de pagamento? D para Dinheiro ou C para Cartão")
    while True:
        if FPag == "D" or FPag == "C" or FPag == "c" or FPag == "d":
            break
        else:
            FPag = input(
                "Qual a forma de pagamento? D para Dinheiro ou C para Cartão")

    if FPag == "D" or FPag == "d":
        valor = float(input("Qual o valor recebido?"))


def Log(texto):
    archive = open('Log.txt', 'w')
    archive.write(texto)
    archive.close()


ListarProdutos()
