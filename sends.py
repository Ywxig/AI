from ChatBot import Chat, Text
from ChatBot import LinkGen as link
from ChatBot import WordOperations as wo
import time
from OWM import Water_sys
from CuteON import Read_

def main(message=[], user="None"):

    PARAMETERS = Read_.readAll("education/parameters.sws")

    if PARAMETERS["show_dict_PARAMETERS"] == True:
        print("[Parameters] - " + str(PARAMETERS))
    respons = ""
    add = ""
    start = time.time()
    print( "[@"+ str(user) + "]" + " ".join(message) + time.strftime("{ %H:%M }"))
    match_percentage = 0.78
    for i in message:
        if wo.is_word("такое", i) > match_percentage:
           add = Text.Text(" ".join(message), "education/text.txt", file_for_hybrid="education/hybrid.txt") 

        if wo.is_word("погода", i) >= match_percentage:
            add = Water_sys.All(Read_.readLine("config.sws", "OWM-API-key"))

        if wo.is_word("найди", i) > match_percentage:
           add = link.Search.Yandex( message)
    try:
        respons = Chat.ChatCraft(message, "education/chatcraft.txt", iterabel_counts=64) + "\n" +  str(add)
    except:
        respons = str(add)
    print("[Time of generation is] - " + str(time.time() - start))
    if respons == '' or respons == None:
        return "Я не знаю что сказать..."
    else:
       return respons