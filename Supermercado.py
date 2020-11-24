import sys
from Cliente import Cliente
from Funcionario import Funcionario
from Produto import Produto

cliente1 = Cliente('Renato', '45478759612', 'av a 123')
cliente2 = Cliente('Vitor', '85212345678', 'rua 9 41a')
cliente3 = Cliente('Ramir', '78945612300', 'rua dez 10')

funcionario = Funcionario('Renato', '119122036', 'Aluno')


produto1 = Produto('Arroz 1kg', 'Grão', 'Prato Fino', '5.89')
produto2 = Produto('Feijão 1kg', 'Grão', 'Camil', '7.99')
produto3 = Produto('Macarrão Espaguete', 'Massa', 'Vilma', '3.75')
produto4 = Produto('Milho 1kg', 'Conservante', 'Quero', '5.89')
produto5 = Produto('Feijão 1kg', 'Grão', 'Camil', '7.99')
produto6 = Produto('Macarrão Espaguete', 'Massa', 'Vilma', '3.75')
produto7 = Produto('Arroz 1kg', 'Grão', 'Prato Fino', '5.89')
produto8 = Produto('Feijão 1kg', 'Grão', 'Camil', '7.99')
produto9 = Produto('Macarrão Espaguete', 'Massa', 'Vilma', '3.75')


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
        frase = "codigo:" + str(aux) + " -> " + \
            prdt.nome + " por " + prdt.preco
        print(frase)
        aux = aux + 1

    Log("Listagem de Produtos")
    return listProdutos


def Comprar():

    comprados = SelecinarProdutos()

    Pagamento(comprados)

    Log("Compra finalizada")
    print("A compra foi finalizada")


def SelecinarProdutos():
    produtosC = []
    listProdutos = ListarProdutos()
    while True:
        produto = int(input("Digite o codigo do produto "))

        if produto < len(listProdutos):
            produtosC.append(listProdutos[produto])

            frase = "Produto " + listProdutos[produto].nome + " adicionado"
            Log(frase)
        else:
            print("Produto invalido")
            Log("Produto invalido")

        aux = input("Deseja comprar mais produtos? Y/N ")

        if aux == "N" or aux == "n":
            break
            Log("Finalizada Escolha dos produtos")

    return produtosC


def Pagamento(produtos):
    aux = 0
    valores = 0
    for prod in produtos:
        valores = valores + float(prod.preco)

    frase = "O valor total da compra é de: " + str(valores)
    Log(frase)
    print(frase)

    FPag = input(
        "Qual a forma de pagamento? D para Dinheiro ou C para Cartão ")
    while True:
        if FPag == "D" or FPag == "C" or FPag == "c" or FPag == "d":
            Log("A escolha da forma de pagamento foi definida como: " + FPag)
            break

        else:
            FPag = input(
                "Qual a forma de pagamento? D para Dinheiro ou C para Cartão ")
            Log("Valor inserido invalido na forma de pagamento")

    if FPag == "D" or FPag == "d":
        valor = float(input("Qual o valor recebido? "))

        Log("Valor recebido em dinheiro:" + str(valor))

        troco = valor - valores
        frase = "O troco é de: " + str(troco)
        print(frase)
        Log(frase)

    elif FPag == "C" or FPag == "c":
        print("Produto Pago...")


def Log(texto):

    archive = open('Log.txt', 'r')
    conteudo = archive.readlines()
    conteudo.append(texto + '\n')

    archive = open('Log.txt', 'w')
    archive.writelines(conteudo)

    archive.close()


Comprar()
