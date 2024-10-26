from modelo.file import File

if __name__ == '__main__':
    try:
        file = File()
        path = "example.txt"
        file.open_file(path, "r")
        file.read_file()
        file.close_file()
    except Exception as e:
        print(e)
    pass