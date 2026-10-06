from datetime import datetime
from produto import Produto
from item_venda import ItemVenda

class Venda:
    def __init__(self):
        self.__data = datetime.now()
        self.__itens = []  
        self.__valor_total = 0.0


    @property
    def data(self) -> datetime:
        return self.__data

    @data.setter
    def data(self, data: datetime):
        self.__data = data

    @property
    def valor_total(self) -> float:
        return self.__valor_total

    @property
    def itens(self) -> list:
        return self.__itens


    def adicionar_item(self, produto: Produto, quant: int):
        if produto.decrementar_estoque(quant):
            novo_item = ItemVenda(produto, quant)
            self.__itens.append(novo_item)
            self.calcular_total()
            print(f"Adicionado {quant}x '{produto.descricao}' à venda.")

    def remover_item(self, produto: Produto):
        for item in self.__itens:
            if item.produto == produto:
                produto.estoque = produto.estoque + item.quantidade
                self.__itens.remove(item)
                self.calcular_total()
                print(f"Removido '{produto.descricao}' da venda.")
                return
        print("Item não encontrado na venda.")

    def calcular_total(self) -> float:
        total = 0.0
        for item in self.__itens:
            total += item.calcular_subtotal()
        self.__valor_total = total
        return self.__valor_total