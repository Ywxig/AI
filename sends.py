import ChatBot
import time

match_percentage = 0.88

def main(message=[]):
        start = time.time()
        print(message)
        add = ""
        for i in message:
                if ChatBot.is_word("погода", i) >= match_percentage:
                        add = ChatBot.Water_sys.All('88c77e859289463928b17b24f2f7ea99')

                if ChatBot.is_word("выключи", i) > match_percentage:
                        ChatBot.ShootDown()

                if ChatBot.is_word("найди", i) > match_percentage:
                        add = ChatBot.Search.Yandex( message)

                if ChatBot.is_word("открой", i) > match_percentage:
                        add = ChatBot.App.open( message[message.index(i) + 1] )


        respons = ChatBot.Generator.wandering_drunk_modified(" ".join(message), "education/text.txt", adaptive_respons_size=True, file_for_hybrid="education/hybrid.txt") + "\n" +  add

        if respons == '' or respons == None:
                return "Я не знаю что сказать..."
        else:
                return respons

 