class InputProduto:
    def input_name(self):
        name = input("Informe o nome do produto: ")
        return name
        pass

    def input_price(self):
        try:
            price = float(input("Informe o preço do produto: "))
            if price < 0:
                raise Exception('PriceValueError, O preço não pode ser negativo.')
            return price
        except ValueError as e:
            print("Não foi possível converter a string em decimal.")
            return self.input_price()
        except Exception as e:
            print(e.args)
            print(e.__class__)
            print("Erro ao tentar resgatar o preço.")
            return self.input_price()
        pass

    def input_quantity(self):
        price = int(input("Informe a quantidade do produto: "))
        return price
        pass
    pass