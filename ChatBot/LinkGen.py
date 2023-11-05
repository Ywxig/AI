from . import WordOperations

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
            if WordOperations.is_word(j, "найди") >= 0.51:
                arr = message.split(j)
                respons = []
                for i in arr[1].split():
                    if i not in dont_use_words:
                        respons.append(i)       
                task = '%20'.join(respons)
                s = 'https://yandex.ru/yandsearch?clid=202826&text=' + task
                return s