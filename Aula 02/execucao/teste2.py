from modelo.cliente import *

if __name__ == '__main__':
    cf = ClienteFisico("Eric", "eric@gmail.com", "12345678901", "M")
    print(cf)

    cj = ClienteJuridico()
    cj.name = "McDonalds"
    cj.email = "mc@donalds.com"
    cj.cnpj = "123-456/0001-78"
    cj.ramo = "Alimentação"

    print(cj.name)
    print(cj.email)
    print(cj.cnpj)
    print(cj.ramo)
    pass