"""
Agregação
- Uma classe usa outra classe como parte de si, e precisa da mesma para se completar
"""
from classes import CarrinhoDeCompras, Produtos

carrinho = CarrinhoDeCompras()

p1 = Produtos('Camiseta', 50)
p2 = Produtos('Bermuda', 60)
p3 = Produtos('Jaqueta Jeans', 75.90)
p4 = Produtos('Cropped', 25)
p5 = Produtos('Conjunto', 50)

carrinho.add_product(p1)
carrinho.add_product(p2)
carrinho.add_product(p3)
carrinho.add_product(p4)
carrinho.add_product(p5)

carrinho.list_products()

print(f"Valor Total da Compra - R$ {carrinho.soma_total()}")