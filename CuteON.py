type_str_action = ("str", "url", "file")
type_int_action = ("int")
type_list_action = ("list", "rgb", "rgba", "diolog", "matrix")
type_float_action = ("float")
WebFile = ('html', 'css', 'js')
coment = ("//", "№")

import time
import math

class Types:

    class List:

        def toInt(list_):
            try:
                list_ = list_.split(",")
            except:
                pass
            arr = []
            for i in list_:
                arr.append(int(i))
            print(arr)
            return arr

    def toIntVec(list_):
        try:
            list_ = list_.split(",")
        except:
            pass
        arr = []
        for i in range(2):
            arr.append(int(i))
        return arr

class Color:
    def subtraction(Color_vector1 : list, Color_vector2 : list) -> list:
        Color_vector = []
        for color in range(3):
            rezalt_color = Color_vector1[color] - Color_vector2[color]
            if rezalt_color < 0:
                Color_vector.append(0)
            if rezalt_color > 255:
                Color_vector.append(255)
            else:
                Color_vector.append(rezalt_color)
        return Color_vector   
    
    def addition(Color_vector1 : list, Color_vector2 : list) -> list:
        Color_vector = []
        for color in range(3):
            rezalt_color = Color_vector1[color] + Color_vector2[color]
            if rezalt_color < 0:
                Color_vector.append(0)
            if rezalt_color > 255:
                Color_vector.append(255)
            else:
                Color_vector.append(rezalt_color)
        return Color_vector

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
            if text[1] == str(nameString):
                return text[2]
            else:
                pass

    def getType(file, nameString):
        file = file = open(file, "r", encoding="utf-8")
        content = file.read()
        content_l = content.split("\n")
        for i in content_l:
            text = i.split("::")
            if text[1] == str(nameString):
                return text[0]
            else:
                pass

    def getObj(file : str, nameObj : str) -> dict:
        """
        getObj read obj in file and serialize this
        pbject. And return dict values for this
        opject
        """
        file = open(file, "r", encoding="utf-8")
        content = file.read()
        content_l = content.split("object::"+nameObj+"::{")
        fin = content_l[1].split("}")
        content = fin[0]
        values = {}
        content_l = content.split("\n")
        for i in content_l:
            text = i.split("::") 
            values[text[1]] = text[2]
        return values

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
                if text[0] in type_list_action:
                    return text[2].split(",")
                if text[0] in type_str_action:
                    return str(text[2])
                if text[0] in type_int_action:
                    return int(text[2])
                if text[0] in type_float_action:
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
                if text[0] in type_list_action:
                    arr[text[1]] = text[2].split(",")
                if text[0] in type_str_action:
                    arr[text[1]] = str(text[2])
                if text[0] in type_int_action:
                    arr[text[1]] = int(text[2])
                if text[0] in type_float_action:
                    arr[text[1]] = float(text[2])
                if text[0] == "bool":
                    arr[text[1]] = bool(text[2])
                if text[0] == "print":
                    print(text[1])
                if text[0] in coment:
                    pass
            count_line += 1
        return arr

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