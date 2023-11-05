from . import WordOperations
from CuteON import Read_
import random
from . import LinkGen
import wikipedia
import time

def cord_word(text, word_find, float_pass = 0.52):
    count = 0
    for i in text:
        if  WordOperations.is_word(i, word_find) >= float_pass:
            return count
        count += 1


def Text(message, prompt,
    chance_choosing_full_pair=0.59,
    chance_choosing_main_word=0.4,
    chance_teleport = 0.1,
    chance_use_message = 0.45,
    chance_use_next_word = 0.42,
    match_percentage = 0.78,
    Probability_descent_for_use_message = 0.06,
    max_size_respons = 5,
    min_word_in_pair = 2,
    max_word_in_pair = 5,
    list_wiki_call = ["расскажи", "как"],
    set_languadge = "ru",
    dont_use_words = ["None"],
    reqest_is_empty = ["...", "Ага", "Окей"],
    file_for_hybrid = "hybrid.txt",
    file_mode = True,
    filter_comma_in_end = True,
    use_sentens_to_keywords = False,
    add_random_sentens = False,
    adaptive_respons_size = False,
    hybrid_generation = True):
    wiki_data = None
    t1 = time.time()
    result = []
    try:
        for i in message.split():
            for q in list_wiki_call:
                if  WordOperations.is_word(i, q) >= 0.6:
                    ms = (message.split(i)[1]).split(".")[0]
                    wikipedia.set_lang(set_languadge)
                    wiki_data = wikipedia.summary(ms)
                    wiki_page = wikipedia.page(ms)
    except:
        wiki_data = None
    # если гиблиднасть включена, то алгоритм сверяет сообщение с тем что есть в базе если есть совпадение то с 0.5 шансом добавим в начало списка result
    if hybrid_generation == True:
        r = round(random.random())
        content = Read_.readAll(file_for_hybrid)
        for i in content:
            if  WordOperations.is_word(message, i) >= match_percentage:
                try:
                    ctx = content[i].split("||")
                    return random.choice(ctx)
                except:
                    return content[i]             
    Key_word = WordOperations.Keywords(message) + WordOperations.Keywords(prompt)
    if file_mode == True:
        text = (open(prompt, "r", encoding="utf-8").read()).split()
    else:
        text = prompt.split()
    iner_propt = " ".join(text)
    # использовать ли только те предложения где есть ключевыне слова !ИМЕННО ПРЕДЛОЖЕНИЯ А НЕ АБЗАЦИ!
    if use_sentens_to_keywords == True:
        new_text = []
        ctx = iner_propt.split(".")
        count_iterable = 0
        for i in ctx:
            for j in i.split():
                if j in WordOperations.get_prompt_key_words(prompt) + list(Key_word):
                    if add_random_sentens == True:
                        new_text.append(i)
                        new_text.append(random.choice(ctx))
                    else:
                        new_text.append(i)
            count_iterable += 1
        text = (". ".join(new_text)).split()
    arr = [] # промежуточьный массив, куда вводятся все слова и пары
    # Далие алгоритм который разабьёт текст на пары слов и недастоющее слово заменит на None
    matrix = []
    iterable = min_word_in_pair
    for i in range(0, len(text), iterable):
        iterable = random.randint(min_word_in_pair, max_word_in_pair)
        if i+1 < len(text):
            for item in range(iterable):
                try:
                    matrix.append([text[i+item]])
                except:
                    matrix.append([text[i]])
        else:
            for item in range(iterable):
                matrix.append('None')
    # Используя параметры и генерацию случайных чисел генерируем сообщение с размеров в загружанный текст
    for i in matrix:
        random_cofficient1 = random.random()
        random_cofficient2 = random.random()
        if random_cofficient1 <= chance_choosing_main_word:
            arr.append(i[0])
        if random_cofficient2 <= chance_choosing_full_pair:
            arr.append(" ".join(i))
    # Очищаем полученный текст от артифактов
    respons = (" ".join(arr)).split()
    sentens = []
    for i in respons:
        if WordOperations.Frequency(text, i) <= match_percentage:
            sentens.append(i)
    # Использование адоптивного размера результата
    if adaptive_respons_size == True:
        try:
            max_size_respons = len(message.split()) + random.randint(1, len(message.split()))
        except:
            return "[Ошибка!] использование адоптивного режима подрузомивает использование сообщения, но вы не передали сообщение!"
    # Проходимся по финальному тексту и отсикаем лишнее
    count = 0
    if wiki_data != None:
        max_size_respons = 50
    else:
        pass
    for i in range(max_size_respons):
        random_cofficient1 = random.random()
        random_cofficient2 = random.random()
        random_cofficient3 = random.random()
        if random_cofficient2 <= chance_use_message + count and len(Key_word) != 0:
            random_key_word = random.choice(Key_word)
            sentens.append(random_key_word)
            # Далия добавим слово которое идёт после слово которое мы взяли из сообщения
            if random_cofficient3 <= chance_use_next_word:
                for j in text:
                    if  WordOperations.is_word(j, random_key_word) <= match_percentage:
                        try:
                            sentens.append(text[cord_word(text, random_key_word)+1])
                        except:
                            pass
                        break
            count += Probability_descent_for_use_message
            del Key_word[Key_word.index(random_key_word)]
        if random_cofficient1 <= chance_teleport:
            try:
                sentens.append(respons[i + round(max_size_respons / 2)])
            except:
                pass
        else:
            try:
                sentens.append(respons[i])
            except:
                pass
    count = 0
    if filter_comma_in_end == True and sentens != []:
        some_word = list(sentens[len(sentens)-1])
        for i in sentens[len(sentens)-1]:
            if i in [",", ";"]:
                del some_word[len(some_word)-1]
                fin = "".join(some_word)
                del sentens[len(sentens)-1]
                sentens.append(fin)
                break
    try:
        respons = wiki_data.split()
    except:
        respons = []
    # Финальная очистка ответа от повторяющехся слов
    for i in sentens:
        if i not in respons and i not in dont_use_words:
            respons.append(i)
    if len(respons) > 8:
        for _ in range(random.randint(3, 6)):
            del respons[0]
    for i in range(max_size_respons):
        try:
            result.append(respons[i])
        except:
            pass
    if wiki_data != None:
        end_message = ". Больше узнать по теме:\n" + wiki_page.url
    else:
        end_message = ""
    reqest = " ".join(result) + end_message
    if reqest is None:
        return random.choice(reqest_is_empty)
    else:
        return reqest
def Marcov(  text : str,
                    message,
                    order=1,
                    length=5,
                     ):
    keywords = WordOperations.Keywords(message)
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