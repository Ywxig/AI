import CuteON
import random
"""

это модуль с реализацией всех алгоритмов для Зои. Данный модуль используется исключтельно в качестве оброботчика сообщений от юзера

"""

hello = (CuteON.Get_.getLine("BaseData.sws", "hello")).split(",")
bay = (CuteON.Get_.getLine("BaseData.sws", "bay")).split(",")


class Say:

    def Struct(ctx, obj, postfix_sentenc : list = [None] ):

        emoj = (CuteON.Get_.getLine("BaseData.sws", "emoj")).split(",")

        Insert_word = []

        """        
        Данный метод отвечает за создани
        структуры ответов.

        Если мы оратимся к лингвистике то мы узнаем что
        в лингвистике описаны все структуры предложений

        Obj - Придмет о ктором говорится в предложение,
        евляется сущ. доесть таки слова как (привет, утро, т.п)

        PosSen - Простое предложения для завершения фразы,
        примеры (как дела, что делаешь, какие планы)

        Ins - вводное слова или конструкция прмер
        (во-первых, однажды)
        """

        arr = []

        for item in ctx.split("=>"):
            if item == "Obj":
                arr.append(obj[random.randint(0, 1)])

            if item == "PosSen":
                arr.append(postfix_sentenc[random.randint(0, len(postfix_sentenc)-1)])

            if item == "Ins":
                arr.append(Insert_word[random.randint(0, len(Insert_word)-1)])

            if item == "emoj":
                arr.append(emoj[ random.randint( 0, (len(emoj) - 1) ) ])

        print(obj[random.randint(0, len(obj)-1)])

        return ' '.join(arr)


class Generator:

    

    def Send(werd_exemples, simple_sentenses, send_structure=None):
        emoj = (CuteON.Get_.getLine("BaseData.sws", "emoj")).split(",")

        """
        Данный метод отвечает за создания реплики
        на основе слов которые мы передаём
        в качестве примера для создания ответа
        """

        j = len(werd_exemples)
        rand = random.randint(0, (j - 1))
        E = emoj[ random.randint( 0, (len(emoj) - 1) ) ]
        return werd_exemples[rand] + " " + simple_sentenses[random.randint(0, len(simple_sentenses) - 1)] + " " + E

    def Twsted(word, cut_shar, emoj=[]):
        word_arr = list(word)
        score = 0
        while score < cut_shar:
            del word_arr[len(word_arr)]
            score += 1
        return "".join(word_arr)


def Zoe_algorithm_2(Word, word_set):
    print(word_set)
    arr = []
    for word_ in word_set:
        cout = 0
        for i in Word:
            if i in list(word_):
                cout += 1
        res = (cout * 100) / len(word_)   
        arr.append(round(res))
    print(arr)
    return max(arr)

def main(message=[]):
    for word in message:
        
        if Zoe_algorithm_2(word, hello) >= 55:
            return Generator.Send(hello, (CuteON.Get_.getLine("BaseData.sws", "simple_sentens_hello")).split(","))

        if Zoe_algorithm_2(word, bay) >= 50:
            return Say.Struct(ctx="Obj=>PosSen=>emoj", obj=bay, postfix_sentenc=CuteON.Get_.getLine("BaseData.sws", "simple_sentens_bay").split(","))
