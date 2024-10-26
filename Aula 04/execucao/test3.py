from banco.produto_dao import ProdutoDao
from modelo.produto import Produto

def cadastrar():
    try:
        produto = Produto(nome= "Mouse", quantidade=3, preco=10.3)
        dao = ProdutoDao()
        dao.create(produto)
        print("Produto registrado com sucesso")
    except Exception as e:
        print(e)

def listar():
    try:
        dao = ProdutoDao()
        for produto in dao.read():
            print(produto)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    #cadastrar()
    listar()
    pass