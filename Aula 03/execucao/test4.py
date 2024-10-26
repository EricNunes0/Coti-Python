from colored_print import colored_print

if __name__ == '__main__':
    # Dicionários -> Chave, valor
    clients = {
        "COD01": "Eric",
        "COD02": "Gabriel",
        "COD03": "João",
        "COD04": "Nathan",
    }

    colored_print().string(type(clients), "red")

    # Acessar os itens do dicionário
    colored_print().string(clients["COD01"], "yellow")

    # Função do dicionário para acessar
    colored_print().string(clients.get("COD02", "Cliente não encontrado."), "green", underline=False)

    # Adicionar elementos a um dicionário
    clients['COD05'] = "Kauã"
    colored_print().string(clients, "cyan", bold=True)

    # Remover elemento do dicionário
    del clients['COD05']
    colored_print().string(clients, "blue")

    # pop
    colored_print().string(clients.pop('COD04', "Cliente não encontrado."), "green", bold=True, underline=True)
    colored_print().string(clients.pop('COD14', "Cliente não encontrado."), "red", bold=False, underline=False)

    # keys -> Chaves
    colored_print().string(clients.keys(), "yellow")

    # values -> Valores
    colored_print().string(clients.values(), "yellow")

    # Iterar
    colored_print().array_for_each(clients.keys(), "green", bold=True, underline=True)

    # Tupla, lista imutável
    tupla = (10, 30, 50, 70, 90)
    colored_print().string(type(tupla), "red")
    pass