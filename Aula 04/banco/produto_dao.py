from modelo.produto import Produto
from .connect import Connect

class ProdutoDao(Connect):
    def create(self, produto):
        try:
            self.open()
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO produto(nome,preco,quantidade) VALUES (%s, %s, %s)",
                           (produto.nome, produto.preco, produto.quantidade))
            self.conn.commit()
        except Exception as e:
            raise Exception('CreateError, Erro ao criar o objeto' + str(e.args))
        finally:
            self.close()
        pass

    def read(self):
        try:
            self.open()
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM produto ORDER BY nome")
            registros = cursor.fetchall()
            produtos = []
            for registro in registros:
                produto = Produto(registro[0], registro[1], registro[2], registro[3])
                produtos.append(produto)

            return produtos
        except Exception as e:
            raise Exception("ReadError, Erro ao ler os dados" + str(e.args))
        finally:
            self.close()
        pass

    def read_one(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass
    pass