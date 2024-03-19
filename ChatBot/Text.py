from . import utils
from CuteON import Read_
import random
from . import LinkGen
import wikipedia
import time



def cord_word(text, word_find, float_pass = 0.52):
    count = 0
    for i in text:
        if  utils.is_word(i, word_find) >= float_pass:
            return count
        count += 1


def TextWiki(prompt = [],
             set_languadge = "ru",
             len_article = 8):
    text = []
    block = []
    wikipedia.set_lang(set_languadge)
    wiki_data = wikipedia.summary(prompt)
    wiki_page = wikipedia.page(prompt)

    keyWords =  utils.Keywords(wiki_data)
    keyWordsBucet = 0

    sentens = wiki_data.split(".")    
 
    for i in sentens:
        if keyWordsBucet >= len(keyWords):
            break
        else:
            item = i.split()
            for q in item:
                if q in keyWords:
                    text.append(i)
                    keyWordsBucet += 1
    
    arr = []

    for i in text:
        for j in i.split():
            if j not in arr:
                arr.append(j)
            else:
                pass

    print(len(wiki_data.split()) - len(" ".join(arr).split()))
    return " ".join(arr) + "\n" + "Узнать больше: " + str(wiki_page.url)


def TextCraft(message : list, file_dataset : str, iterabel_counts = 64):
    text = []
    iner_data = utils.GetTokenInMessage(file = file_dataset, message = message)
    str_ = ". ".join(iner_data).split()
    keyWords = utils.Keywords(". ".join(iner_data))

    for i in iner_data:
        item = i.split()
        for q in item:
            if q in keyWords:
                text.append(i)

    arr = []

    for i in text:
        for j in i.split():
            if j not in arr:
                arr.append(j)
            else:
                pass
    
    return " ".join(arr)




