from modelo.cliente import Cliente
from entrada.entrada_cliente import EntradaCliente

if __name__ == '__main__':
    cliente = Cliente()
    entCliente = EntradaCliente()

    cliente.name = entCliente.entrada_name()
    cliente.email = entCliente.entrada_email()
    print(cliente)
    pass