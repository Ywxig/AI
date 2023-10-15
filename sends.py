import ChatBot
import time
from OWM import Water_sys
from CuteON import Read_




def main(message=[], user="None"):

    PARAMETERS = Read_.readAll("education/parameters.sws")

    if PARAMETERS["show_dict_PARAMETERS"] == True:
        print("[Parameters] - " + str(PARAMETERS))

    add = ""
    start = time.time()
    print( "[@"+ str(user) + "]" + " ".join(message) + time.strftime("{ %H:%M }"))
    match_percentage = 0.78
    for i in message:
        
        if ChatBot.WordsOperations.is_word("погода", i) >= match_percentage:
            add = Water_sys.All(Read_.readLine("config.sws", "OWM-API-key"))

        if ChatBot.WordsOperations.is_word("найди", i) > match_percentage:
           add = ChatBot.Search.Yandex( message)

    respons = ChatBot.Generator.Chat.ChatCraft(message, "education/chatcraft.txt", iterabel_counts=64) + "\n" +  str(add)
    
    print("[Time of generation is] - " + str(time.time() - start))
    if respons == '' or respons == None:
        return "Я не знаю что сказать..."
    else:
       return respons