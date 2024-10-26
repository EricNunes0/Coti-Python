from modelo.cliente import *

if __name__ == '__main__':
    cliente = None
    cliente = ClienteFisico()
    print(cliente.calculate_discount())

    cliente = ClienteJuridico()
    print(cliente.calculate_discount())
    pass