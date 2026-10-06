class Produto:
    def __init__(self, descricao: str, preco_unitario: float, estoque: int):
        self.__descricao = descricao
        self.__preco_unitario = preco_unitario
        self.__estoque = estoque

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def preco_unitario(self) -> float:
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario: float):
        if preco_unitario >= 0:
            self.__preco_unitario = preco_unitario

    @property
    def estoque(self) -> int:
        return self.__estoque

    @estoque.setter
    def estoque(self, estoque: int):
        if estoque >= 0:
            self.__estoque = estoque


    def decrementar_estoque(self, quant: int) -> bool:
        if self.__estoque >= quant:
            self.__estoque -= quant
            return True
        else:
            print("Estoque insuficiente!")
            return False