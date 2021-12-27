"""
A classe carrinho pode existir sozinha, no entanto, ela precisa da classe produtos.
"""
class CarrinhoDeCompras:
    def __init__(self):
        self.products = []

    
    def add_product(self, produto):
        self.products.append(produto)
        
    
    def list_products(self):
        for produto in self.products:
            print(f"{produto.name} - R$ {produto.value}")
            
    
    def soma_total(self):
        total = 0
        for produto in self.products:
            total += produto.value
        return total
        

class Produtos:
    def __init__(self, name, value):
        self.name = name
        self.value = value