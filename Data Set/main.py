import CuteON
from colorama import Fore, Back, Style

while True:
    com = input(Fore.CYAN + ">>>: ")

    if com == "add":
        text1= input('Text for data set: ')
        text2= input('Text for anser: ')
        CuteON.Write_.WriteStr("ds.sws", text1)
        CuteON.Write_.WriteStr("anser.sws", text2)

    if com == "all":
            print(Fore.CYAN + CuteON.Get_.getAll("ds.sws"))
            print(Fore.BLUE + CuteON.Get_.getAll("anser.sws"))
            
