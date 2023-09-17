
import random
import time
import pymorphy2
from CuteON import Read_
import wikipedia

def cord_word(text, word_find, float_pass = 0.52):
    count = 0
    for i in text:
        if is_word(i, word_find) >= float_pass:
            return count
        count += 1

def Frequency(arr, item):
    count = 0
    for i in arr:
        if item == i:
            count += 1
        else:
            pass
    return count / len(arr)

def Text_to_matrix(text, words_per_line):
    words = text.split()
    matrix = []
    current_line = []
    
    for word in words:
        current_line.append(word)
        
        if len(current_line) == words_per_line:
            matrix.append(current_line)
            current_line = []

    if current_line:
        matrix.append(current_line)

    return matrix

def Keywords(sentence):
    morph = pymorphy2.MorphAnalyzer()
    words = sentence.split()
    keywords = []
    for word in words:
        parsed_word = morph.parse(word)[0]
        if 'NOUN' in parsed_word.tag or 'ADJF' in parsed_word.tag:
            keywords.append(parsed_word.normal_form)
    return keywords

def get_prompt_key_words(file_propt, index_of_list_keywords=0):
    file = ((open(file_propt, "r", encoding="utf-8").read()).split("\n"))[index_of_list_keywords]
    text = file.split()
    if text[0] == "#KEYWORDS":
        return text[1].split(",")
    
def is_word(word_1, word_2):
    """на сколько 1 похоже на 2"""
    word_2 = list(word_2)
    count_repit_char = 0
    for i in word_1:
        try:
            if i == word_2[word_1.index(i)]:
                count_repit_char += 1
        except:
            break

    return count_repit_char / len(list(word_2))

def caht_gigachat_001(message : list, file_dataset : str, len_generation_max = 55):
    textdata = Read_.readAll(file_dataset)
    
    iner_data = []

    # создаём массив значений для генерации текста
    for q in textdata:
        count = 0
        for i in q.split():
            try:
                res = is_word(message[count], i.split()[count])# res = результат на сколько слово из сообщений похоже на слово в ключе
                if res > 0.65:
                    iner_data.append(textdata[q])
                    count += 1
            except:
                pass

    # слово которое самое часто встречающаеся в тексте добовляем как первое
    text = []
    word_dict = {}
    PREP = ''
    for i in iner_data:
        morph = pymorphy2.MorphAnalyzer()
        words = i.split()
        NOUN = ''
        ADJF = ''

        for word in words:
            
            parsed_word = morph.parse(word)[0]
            if 'NOUN' in parsed_word.tag:
                NOUN = word

            if "ADJF" in parsed_word.tag or "ADVB" in parsed_word.tag or "VERB" in parsed_word.tag:
                ADJF = word

            if "PREP" in parsed_word.tag:
                PREP = word             
        word_dict[NOUN] = ADJF

    count = 0
    while count < len_generation_max:
        try:
            sentens = random.choice(iner_data)
            if sentens.split()[count] not in text and sentens.split()[count] in word_dict:
                text.append(sentens.split()[count])
                if PREP in sentens.split():
                    text.append(PREP)
                text.append(word_dict[sentens.split()[count]])
            count += 1
        except:
            break

    return " ".join(text)
        


while True:
    message = input("<User:> ")
    print( "<User:Zoe5.6>" + str(caht_gigachat_001(message=message.split(), file_dataset="text.txt")))
