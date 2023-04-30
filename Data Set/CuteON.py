class Get_:

    def getAll(file):
        file = file = open(file, "r", encoding="utf-8")
        content = file.read()
        content_l = content.split("\n")

        return_ = []
        arr = []

        for i in content_l:
            text = i.split("::")
            if text[0] == "public":
                return_.append(text[2])
            if content_l == "":
                pass
            else:
                pass
            


        return return_


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
        file = open(file, "r")
        content = file = open(file, "r", encoding="utf-8")
        content_l = content.split("\n")
        for i in content_l:
            if i == "public::"+nameObj+"::{":
                text = content_l[i].split("::{")
                t = text[1].split("}")
                return t[0]

    def getClass(file, nameClass):
        file = open(file, "r")
        content = file = open(file, "r", encoding="utf-8")
        content_l = content.split("\n")
        for i in content_l:
            if i == "public::"+nameClass+"::[":
                text = i.split("::[")
                t = text[1].split("]")
                return t[0]


class Read_:
    def Read(file):
        file = open(file, "r")
        text = file.read()
        return text

class Write_:
    def WriteStr(file, text):
        file = open(file, "a", encoding="utf-8")
        if text.split()[0] == "public" or text.split()[0] == "private":
            file.write(text)
        else:
            file.write("\npublic::none::"+text)