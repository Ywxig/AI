import random
import pymorphy2

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

import os

import time

def ShootDown():
    os.system("shutdown -h")

class App:
    cfg = "app_cfg_file.txt"

    def creat():
        open(App.cfg, "w", encoding="utf-8").write("")
        

    def open(app_name):    
        app_paph = open(App.cfg, "r", encoding="utf-8").read().split("\n")
        for i in app_paph:
            if is_word(app_name, i.split("<>")[0]) >= 0.58:
                os.startfile(i.split("<>")[1])
                return  "Запускаю преложение `"+ i.split("<>")[1] +"` ожидайте..."
        return "ой... Похоже что приложение не найдено"

class Water_sys:
    def Air(self):
        owm = OWM('88c77e859289463928b17b24f2f7ea99')
        mgr = owm.weather_manager()
        # Search for current weather in London (Great Britain) and get details
        observation = mgr.weather_at_place('Молдова')
        w = observation.weather
        w2 = w.temperature('celsius')['temp']
        print(w)

    def Status(self):
        owm = OWM('88c77e859289463928b17b24f2f7ea99')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place('Молдова')
        w = observation.weather
        w2 = w.temperature('celsius')['temp']
        print(w)
        print(w2)
        return "В даный момент " + str(w.status)

    def Temp(self):
        owm = OWM('88c77e859289463928b17b24f2f7ea99')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place('Молдова')
        w = observation.weather
        w2 = w.temperature('celsius')['temp']
        print(w)
        print(w2)
        return "В даный момент " + str(w.temperature('celsius')['temp']) + '°'

    def All(self):
        owm = OWM('88c77e859289463928b17b24f2f7ea99')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place('Молдова')
        w = observation.weather
        w2 = w.temperature('celsius')['temp']
        print(w)
        print(w2)
        return "В даный момент температура " + str(w.temperature('celsius')['temp']) + '°' + '\n' + "В даный момент статус " + str(w.status) + '\n' + "В даный момент скорость ветра " + str(w.wind()['speed'])  + 'm/s' + '\n' + "В даный момент влажность " + str(w.humidity)+ '%'

    def Wther(self):
        owm = OWM('88c77e859289463928b17b24f2f7ea99')
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place('Молдова')
        w = observation.weather
        w2 = w.temperature('celsius')['temp']
        print(w)
        print(w2)
        return "В даный момент " + str(w.humidity)+ '%'

def Keywords(sentence):
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
            if is_word(j, "найди") >= 0.51:
                arr = message.split(j)
                respons = []
                for i in arr[1].split():
                    if i not in dont_use_words:
                        respons.append(i)       
                task = '%20'.join(respons)
                s = 'https://yandex.ru/yandsearch?clid=202826&text=' + task
                return s
    
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
    
def is_word(word_exemple, word_find):
    if len(list(word_exemple)) < 2:
        return 0
    word_find = list(word_find)
    count_repit_char = 1
    for i in word_exemple:
        try:
            if i == word_find[word_exemple.index(i)]:
                count_repit_char += 1
        except:
            pass

    return count_repit_char / len(list(word_exemple))

def is_sentens(sentens_1, sentens_2):
    ctx = sentens_1.split()
    count = 0
    for i in ctx:
        try:
            if is_word(sentens_2.split()[sentens_2.split().index(i)], i) > 0.5:
                count += 1
        except:
            pass
        return count * 2 / len(ctx[0])

def cord_word(text, word_find, float_pass = 0.52):
    count = 0
    for i in text:
        if is_word(i, word_find) >= float_pass:
            return count
        count += 1

