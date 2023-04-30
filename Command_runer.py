import Zoe
import CuteON
import os
import random


hello = (CuteON.Get_.getLine("education/BaseData.sws", "hello")).split(",")
bay = (CuteON.Get_.getLine("education/BaseData.sws", "bay")).split(",")
predlog = (CuteON.Get_.getLine("education/BaseData.sws", "predlog")).split(",")
too = (CuteON.Get_.getLine("education/BaseData.sws", "too")).split(",")
TV = (CuteON.Get_.getLine("education/BaseData.sws", "TV")).split(",")

say = (CuteON.Get_.getLine("education/BaseData.sws", "say")).split(",")

plan = (CuteON.Get_.getLine("education/BaseData.sws", "plan")).split(",")

status_good=(CuteON.Get_.getLine("education/exe_send.sws", "status_good")).split(",")
status_bad=(CuteON.Get_.getLine("education/exe_send.sws", "status_bad")).split(",")
status_neitral=(CuteON.Get_.getLine("education/exe_send.sws", "status_neitral")).split(",")

Words_duing = (CuteON.Get_.getLine("education/BaseData.sws", "Words_duing")).split(",")
qation_words = (CuteON.Get_.getLine("education/BaseData.sws", "qation_words")).split(",")
that_good=(CuteON.Get_.getLine("education/exe_send.sws", "that_good")).split(",")


Yandex = (CuteON.Get_.getLine("education/BaseData.sws", "Yandex")).split(",")
Google= (CuteON.Get_.getLine("education/BaseData.sws", "Googol")).split(",")
Youtube= (CuteON.Get_.getLine("education/BaseData.sws", "Youtube")).split(",")
AppList = CuteON.Get_.getAll("Apps.sws")

print(AppList)

def run(message):
    """
    Здесь прописывабтся все комманды
    Если вам надо добавить комманду то,
    напишите логику комманды используя
    шаблон:

    if word[0] == "найди":
        del message[0]
        del message[0]
        del message[0]
        return Search.Yandex(message)

    """
    for word in message:
        if word in Google:
            del message[0]
            del message[0]
            del message[0]
            return Zoe.Search.Googol(message)
        if word in Yandex:
            del message[0]
            del message[0]
            del message[0]
            return Zoe.Search.Yandex(message)
        if word in Youtube:
            del message[0]
            del message[0]
            del message[0]
            return Zoe.Search.Youtube(message)

        if word in (CuteON.Get_.getLine("education/BaseData.sws", "Start")).split(","):
            for w in message:
                if w in AppList:
                    os.startfile(w)
                     

        if word in "себе":
            return "Я Зои асистент для помощи, автоматизации. Могу помочь найти ответы, запустить приложение. Использую зарание написоный текст для генерации ответов на соабщения"