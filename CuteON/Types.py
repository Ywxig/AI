type_str_action = ("str", "url", "file")
type_int_action = ("int")
type_list_action = ("list", "rgb", "rgba", "diolog", "matrix")
type_float_action = ("float")
WebFile = ('html', 'css', 'js')
coment = ("//", "№")

class Types_:

    class List:

        def toInt(list_):
            try:
                list_ = list_.split(",")
            except:
                pass
            arr = []
            for i in list_:
                arr.append(int(i))
            print(arr)
            return arr

    def toIntVec(list_):
        try:
            list_ = list_.split(",")
        except:
            pass
        arr = []
        for i in range(2):
            arr.append(int(i))
        return arr

    class Color:
        def subtraction(Color_vector1 : list, Color_vector2 : list) -> list:
            Color_vector = []
            for color in range(3):
                rezalt_color = Color_vector1[color] - Color_vector2[color]
                if rezalt_color < 0:
                    Color_vector.append(0)
                if rezalt_color > 255:
                    Color_vector.append(255)
                else:
                    Color_vector.append(rezalt_color)
            return Color_vector