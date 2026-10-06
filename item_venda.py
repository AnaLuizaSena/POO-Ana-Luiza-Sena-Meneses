from produto import Produto

class ItemVenda:
    def __init__(self, produto: Produto, quantidade: int):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__valor_item = produto.preco_unitario


    @property
    def produto(self) -> Produto:
        return self.__produto

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        if quantidade > 0:
            self.__quantidade = quantidade

    @property
    def valor_item(self) -> float:
        return self.__valor_item

    @valor_item.setter
    def valor_item(self, valor_item: float):
        if valor_item >= 0:
            self.__valor_item = valor_item


    def calcular_subtotal(self) -> float:
        return self.__quantidade * self.__valor_item