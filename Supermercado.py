import sys


class Supermercado:
    produtos = []

    def _init_(self, produto, preco, marca, entrega):
        self.produto = produto
        self.preco = preco
        self.entrega = entrega
        self.marca = marca

    def EntregarProduot(self):
        if self.entrega == True:
            print("Produto Entregue...")

    def CadastrarProduto():

        produto = input("Qual é o nome do Produto?")

        preco = float(input("Qual o preço do Produto?"))

        marca = input("Qual é a marca do produto?")

        temp = Supermercado(produto, preco, marca)

        produtos.append(temp)

        if input("Casdastrar mais Produtos? S/N") == "S":
            break

    # falta terminar esse#

    def ListarProdutos(produtos):
        i = 0
        for i in len(produtos):
            print("e")
            # print("Nome: " + produtos[i].)produtos[i]
