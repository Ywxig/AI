from CuteON import *

class Builder:
     
    class File:

        def build(file : str, content : list):
            arr = []
            DB_TYPES = ("sws")
            for i in content:
                item = i.split()
                if item[0] == "creat":
                    try:
                        file_ = item[1].split(".")[1]
                        if file_ in DB_TYPES:
                            Write_.write(file + file_, "")
                    except:
                        Write_.write(item[1], "")
                
                if item[0] == "insert":
                    FILE = content[content.index(i)].split()[1]
                    arr.append(Read_.Read(FILE))
                
                else:
                    arr.append(i)       

    class CSS:

        def New(tupe_ : str, name : str):
            if tupe_ == "id":
                return "#" + name + "{"
            if tupe_ == "class":
                return "." + name + "{"
            else:
                print("[Sorry what is `" + tupe_ + "`? I dont know what is type of style!]")      

    class HTML:

        def Tag(tag : str, ctx : str, class_:str):
            if class_ != "":
                return '<' + tag + ' class="' + class_ + '">' + ctx + '</' + tag + '>'
            else:
                return '<' + tag + '>' + ctx + '</' + tag + '>'

        def Form(action="", content=""):
            return '<form action="/'+action+'" method="POST">\n' + content + '\n</form>'

        def build(file : str, content : list, return_=False):
            arr = []
            for i in content:
                if i == "#insert":
                    FILE = content[content.index(i)].split()[1]
                    arr.append(Read_.Read(FILE))
                if i == "#include":
                    FILE = content[content.index(i)].split()[1]
                    name_file = FILE.split(".")
                    if name_file[1] == "css":
                        arr.append("<style>\n" + open("template/" + Read_.Read(FILE), "r").read() + "\n" + "</style>\n")

                    if name_file[1] == "js":
                        arr.append("<script>\n" + open("template/" + Read_.Read(FILE), "r").read() + "\n" + "</script>\n")
                
                else:
                    arr.append(i)
            if return_ == False:
                Write_.write(file, "\n".join(arr))
            else:
                return "\n".join(arr)

DIR = "template/"
command = ["#include"]

class Compilator:

    def comp(file, file_out):
        text = open(DIR + file, "r", encoding="utf-8").read()
        Text = text.split("\n")
        fin = []
        count = 0
        for i in Text:
            print(i)
            word = i.split()
            try:
                print(word[0])
                if word[0] == "#include":
                    name_file = word[1].split(".")
                    if name_file[1] == "css":
                        print("ok")
                        fin.append("<style>\n" + open(word[1], "r").read() + "\n" + "</style>\n")
                        del Text[count]
                    if name_file[1] == "js":
                        fin.append("<script>\n" + open(word[1], "r").read() + "\n" + "</script>\n")
                        del Text[count]              
                else:
                    fin.append(i)
            except:
                fin.append(i)
            count += 1
            open(file_out, "w", encoding="utf-8").write("\n".join(fin))

