class Write_:

    def write(file, text):
        file = open(file, "w", encoding="utf-8")
        file.write(text)
        file.close()

    def add(file, text):
        file = open(file, "a")
        if text.split()[0] == "public" or text.split()[0] == "private":
            file.write(text)

    def WriteLine(file : str, Line : str):
        nameLine = Line.split("::")[1]
        file_ = open(file, "r", encoding="utf-8").read()
        content = file_.split("\n")
        for i in content:
            if i.split("::")[1] == nameLine:
                cutLine = i
        fileParts = file_.split(cutLine)
        open(file, "w", encoding="utf-8").write(str(fileParts[0]) + str(Line) + str(fileParts[1]))