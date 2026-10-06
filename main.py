from produto import Produto
from venda import Venda

p1 = Produto("Caderno", 15.50, 10)
p2 = Produto("Caneta", 2.50, 50)

print(f"Estoque inicial do {p1.descricao}: {p1.estoque}")

minha_venda = Venda()

minha_venda.adicionar_item(p1, 2)  
minha_venda.adicionar_item(p2, 5)  

print(f"Valor total da venda: R$ {minha_venda.valor_total:.2f}")
print(f"Estoque restante do {p1.descricao}: {p1.estoque}")

p1.preco_unitario = 18.00
print(f"Novo preço do {p1.descricao}: R$ {p1.preco_unitario:.2f}")