class CuteScript:
    FLAG = "main"

    class Post():

        def text_md(text_):
            text = []
            ctx = text_.split("\n")
            for i in ctx:
                paragraph = []
                word = i.split()
                try:
                    for j in word:
                        if j == "(":
                            paragraph.append("<i>")
                        if j == ")":
                            paragraph.append("</i>")

                        if j == "{":
                            paragraph.append("<b>")
                        if j == "}":
                            paragraph.append("</b>")

                        if j == "#":
                            paragraph.append("<h1>")

                        if j == "##":
                            paragraph.append("<h2>")

                        if j == "###":
                            paragraph.append("<h3>")

                        else:
                            paragraph.append(j)
                except:
                    pass
                text.append(" ".join(paragraph))
            return "<p>" + "\n".join(text) + " </p>"

        def new_post(file, data, type_="article"):
            ctx = open(file, "r", encoding="utf-8").read().split("<cut>")
            if type_ == "video":
                img = data["img"]
                link = data["link"]
                title = data["title"]
            
                content = open("template/video_element.html", "r", encoding="utf-8").read().split("\n")
                arr = []
                for i in content:
                    if i == "img:":
                        arr.append('<a href="' + link + '"><img class="project-img" src="' + img + '"></a>')
                    if i == "title:":
                        arr.append("<h1>" + title + "</h1>")
                    if i == "link:":
                        arr.append('<button type="submit" name="video" value="' + link + '" class="show">Смотреть</button>')
                    else:
                        arr.append(i)
                for i in arr:
                    if i == "title:" or i == "img:":
                        arr.remove(i)

            if type_ == "article":
                title = data["title"]
                contnet = data["ctx"]
                link = data["link"]

                content = open("posts/article_element.html", "r", encoding="utf-8").read().split("\n")
                arr = []
                for i in content:
                    if i == "ctx:":
                        arr.append(
                            CuteScript.Post.text_md(contnet)
                        )
                    if i == "title:":
                        arr.append("<h1>" + title + "</h1>")
                    if i == "link:":
                        arr.append('<a href="' + link + '"><button type="submit" name="article" value="' + link + '" class="show">Смотреть</button><a>')
                    else:
                        arr.append(i)
                for i in arr:
                    if i == "title:" or i == "ctx:":
                        arr.remove(i)

            if type_ == "projet":
                img = data["img"]
                desc = data["desc"]
                title = data["title"]

                content = open("template/project.html", "r", encoding="utf-8").read().split("\n")
                arr = []
                for i in content:
                    if i == "img:":
                        arr.append('<img class="project-img" src="' + img + '">')
                    if i == "title:":
                        arr.append("<h1>" + title + "</h1>")
                    if i == "description:":
                        arr.append("<p>" + desc + "</p>")
                    if i == "link:":
                        arr.append('<a href="projects/' + title + '/readme.html"><button class="learn-more">Learn more</button></a>')
                    else:
                        arr.append(i)
                for i in arr:
                    if i == "title:" or i == "img:" or i == "description:":
                        arr.remove(i)
                    
            open(file, "w", encoding="utf-8").write(ctx[0] + "\n".join(arr)+ "\n\n<cut>" + ctx[1])

    def ConveyorBuilding(files, config="config.sws"):
        for file in files:
            CuteScript.start(Get_.getLine(config, "DIR") + file)


    def buildHTML(line, vars_ = {}):
        for i in line.split():
            Word = i.split(".")

            if Word[0] == "HTML":
                if Word[1] == "tag":
                    return Builder.HTML.Tag(Word[2], str(line.split("HTML.tag." + Word[2])[1]), class_="")
                
                if Word[1] == "form":
                    file_ = line.split("HTML.form." + Word[2]+" ")[1]
                    return Builder.HTML.Form(content=Read_.Read(file_), action=Word[2])

                if Word[1] == "add":
                    return str(line.split("HTML.add")[1])
                
                if Word[1] == "element":
                    file_type = str(line.split("HTML.element ")[1]).split(".")[1]
                    if file_type in WebFile:
                        return Read_.Read(str(line.split("HTML.element ")[1]))
                    else:
                        print("[Element is not for web. I can't use this element]")

            if Word[0] == "CSS":

                if Word[1] == "start":
                    return "<style>"

                if Word[1] == "new":
                    return Builder.CSS.New("id", str(line.split("CSS.new ")[1]))

                if Word[1] == "element":
                    file_type = str(line.split("CSS.element ")[1]).split(".")[1]
                    if file_type == "css":
                        return Read_.Read(str(line.split("CSS.element ")[1]))
                    else:
                        print("[Element is not `css`. I can't use this element]")

                if Word[1] == "end":
                    try:
                        if str(line.split("CSS.end ")[1]) == "element":
                            return "}"
                        else:
                            return "</style>"
                    except:
                        return "</style>"
       
            if Word[0] == "doc":
                if Word[1] == "start":
                    return '<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t'
                if Word[1] == "title":
                    return '<title>' + str(line.split("doc.title ")[1]) + '</title>\n</head>\n<body>\n\n'
                if "end":
                    return '</body>\n</html>'

            if Word[0] == "console":
                if Word[1] == "var":
                    print(vars_[line.split()[1]])
            
                if Word[1] == "time":
                    time_ = time.strftime("{ %H:%M }")
                    print(time_)

            if line.split()[0] in vars_:
                return str(vars_[line.split()[0]])

    def start(file : str, comm_prefix = "") -> list:
        strat_time = time.time()
        vars_ = {}
        STEK_COMMAND = []
        FILE = Read_.Read(file) #Получаем данные из файла
        HEEP = FILE.split("\n") #Делаем кучу из фала по которой будем ходить

        for line in HEEP:
            if line == "":
                pass
            else:
                items = line.split()
                """Читаем кучу по линиям и делаем очередь из комманд"""

                if comm_prefix + items[0] == "build":
                    STEK = []
                    for i in STEK_COMMAND:
                        if i == None:
                            pass
                        else:
                            STEK.append(i)
                    if items[1] == "html":
                        Builder.HTML.build(vars_[items[2]], STEK)

                    if items[1] == "db":
                        Builder.HTML.build(vars_[items[2]], STEK)
                if items[0] == "line":
                    try:
                        vars_[items[1]] = items[0] + "::" + items[1] + "::" + items[2]
                    except:
                        vars_[items[1]] = items[0] + "::" + items[1] + "::0"


                if items[0] == "int":
                    try:
                        vars_[items[1]] = int(items[2])
                    except:
                        vars_[items[1]] = 0


                if items[0] == "str":
                    vars_[items[1]] = items[2]


                if items[0] == "rgb":
                    vars_[items[1]] = items[2].split(",")


                if items[0] == "@":
                    vars_[items[1]] = items[2]


                if comm_prefix + items[0] == "subtractionRGB":
                    Vec1 = Types.toIntVec(vars_[items[1]])
                    Vec2 = Types.toIntVec(vars_[items[2]])
                    vars_[items[1]] = Color.subtraction(Vec1, Vec2)


                if comm_prefix + items[0] == "additionRGB":
                    Vec1 = Types.toIntVec(vars_[items[1]])
                    Vec2 = Types.toIntVec(vars_[items[2]])
                    vars_[items[1]] = Color.addition(Vec1, Vec2)


                if comm_prefix + items[0] == "write" and CuteScript.FLAG == "main":
                    if items[2] in vars_ and items[1] in vars_:
                        Write_.WriteLine(vars_[items[1]], str(vars_[items[2]]))
                        STEK_COMMAND.append("write " + vars_[items[1]] + " " + str(vars_[items[2]]))
                    else:
                        Write_.WriteLine(items[1], items[2])
                        STEK_COMMAND.append("write " + items[1] + " " + items[2])


                if comm_prefix + items[0] == "getLine":
                    if items[2] in vars_ and items[1] in vars_:
                        try:
                            if Get_.getType(vars_[items[1]], (str(vars_[items[2]])).split("::")[1]) in type_list_action:
                                new_list = Get_.getLine(vars_[items[1]], (str(vars_[items[2]])).split("::")[1])
                                vars_[items[2]] = new_list.split(",")
                            else:
                                 vars_[items[2]] = Get_.getLine(vars_[items[1]], (str(vars_[items[2]])).split("::")[1])
                        except:
                            pass
                    else:
                        if Get_.getType(vars_[items[1]], items[2]) in type_list_action:
                            new_list = Get_.getLine(vars_[items[1]], items[2])
                            vars_[items[2]] = new_list.split(",")
                        else:
                            vars_[items[2]] = Get_.getLine(vars_[items[1]], items[2])          


                if comm_prefix + items[0] == "clone" and CuteScript.FLAG == "main":
                    vars_[ "clone_" + items[1]] =  vars_[items[1]]

                if comm_prefix + "import" in STEK_COMMAND:
                    STEK_COMMAND.append( "#include" + vars_[items[1]])

                if comm_prefix + items[0] == "import":
                    STEK_COMMAND.append( "#insert" + vars_[items[1]])

                if items[0] in vars_ and items[1] == "=" and items[2] in vars_:
                    vars_[items[0]] = vars_[items[2]]


                if items[0] in vars_ and items[1] == "+" and items[2] in vars_:
                    try:
                        result = int(vars_[items[0]]) + int(vars_[items[2]])
                        vars_[items[0]] = result
                    except:
                        print("You are trying to perform mathematical addition not with numbers")


                if items[0] in vars_ and items[1] == "-" and items[2] in vars_:
                    try:
                        result = int(vars_[items[0]]) - int(vars_[items[2]])
                        vars_[items[0]] = result
                    except:
                        print("You are trying to do mathematical subtraction not with numbers")


                if comm_prefix + items[0] == "print" and CuteScript.FLAG == "main":
                    print(vars_[items[1]])


                if comm_prefix + items[0] == "toLine":
                    if str(items[1]) == "rgb":
                        normalize = []
                        for i in range(3):
                            normalize.append(str(vars_[items[3]][i]))
                        rgb_l = ",".join(normalize)
                    elif str(items[1]) == "int":
                        vars_[items[2]] = str(items[1]) + "::" + str(items[2]) + "::" + str(vars_[items[3]])


                if comm_prefix + items[0] == "loop":
                    cycle = FILE.split("{")
                    body = cycle[1].split("}")
                    count = 0
                    while count < vars_[items[1]]:
                        for q in body[0].split("\n"):
                            STEK_COMMAND.append(CuteScript.command(q, vars_))
                        count += 1

                if comm_prefix + items[0] == "ui":
                    cycle = FILE.split("{")
                    body = cycle[1].split("}")
                    for q in body[0].split("\n"):
                        STEK_COMMAND.append(CuteScript.buildUI(q, vars_))

                if comm_prefix + items[0] == "html":
                    cycle = FILE.split("{")
                    body = cycle[1].split("}")
                    for q in body[0].split("\n"):
                        STEK_COMMAND.append(CuteScript.buildHTML(q, vars_))

                if comm_prefix + items[0] == "css":
                    cycle = FILE.split("{")
                    body = cycle[1].split("}")
                    for q in body[0].split("\n"):
                        STEK_COMMAND.append(CuteScript.styler(q, vars_))              

                if comm_prefix + items[0] == "Make":
                    all_body = FILE.split("{")
                    make_body = all_body[1].split("}")[0]
                    CuteScript.Meke(
                        file=file,
                        STEK=STEK_COMMAND,
                        VARS=vars_,
                        BODY=make_body.split("\n"),
                        comm_prefix=comm_prefix
                    )

        STEK = []
        for i in STEK_COMMAND:
            if i == None:
                pass
            else:
                STEK.append(i)
        return STEK
        print( "[Code execution time] - " + str(time.time() - strat_time) + "ms")