class Get_:

    def getAll(file):
        file = file = open(file, "r", encoding="utf-8")
        content = file.read()
        content_l = content.split("\n")

        arr = []

        for i in content_l:
            text = i.split("::")
            if text[0] == "public":
                arr.append(text[2])
            if content_l == "":
                pass
            else:
                pass
        return arr

    def getLine(file, nameString):
        file = file = open(file, "r", encoding="utf-8")
        content = file.read()
        content_l = content.split("\n")

        for i in content_l:
            text = i.split("::")
            if text[0] == "public" and text[1] == str(nameString):
                return text[2]
            else:
                pass

    def getObj(file, nameObj):
        file = open(file, "r", encoding="utf-8")
        content = file.read()
        content_l = content.split("public::"+nameObj+"::{")
        fin = content_l[1].split("}")
        return fin[0]


    def getClass(file, nameClass):
        file = open(file, "r")
        content = file = open(file, "r", encoding="utf-8")
        content_l = content.split("\n")
        for i in content_l:
            if i == "public::"+nameClass+"::[":
                text = i.split("::[")
                t = text[1].split("]")
                return t[0]

    def getLineText(content, nameString):
        content_l = content.split("\n")
        for i in content_l:
            text = i.split("::")
            if text[0] == "public" and text[1] == str(nameString):
                return text[2]
            else:
                pass 

class Read_:
    def Read(file):
        file = open(file, "r", encoding="utf-8")
        text = file.read()
        return text

class Write_:
    def WriteStr(file, text):
        file = open(file, "a")
        if text.split()[0] == "public" or text.split()[0] == "private":
            file.write(text)


