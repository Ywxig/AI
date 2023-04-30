import CuteON
import random
import Command_runer
import pymorphy2

def help():
    return "это модуль с реализацией всех алгоритмов для Зои. Данный модуль используется исключтельно в качестве оброботчика сообщений от юзера"

emoj = (CuteON.Get_.getLine("education/BaseData.sws", "emoj")).split(",")# Это мпимок всех эводжи который может использовать бот

def Filter(arr=[], target=[]):
    ARR = []
    for i in arr:
        if i in target:
            pass
        else:
            ARR.append(i)
    return ARR

class Generator:

    def random_message(messages=[]):
        r = random.randint(0, len(messages) - 1)
        return messages[r]

    def Message(message_exe="hello world", word_list=[]):
        for i in message_exe.split():
            if i in CuteON.Get_.getAll("BaseData.sws"):
                pass

            
    def defain(text, key_word, def_=help()):
        for i in text:
            if Zoe_Word(i, [key_word]) >= 55:
                if def_ == "" or def_ == None:
                     return "Ошибка я немагу исполнить фунцию"
                else:
                    return def_
            else:
                pass

    def Command(content, ctx="помащь", arguments : list = None, count_arguments : int = 0):
        """
        Этот метод используется для получения 
        аргументов для использования в комманде
        возращает список аргументов которые
        ты указываешь в arguments используя 
        алгоритм распознования слов
        """
        pass


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

def Zoe_Word(Word, word_set, messge="Сообщение"):
    data_set = CuteON.Get_.getAll("Data Set/ds.sws")
    anser_set = CuteON.Get_.getAll("Data Set/anser.sws")
    c = 0
    arr = []
    for word_ in word_set:
        REPIAT_LETER = 0
        for i in Word:
            try:
                if i == list(str(word_[0]))[list(Word).index(i)]:
                    REPIAT_LETER += 1
                else:
                    pass
                c += 1       
            except:
                return Generator.Markov(messge)
        res = (REPIAT_LETER * 100)/1
        arr.append(res)
    return str(anser_set[arr.index(max(arr))][0])

def keywords(sentence):
    morph = pymorphy2.MorphAnalyzer()
    words = sentence.split()
    keywords = []
    for word in words:
        parsed_word = morph.parse(word)[0]
        if 'NOUN' in parsed_word.tag or 'ADJF' in parsed_word.tag:
            keywords.append(parsed_word.normal_form)
    return keywords

class Search:

    def Youtube(List):

        task = '+'.join(List)
        s = 'https://www.youtube.com/results?search_query=' + task
        return s

    def Googol(List):

        task = '+'.join(List)
        s = 'https://www.google.com/search?q=' + task
        return s

    def Yandex( List):
        task = '%20'.join(List)
        s = 'https://yandex.ru/yandsearch?clid=202826&text=' + task
        return s

def return_commad(message):
    """
    данная функция по конструкции комманды исполняет её
    некоторые комманды уже сделаны пользователь может
    вводить или изменять существующие комманды.
    """
    prompt=Command_runer.run(message)
    
    if prompt == "":
        return "No is prompt"
    else:
        return prompt

class Generator:

    def generate_text(text : str, keywords : list, order=1, length=5):
        words = text.split()
        markov_dict = {}
        # Создаем словарь цепей Маркова
        for i in range(len(words) - order):
            key = tuple(words[i:i+order])
            value = words[i+order]
            if key in markov_dict:
                markov_dict[key].append(value)
            else:
                markov_dict[key] = [value]
        # Выбираем случайный ключ из словаря
        possible_keys = [key for key in markov_dict.keys() if all(keyword in key for keyword in keywords)]
        if possible_keys:
            current_key = random.choice(possible_keys)
        else:
            current_key = random.choice(list(markov_dict.keys()))
        # Генерируем текст на основе цепей Маркова
        sentence = list(current_key)
        for i in range(length - order):
            if current_key in markov_dict:
                current_word = random.choice(markov_dict[current_key])
            else:
                current_word = random.choice(list(markov_dict.keys()))
            sentence.append(current_word)
            current_key = tuple(sentence[-order:])
        count = 0
        delete_word=[]
        for i in sentence:
            if i == sentence[count] and i in delete_word:
                del sentence[count] 
            else:
                delete_word.append(sentence[count])
            count += 1
        print("Delete words is =",delete_word)
        delete_word=[]
        return " ".join(sentence)

    def Markov(text, order=2):
        length = len(text.split())
        t = text.split()[0]
        text = CuteON.Read_.Read("education/text.txt")
        words = text.split()
        markov_dict = {}
        for i in range(len(words) - order):
            key = tuple(words[i:i+order])
            value = words[i+order]
            if key in markov_dict:
                markov_dict[key].append(value)
            else:
                markov_dict[key] = [value]

        if markov_dict:
            current_key = random.choice(list(markov_dict.keys()))
        else:
            return 'None'
        sentence = list(current_key)
        for i in range(length - order):
            current_word = random.choice(markov_dict[current_key])
            sentence.append(current_word)
            current_key = tuple(sentence[-order:])

        return " ".join(sentence)


def Zoe_Sentenses(message, file_data_set="Data Set/ds.sws", file_ansers="Data Set/anser.sws"):
    data_set = CuteON.Get_.getAll(file_data_set)
    anser_set = CuteON.Get_.getAll(file_ansers)
    for i in data_set:
        A = len(str(anser_set[data_set.index(i)]).split("|"))
        MS = len(str(message).split())
        
        if MS <= 1:
            if A > 1:
                return str(anser_set[data_set.index(i)][0]).split("|")[random.randint(0, len(str(anser_set[data_set.index(i)][0]).split("|") ) - 1)]
            else:
                print(anser_set[data_set.index(i)])
                return str(anser_set[data_set.index(i)][0])
        if MS > 1 and message == str(i[0]):
            if A > 1:
                return str(anser_set[data_set.index(i)][0]).split("|")[random.randint(0, len(str(anser_set[data_set.index(i)][0]).split("|") ) - 1)]
            else:
                return str(anser_set[data_set.index(i)][0])
    return Generator.Markov(message)
