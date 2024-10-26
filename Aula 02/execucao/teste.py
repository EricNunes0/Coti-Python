from modelo.cliente import Cliente

if __name__ == '__main__':
    cliente = Cliente()

    cliente.name = "Eric"
    cliente.email = "email@yahoo.com"

    print(cliente.name)
    print(cliente.email)

    cliente2 = Cliente("Gabriel", "email@gmail.com")

    print(cliente2)
    pass