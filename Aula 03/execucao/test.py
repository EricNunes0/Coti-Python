from modelo.file import File
from modelo.person import Person

if __name__ == '__main__':
    try:
        person = Person("Eric", "eric@email.com.br")
        file = File()
        path = "example.txt"

        file.open_file(path, "w")
        file.write_file(str(person))
        print("Arquivo gerado com sucesso!")
        file.close_file()
    except Exception as e:
        print(e)
    pass