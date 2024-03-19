from ChatBot import Chat, Text
from ChatBot import LinkGen as link
from ChatBot import utils as wo
from ChatBot import initBot
import time
from OWM import Water_sys
from CuteON import Read_

def main(message : str =[], user="None", cfg : any ={}) -> str:

    respons = ""
    add = ""
    start = time.time()
    print( "[@"+ str(user) + "]" + " ".join(message) + time.strftime("{ %H:%M }"))
    match_percentage = 0.88
    for i in message:
        
        if wo.is_word("себе", i) > match_percentage:
           add = "\n" + cfg["About"]["Bio"]

        if wo.is_word("такое", i) > match_percentage:
           prompt = " ".join(message).split(i)[1]
           add = "\n" + Text.TextWiki(prompt) 

        if wo.is_word("сочинение", i) > match_percentage:
            prompt = " ".join(message).split(i)[1]
            add = Text.TextCraft(prompt.split(), "education/textcraft.txt")

        if wo.is_word("погода", i) >= match_percentage:
            count = 0
            for j in message:
                count += 1
                if j == "в":
                    add = Water_sys.All(Read_.Read_.readLine("config.sws", "OWM-API-key"), message[count + 1])
                else:
                     add = Water_sys.All(Read_.Read_.readLine("config.sws", "OWM-API-key"), "молдова")

        if wo.is_word("найди", i) > match_percentage:
           add = link.Search.Yandex( message)
    try:
        respons = Chat.ChatCraft(message, "education/chatcraft.txt") + "\n" +  str(add)
    except:
        respons = str(add)
    print("[Time of generation is] - " + str(time.time() - start))
    if respons == '' or respons == None:
        return "Я не знаю что сказать..."
    else:
       return respons

if __name__ == "__main__":
    BOT = initBot.init("Config.sws")
    message = "None"
    while " ".join(message) != "quit":
        message = input("<user:> ").split()
        print(main(message=message, user="None", cfg=BOT))