class Generator:    
    
    def wandering_drunk_modified(message, prompt, 
            chance_choosing_full_pair=0.59,
            chance_choosing_main_word=0.4,
            chance_teleport = 0.1,
            chance_use_message = 0.45,
            chance_use_next_word = 0.42,
            match_percentage = 0.78,
            chance_add_to_banlist = 0.5,
            Probability_descent_for_use_message = 0.06,
            max_size_respons = 5,
            allowed_array_length = 16,
            min_word_in_pair = 2,
            max_word_in_pair = 5,
            dont_use_words = ["—", "None", "#KEYWORDS"],
            file_for_hybrid = "hybrid.txt",
            file_mode = True,
            no_pretexts_in_end_respons = True,
            filter_comma_in_end = True,
            use_sentens_to_keywords = False,
            add_random_sentens = False,
            adaptive_respons_size = False,
            hybrid_generation = True,
            no_repeat_wotrd_in_respons = True):

        """
            chance_choosing_full_pair - шанс выбора всей пары а не только конкретного слова
            chance_choosing_main_word - шанс выбора главного слова или первого
            chance_teleport - шанс телепорта или прыжка на дельту растояния сообщения плюс индекс слова из итерации
            chance_use_message - шанс использования случайного слова из сообщения
            chance_use_next_word - шанс использования следующего слова после слова которое выброли из сообщения если данное слово есть в тексте
            match_percentage - процент совпаднения слова, если слово меньше чем данный коэффициент то слово не считается нужным
            chance_add_to_banlist - С каим шансом слова из респонса попадёт в список не используемых слов
            Probability_descent_for_use_message - шаг, прибовля который будет уменьшатся вероятность использования сообщения
            max_size_respons - максимальный размер ответа
            allowed_array_length - Если величина не использумого массива будет больше то обнулится до стандартного значения
            dont_use_words - Слова которые нельзя использовать, алгоритм при финальной коректировке избавится от них
            file_for_hybrid - Фаил в котором находятся варианты ответа на сообщения
            file_mode - рижим чтения промпта из файла
            no_pretexts_in_end_respons - удоление предлога из конца предложения
            filter_comma_in_end - удоление запетой у последнего слова
            use_sentens_to_keywords - использовать ли алгоритму предложения с ключевыми словами в промпте, важно чтобы при этом был включён режим чтения файла
            add_random_sentens = Добавить ли в конец внутреннего промпта случайное предложение
            adaptive_respons_size - Адоптивный размер респонса алгоритма, если он актевирован то алгоритм будет генерировать ответ который будет по размеру похожий на сообщения пользователя
            hybrid_generation - Использовать ли гибридную генерацию текста
            no_repeat_wotrd_in_respons - добавлять ли слова в список не используемых слов

            #KEYWORDS - используется в самом промпте
            данный параметр поббирается вами а не
            алгоритмом. Прошу помнить что вы должни
            фильтровать текст который в используете

        """
        t1 = time.time()
        print(t1)
        result = []
        # если гиблиднасть включена, то алгоритм сверяет сообщение с тем что есть в базе если есть совпадение то с 0.5 шансом добавим в начало списка result
        if hybrid_generation == True:
            r = round(random.random())
            content = open(file_for_hybrid, "r", encoding="utf-8").read().split("\n")
            for i in content:
                ctx = i.split(":")

                if is_sentens(ctx[0], message) > 0.9:
                    part_ctx = ctx[1].split("||")
                    if len(part_ctx) > 1:
                        for j in part_ctx[random.randint(0, len(part_ctx) - 1)].split():
                            result.append(j)
                    else:
                        for j in ctx[1].split():
                            result.append(j)  

                if len(message.split()) < 2 and r == 0 and is_word(ctx[0], message) >= 0.62:
                    part_ctx = ctx[1].split("||")
                    return part_ctx[random.randint(0, len(part_ctx) - 1)]

                if len(message.split()) < 2 and is_word(ctx[0], message) >= 0.62 and r == 1:
                    part_ctx = ctx[1].split("||")
                    if len(part_ctx) > 1:
                        for j in part_ctx[random.randint(0, len(part_ctx) - 1)].split():
                            result.append(j)
                    else:
                        for j in ctx[1].split():
                            result.append(j)  
                 

        sum_of_parameters = chance_choosing_full_pair + chance_choosing_main_word
        Key_word = Keywords(message) + Keywords(prompt)

        if sum_of_parameters >= 1.0:
            return "[Ошибка!] значения параметров больше допустимого предела пожалуста уменьшите их! сумма всех пораметров должнабыть '1.0'! Сейчас сумма = " + str(sum_of_parameters)

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
                        if is_word(j, random_key_word) <= match_percentage:
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
        
        respons = []

        # Финальная очистка ответа от повторяющехся слов
        for i in sentens:
            if i not in respons and i not in dont_use_words:
                respons.append(i)
        
        if no_repeat_wotrd_in_respons is True:
            
            for i in respons:
                if random.random() <= chance_add_to_banlist:
                    dont_use_words.append(i)
                if len(dont_use_words) > allowed_array_length:
                    dont_use_words = ["—", "None", "#KEYWORDS"]

        if len(respons) > 8:
            for _ in range(random.randint(3, 6)):
                del respons[0]

        for i in range(max_size_respons):
            try:
                result.append(respons[i])
            except:
                pass

        try:
            if no_pretexts_in_end_respons == True and len(result[len(result)-1]) <= 3:
                del result[len(result)-1]
        except:
            pass
        print(dont_use_words)
        print( str(time.time() - t1) + " - Время выполнения алгоритма")
        return " ".join(result)


    def generate_text(  text : str,
                        message,
                        order=1,
                        length=5,
                         ):
        keywords = Keywords(message)
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
    

    def random_text(text, message):
        arr = []
        states = text.split()
        key_word = Keywords(message)
        random_word = []
        for i in states:
            for _ in range(1):
                random_word.append(random.choice(key_word))

            random_gen = random.choice(states)

            if i != random_gen and Frequency(states, i) >= 0.02:
                arr.append(random_gen)
                try:
                    Intermediate = []
                    Intermediate.append(states[states.index(random_gen) + 1])
                    Intermediate.append(states[states.index(random_gen) - 1])

                    for _ in Intermediate:
                        if Frequency(states, Intermediate) >= 0.02:
                            arr.append(_)
                except:
                    pass
            count = 0
            delete_word=[]

        for i in arr:
            if i == arr[count] and i in delete_word:
                del arr[count] 
            else:
                delete_word.append(arr[count])
                count += 1
        delete_word=[]

        return str(" ".join(arr).split(".")[0])