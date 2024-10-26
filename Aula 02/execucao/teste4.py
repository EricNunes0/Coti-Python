from entrada.entrada_produto import InputProduto
from modelo.produto import Produto

if __name__ == '__main__':
    try:
        produto = Produto()
        inputProd = InputProduto()
        produto.name = inputProd.input_name()
        produto.price = inputProd.input_price()
        produto.quantity = inputProd.input_quantity()
        print(produto)
    except Exception as e:
        print(e)
    finally:
        print("Finalizando...")
    pass