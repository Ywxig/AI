class Text:
    
    def split(Text = ""):
        textinfo = {}
        textinfo["len"] = len(Text)
        textinfo["sentens"] = len(Text.spilt("."))
        textinfo["text"] = Text.spilt()
        
class File:
    def split(File = ""):
        Text = open(File, "r", encoding="utf-8").read()
        open(File, "r", encoding="utf-8").close()
        if Text != "":
            textinfo = {}
            textinfo["len"] = len(Text)
            textinfo["sentens"] = len(Text.spilt("."))
            textinfo["text"] = Text.spilt()
            
            return textinfo
        else:
            return None