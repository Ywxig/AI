import pymorphy2
from CuteON import Read_ 

def Frequency(arr, item):
    count = 0
    for i in arr:
        if item == i:
            count += 1
        else:
            pass
    return count / len(arr)

def get_prompt_key_words(file_propt, index_of_list_keywords=0):
    file = ((open(file_propt, "r", encoding="utf-8").read()).split("\n"))[index_of_list_keywords]
    text = file.split()
    if text[0] == "#KEYWORDS":
        return text[1].split(",")


def Frequency_matrix(matrix, item, procent = 0.90):
    count = 0
    for i in matrix:
        if is_word(item, i[0]) >= procent or is_word(item, i[1]) >= procent:
            count += 1
        else:
            pass
    return count / len(matrix)

def Min_frequency(dict_ : dict) -> float:
    min = 1
    for i in dict_:
        if dict_[i] < min:
            min = dict_[i]
        else:
            pass
    return min

def Find_matrix_row(matrix, item, procent = 0.90):
    arr = []
    for i in matrix:
        if is_word(item, i[0]) >= procent or is_word(item, i[1]) >= procent:
            return i
        else:
            pass
    return arr

def Text_to_matrix(text, words_per_line):
    words = text.split()
    matrix = []
    current_line = []
    
    if len(text) % words_per_line != 0:
        current_line.append("")

    for word in words:
        current_line.append(word)
        
        if len(current_line) == words_per_line:
            matrix.append(current_line)
            current_line = []
        
    return matrix

def Keywords(sentence) -> list:
    morph = pymorphy2.MorphAnalyzer()
    words = sentence.split()
    keywords = []
    for word in words:
        parsed_word = morph.parse(word)[0]
        if 'NOUN' in parsed_word.tag: #or 'ADJF' in parsed_word.tag:
            keywords.append(word)
    return keywords

def is_word(word_1 : str, word_2 : str) -> float:
    """на сколько 1 похоже на 2"""
    word_2 = list(word_2)
    if len(word_2) < 1:
        return 0
    count_repit_char = 0
    for i in word_1:
        try:
            if i == word_2[word_1.index(i)]:
                count_repit_char += 1
        except:
            break
    return count_repit_char / len(word_2)

def GetTokenInMessage(file : str, message : list, procent = 0.65) -> list:
    iner_data = []
    # создаём массив слов который использован для генерации текста. Для избежания бредогенератора из дата сета выберем только те текстовые данные которые используются для ответов на сообщения
    textdata = Read_.Read_.readAll(file)
    for q in textdata:
        count = 0
        for i in q.split():
            try:
                res = is_word(message[count], i.split()[count])# res = результат на сколько слово из сообщений похоже на слово в ключе
                if res > procent:
                    iner_data.append(textdata[q])
                    count += 1
            except:
                pass
    return iner_data

def GetRadialTokenInMessage(file : str, message : list, procent = 0.65, memory = 25) -> list:
    iner_data = []
    # создаём массив слов который использован для генерации текста. Для избежания бредогенератора из 
    # датасета выберем только те текстовые данные которые используются для ответов на сообщения
    textdata = Read_.Read_.readAll(file)
    for q in textdata:
        count = 0
        for i in q.split():
            try:
                res = is_word(message[count], i) + is_word(message[count - 1], i - 1)# res = результат на сколько слово из сообщений похоже на слово в ключе
                if count == 0:
                    if (res/2) > procent:
                        iner_data.append(textdata[q])
            except:
                print("GetRadialToken!!!!!")
            count += 1
    return iner_data


def GetTokenInMessageForText(file : str, message : list, procent = 0.65) -> list:
    iner_data = []
    # создаём массив слов который использован для генерации текста. Для избежания бредогенератора из датасета выберем только те текстовые данные которые используются для ответов на сообщения
    textdata = Read_.Read_.readAll(file)
    for q in textdata:
        count = 0
        for i in q.split():
            try:
                res = is_word(message[count], i)# res = результат на сколько слово из сообщений похоже на слово в ключе
                if res > procent:
                    iner_data.append(textdata[q])
                    count += 1
            except:
                pass
    return iner_data
