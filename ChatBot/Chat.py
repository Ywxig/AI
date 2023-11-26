from . import utils
from CuteON import Read_
import random

def GetTokenInMessage(file : str, message : list, procent = 0.65) -> list:
    iner_data = []
    # создаём массив слов который использован для генерации текста. Для избежания бредогенератора из дата сета выберем только те текстовые данные которые используются для ответов на сообщения
    textdata = Read_.Read_.readAll(file)
    for q in textdata:
        count = 0
        for i in q.split():
            try:
                res = utils.is_word(message[count], i.split()[count])# res = результат на сколько слово из сообщений похоже на слово в ключе
                if res > procent:
                    iner_data.append(textdata[q])
                    count += 1
            except:
                pass
    return iner_data


def ChatCraft(message : list, file_dataset : str, iterabel_counts = 64):
    text = []
    iner_data = GetTokenInMessage(file = file_dataset, message = message)
            
    # Рассмотрим маасив текстовых данных как один текст. Создаём матрицу из текста и проверяем насколько пары слов из матрици всречаются на протежениие всего текста
    str_ = ". ".join(iner_data).split()
    matrix = utils.Text_to_matrix(". ".join(iner_data), 2)
    chain_matrix_material = {}
    for i in str_:
        Freq = utils.Frequency_matrix(matrix, i, procent=0.75)
        chain_matrix_material[i] = Freq
    keywords = utils.Keywords(". ".join(iner_data))
    if keywords == []:
        text.append(random.choice(str_))
    else:
        text.append(random.choice(keywords))
    # Повторяемый кусок кода повторяется "iterabel_counts" раз. Проверяем какая вероятность встретить последний элемент в тексте для генерации, генерируем случайное число если число <
    for i in range(iterabel_counts):
        last_item_text = text[len(text)-1]
        if "." in list(last_item_text):
            break
        rand = random.random()
        rand2 = round(random.random())
        if last_item_text != "":
            try:
                if rand2 > 0 and i < 3:
                    arr = utils.Find_matrix_row(matrix, last_item_text, procent=0.65)
                    for j in matrix[matrix.index(arr) + 1]:
                        text.append(j)
                if rand <= chain_matrix_material[last_item_text]:
                    arr = [utils.Find_matrix_row(matrix, last_item_text, procent=0.65)]
                    for q in arr:
                        for j in q:
                            if j not in text:
                                text.append(j)
            except:
                pass
    return " ".join(text)