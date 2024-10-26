if __name__ == '__main__':
    # Listas => Coleções usadas para agrupar variáveis.
    # -5, -4, -3, -2, -1
    #  0,  1,  2,  3,  4
    list = [1, 2, 3, 4, 5]
    list2 = ["Maria", 20.5, 10, True]
    print(list)
    print(list2)

    # Posições
    print(list[0])
    print(list[len(list) - 1])

    # Indexação inversa
    print(list[-1])
    print(list[len(list) * -1])

    # Funções de lista
    # len -> Retorna o tamanho de uma lista
    print(len(list))

    # Varrer uma lista -> iterar pelos objetos da lista
    # Índice da posição inicial
    x = 0

    # 0, 1, 2, 3, 4
    while x < len(list):
        print(list[x])
        x += 1

    # FOR EACH
    for number in list:
        print(number)

    # Funções
    # enumerat -> Retorna uma tupla com o índice, valor da lista.
    for i, value in enumerate(list):
        print("Índice %d\nValor %d" % (i, value))

    # Listas
    # Lista vazia
    list3 = []

    # Adicionar elementos
    list3.append(10)
    list3.append(20)
    list3.append(30)
    list3.append(40)
    list3.append(50)
    print(list3)

    # Remover elementos da lista
    del list3[0]
    print(list3)

    # Remover a lista da memória
    #del list3
    #print(bcolors.OKBLUE + f'{list3}' + bcolors.ENDC)

    # Fatias
    # Índice do início e o final da fatia
    print(list3[0:2])
    print(list3[1:3])
    print(list3[1:-2])

    # Copiando listas
    list4 = [10, 20, 30, 40, 50]
    list5 = list4
    print(list4)
    list5.append(60)
    print(list4)

    # Cópia real
    list6 = list5[:]
    list6.append(70)
    print(list5)
    print(list6)
    
    print(list4 is list5)
    print(list5 is list6)

    pass