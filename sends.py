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
        
        if ChatBot.is_word("погода", i) >= match_percentage:
            add = Water_sys.All(Read_.readLine("config.sws", "OWM-API-key"))

        if ChatBot.is_word("найди", i) > match_percentage:
           add = ChatBot.Search.Yandex( message)

    respons = ChatBot.Generator.Text(" ".join(message), "education/text.txt",
                                                chance_choosing_full_pair=PARAMETERS["chance_choosing_full_pair"],
                                                chance_choosing_main_word=PARAMETERS["chance_choosing_main_word"],
                                                chance_teleport = PARAMETERS["chance_teleport"],
                                                chance_use_message = PARAMETERS["chance_use_message"],
                                                chance_use_next_word =PARAMETERS["chance_use_next_word"],
                                                match_percentage =PARAMETERS["match_percentage"],
                                                Probability_descent_for_use_message =PARAMETERS["Probability_descent_for_use_message"],
                                                max_size_respons = PARAMETERS["max_size_respons"],
                                                min_word_in_pair = PARAMETERS["min_word_in_pair"],
                                                max_word_in_pair = PARAMETERS["max_word_in_pair"],
                                                file_for_hybrid="education/hybrid.txt") + "\n" +  str(add)
    
    print("[Time of generation is] - " + str(time.time() - start))
    if respons == '' or respons == None:
        return "Я не знаю что сказать..."
    else:
       return respons