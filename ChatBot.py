import random
import wikipedia
import time
from CuteON import Read_
import pymorphy2

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
        if WordsOperations.is_word(item, i[0]) >= procent or WordsOperations.is_word(item, i[1]) >= procent:
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
        if WordsOperations.is_word(item, i[0]) >= procent or WordsOperations.is_word(item, i[1]) >= procent:
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

class WordsOperations():

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

        return count_repit_char / len(list(word_2))

class Tokens():

    def GetTokenInMessage(file : str, message : list, procent = 0.65) -> list:
        iner_data = []
        # создаём массив слов который использован для генерации текста. Для избежания бредогенератора из дата сета выберем только те текстовые данные которые используются для ответов на сообщения
        textdata = Read_.readAll(file)
        for q in textdata:
            count = 0
            for i in q.split():
                try:
                    res = WordsOperations.is_word(message[count], i.split()[count])# res = результат на сколько слово из сообщений похоже на слово в ключе
                    if res > procent:
                        iner_data.append(textdata[q])
                        count += 1
                except:
                    pass
        return iner_data

class Search:

    def Youtube(List):
        message = " ".join(List)
        dont_use_words = ["найди", "ютуб"]
        arr = message.split("найди")
        respons = []
        for i in arr[1].split():
            if i not in dont_use_words:
                respons.append(i)

        task = '+'.join(respons)
        s = 'https://www.youtube.com/results?search_query=' + task
        return s

    def Yandex( List ):
        message = " ".join(List)
        dont_use_words = ["найди", "яндекс", "найти", "отыскать"]
        for j in List:
            if WordsOperations.is_word(j, "найди") >= 0.51:
                arr = message.split(j)
                respons = []
                for i in arr[1].split():
                    if i not in dont_use_words:
                        respons.append(i)       
                task = '%20'.join(respons)
                s = 'https://yandex.ru/yandsearch?clid=202826&text=' + task
                return s
    

def cord_word(text, word_find, float_pass = 0.52):
    count = 0
    for i in text:
        if WordsOperations.is_word(i, word_find) >= float_pass:
            return count
        count += 1

class Generator:

    class Chat:

        def ChatCraft(message : list, file_dataset : str, iterabel_counts = 64):
            text = []

            iner_data = Tokens.GetTokenInMessage(file = file_dataset, message = message)
                    
            # Рассмотрим маасив текстовых данных как один текст. Создаём матрицу из текста и проверяем насколько пары слов из матрици всречаются на протежениие всего текста
            str_ = ". ".join(iner_data).split()
            matrix = Text_to_matrix(". ".join(iner_data), 2)
            chain_matrix_material = {}
            for i in str_:
                Freq = Frequency_matrix(matrix, i, procent=0.75)
                chain_matrix_material[i] = Freq
            keywords = WordsOperations.Keywords(". ".join(iner_data))
            if keywords == []:
                text.append(random.choice(str_))
            else:
                text.append(random.choice(keywords))

            # Повторяемый кусок кода повторяется "iterabel_counts" раз. Проверяем какая вероятность встретить последний элемент в тексте для генерации, генерируем случайное число если число <= последнему чеслу то добовляем то слово из пары которого нет в генерируемом ответе
            for i in range(iterabel_counts):
                last_item_text = text[len(text)-1]
                if "." in list(last_item_text):
                    break
                rand = random.random()
                rand2 = round(random.random())
                if last_item_text != "":
                    try:
                        if rand2 > 0:
                            arr = Find_matrix_row(matrix, last_item_text, procent=0.65)
                            for j in matrix[matrix.index(arr) + 1]:
                                text.append(j)

                        if rand <= chain_matrix_material[last_item_text]:
                            arr = [Find_matrix_row(matrix, last_item_text, procent=0.65)]
                            for q in arr:
                                for j in q:
                                    if j not in text:
                                        text.append(j)
                    except:
                        pass
            return " ".join(text)
                    


    class Text:
            

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
                        if WordsOperations.is_word(i, q) >= 0.6:

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
                    if WordsOperations.is_word(message, i) >= match_percentage:
                        try:
                            ctx = content[i].split("||")
                            return random.choice(ctx)
                        except:
                            return content[i]             

            Key_word = WordsOperations.Keywords(message) + WordsOperations.Keywords(prompt)
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
                        if j in get_prompt_key_words(prompt) + list(Key_word):
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
                if Frequency(text, i) <= match_percentage:
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
                            if WordsOperations.is_word(j, random_key_word) <= match_percentage:
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
            keywords = WordsOperations.Keywords(message)
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

            return str(" ".join(arr).split(".")[0])