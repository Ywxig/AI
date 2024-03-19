from . import Types

class Read_:
    def Read(file):
        File = open(file, "r", encoding="utf-8").read()
        if File != "":
            return File
        else:
            return "None"
        
    def readLine(file, nameString):
        file = file = open(file, "r", encoding="utf-8")
        content = file.read()
        content_l = content.split("\n")
        for i in content_l:
            text = i.split("::")
            if text[1] == str(nameString):
                if text[0] in Types.type_list_action:
                    return text[2].split(",")
                if text[0] in Types.type_str_action:
                    return str(text[2])
                if text[0] in Types.type_int_action:
                    return int(text[2])
                if text[0] in Types.type_float_action:
                    return float(text[2])
                if text[0] == "bool":
                    return bool(text[2])

    def readAll(file) -> dict:
        file = open(file, "r", encoding="utf-8")
        content = file.read()
        content_l = content.split("\n")
        arr = {}
        count_line = 0
        for i in content_l:
            if i != "":
                text = i.split("::")
                if text[0] in Types.type_list_action:
                    arr[text[1]] = text[2].split(",")
                if text[0] in Types.type_str_action:
                    arr[text[1]] = str(text[2])
                if text[0] in Types.type_int_action:
                    arr[text[1]] = int(text[2])
                if text[0] in Types.type_float_action:
                    arr[text[1]] = float(text[2])
                if text[0] == "bool":
                    arr[text[1]] = bool(text[2])
                if text[0] == "print":
                    print(text[1])
                if text[0] in Types.coment:
                    pass
            count_line += 1
        return arr

    def noFile(Text) -> dict:
        content = Text
        content_l = content.split("\n")
        arr = {}
        count_line = 0
        for i in content_l:
            if i != "":
                text = i.split("::")
                if text[0] in Types.type_list_action:
                    arr[text[1]] = text[2].split(",")
                if text[0] in Types.type_str_action:
                    arr[text[1]] = str(text[2])
                if text[0] in Types.type_int_action:
                    arr[text[1]] = int(text[2])
                if text[0] in Types.type_float_action:
                    arr[text[1]] = float(text[2])
                if text[0] == "bool":
                    arr[text[1]] = bool(text[2])
                if text[0] == "print":
                    print(text[1])
                if text[0] in Types.coment:
                    pass
            count_line += 1
        return arr