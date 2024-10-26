class File:
    file = None
    
    def open_file(self, path, mode):
        self.file = open(path, mode)
        pass

    def close_file(self):
        self.file.close()
        pass
    
    def read_file(self):
        for line in self.file.readlines():
            print(line)
        pass
    
    def write_file(self, text):
        self.file.write(text)
        pass
    
    
    pass