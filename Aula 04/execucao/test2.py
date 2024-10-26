from banco.connect import Connect

if __name__ == '__main__':
    try:
        connect = Connect()
        connect.open()
        print("Conexão testada com sucesso!")
    except Exception as e:
        print(e)
    pass