class File:
    @staticmethod
    def write(nome="log", content=""):
        f  = open(nome, "w")
        f.write(content)
        f.close()