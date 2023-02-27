import CuteON
import random
"""

это модуль с реализацией всех алгоритмов для Зои. Данный модуль используется исключтельно в качестве оброботчика сообщений от юзера

"""
emoj = (CuteON.Get_.getLine("BaseData.sws", "emoj")).split(",")# Это мпимок всех эводжи который может использовать бот

command_riester = ["помащь"]

hello = (CuteON.Get_.getLine("BaseData.sws", "hello")).split(",")
bay = (CuteON.Get_.getLine("BaseData.sws", "bay")).split(",")
predlog = (CuteON.Get_.getLine("BaseData.sws", "predlog")).split(",")
too = (CuteON.Get_.getLine("BaseData.sws", "too")).split(",")

status_good=(CuteON.Get_.getLine("exe_send.sws", "status_good")).split(",")
status_bad=(CuteON.Get_.getLine("exe_send.sws", "status_bad")).split(",")
status_neitral=(CuteON.Get_.getLine("exe_send.sws", "status_neitral")).split(",")

Words_duing = (CuteON.Get_.getLine("BaseData.sws", "Words_duing")).split(",")
qation_words = (CuteON.Get_.getLine("BaseData.sws", "qation_words")).split(",")
that_good=(CuteON.Get_.getLine("exe_send.sws", "that_good")).split(",")


class Say:

    def Status(int_good:list, int_bad:list, weight_good:list=range(10),  weight_bad:list=range(10)):
        arr = []
        i = 0
        while i < len(int_good):
            arr.append(((int_good[i] * weight_good[i]) + (int_bad[i] * weight_bad[i]))/2)
            i += 1

        res = sum(arr) / len(arr)

        return res


    def Sand(ctxs = ["Obj=>PosSen=>emoj", "PosSen=>Obj=>emoj"], obj = [""], postfix_sentenc : list = [None]):
        renge = random.randint(0, len(ctxs) - 1)
        Say.Struct(ctxs[renge], obj=obj, postfix_sentenc=postfix_sentenc)

        

    def Struct(ctx, obj=None, postfix_sentenc : list = [None] ):

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
        try:

            arr = []

            for item in ctx.split("=>"):
                if item == "Obj":
                    arr.append(obj[random.randint(0, len(obj)-1)])

                if item == "PosSen":
                    arr.append(postfix_sentenc[random.randint(0, len(postfix_sentenc)-1)])

                if item == "Ins":
                    arr.append(Insert_word[random.randint(0, len(Insert_word)-1)])

                if item == "emoj":
                    arr.append(emoj[ random.randint( 0, (len(emoj) - 1) ) ])

                if item == "mersi":
                    arr.append(emoj[ random.randint( 0, (len(emoj) - 1) ) ])

            print(obj[random.randint(0, len(obj)-1)])
        except:
            pass
        return ' '.join(arr)


class Generator:

    def Command(content, ctx="помащь", arguments : list = None, count_arguments : int = 0):
        """
        Этот метод используется для получения 
        аргументов для использования в комманде
        возращает список аргументов которые
        ты указываешь в arguments используя 
        алгоритм распознования слов
        """
        arr_argument_for_return = []

        for i in content:

            if Zoe_algorithm_2(i, [ctx]) >= 55:

                if Zoe_algorithm_2(i, arguments) >= 55:
                    arr_argument_for_return.append(i)

                else:
                    pass

        if arr_argument_for_return == [] or arr_argument_for_return == None:
            print(arr_argument_for_return)
            return "Ошибка я немагу исполнить фунцию"
        
        else:
            print(arr_argument_for_return)
            return arr_argument_for_return


    def Send(werd_exemples, simple_sentenses):
        
        """
        Данный метод отвечает за создания реплики
        на основе слов которые мы передаём
        в качестве примера для создания ответа
        """

        j = len(werd_exemples)
        rand = random.randint(0, (j - 1))
        E = emoj[ random.randint( 0, (len(emoj) - 1) ) ]

        return werd_exemples[rand] + " " + simple_sentenses[random.randint(0, len(simple_sentenses) - 1)] + " " + E

    def Twsted(word, cut_shar, emoj=emoj):
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
    """
    
    функция main является рамспознователем сообщения
    пользователя. Используя мативатические фопрмулы
    и лагические блоки алгоритм понимает на сколько
    слово похоже на то которое мы передали как пример

    """
    for word in message:

        """
        В данном цикле и происходит вся магия
        Если необщодимо добавить новую ветку в разоворе,
        то нужно добавить логический блок и настроить его

        Но если мы говорим о коммандах для исполения
        то их нужно создовать по другой схеме.

        Вжно: если есть приорететные задачи то 
        их нужно ставить выше чем другие задачи
        их можно расставлять по честоте использования,
        или регулировать числа для прохождения комманды
        """
        
        if Zoe_algorithm_2(word, hello) >= 55:
            return Generator.Send(hello, (CuteON.Get_.getLine("BaseData.sws", "simple_sentens_hello")).split(","))

        if Zoe_algorithm_2(word, bay) >= 76:
            return Generator.Send(bay, (CuteON.Get_.getLine("BaseData.sws", "simple_sentens_bay")).split(","))

        if Zoe_algorithm_2(word, status_good) >= 55:
            print(Say.Status([10, 2, 3], [1, 2, 9]))
            return Generator.Send("", (CuteON.Get_.getLine("BaseData.sws", "simple_sentens_")).split(","))

        if Zoe_algorithm_2(word, predlog) >= 55:
            for word_2 in message:
                if Zoe_algorithm_2(word_2, too) >= 55:
                    return Say.Struct(ctx="PosSen=>emoj", postfix_sentenc=(CuteON.Get_.getLine("exe_send.sws", "status_good")).split(","))

        
        if Zoe_algorithm_2(word, qation_words) >= 55:
            for word_2 in message:
                if Zoe_algorithm_2(word_2, Words_duing) >= 55:
                    status = Say.Status([10, 2, 3], [1, 2, 9])
                    if status > 0:
                        return Say.Struct(ctx="PosSen=>emoj", postfix_sentenc=(CuteON.Get_.getLine("exe_send.sws", "status_good")).split(","))
                    if status < 0:
                        return Say.Struct(ctx="PosSen=>emoj", postfix_sentenc=(CuteON.Get_.getLine("exe_send.sws", "i_can_help")).split(","))
                    else:
                        return Say.Struct(ctx="PosSen=>emoj", postfix_sentenc=(CuteON.Get_.getLine("exe_send.sws", "that_good")).split(","))
                
#       """
        # пример как можно реальзовать комманду для Зои
        if Zoe_algorithm_2(word, ['выполни', "исполни"]) >= 55 or Zoe_algorithm_2(word, command_riester) >= 55:
            if Zoe_algorithm_2(word, ["помащь"]) >= 55:
                return "Хеай, я поммошник Зои версии 4.0"
#       """

        else:
            return "Я не понимаю что ты мне говоришь"

