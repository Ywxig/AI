from Zoe import *
import CuteON

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
            send = Say.Struct(ctx="PosSen=>emoj", postfix_sentenc=(CuteON.Get_.getLine("exe_send.sws", "status_good")).split(","))
            if Zoe_algorithm_2(send, word) >= 85:
                return Say.Struct(ctx="Obj=>PosSen=>emoj", postfix_sentenc=(CuteON.Get_.getLine("exe_send.sws", "status_good")).split(","), obj=["Это"])
            else:
                return send

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