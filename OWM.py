from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


def Air():
    owm = OWM('88c77e859289463928b17b24f2f7ea99')
    mgr = owm.weather_manager()
    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place('Молдова')
    w = observation.weather
    w2 = w.temperature('celsius')['temp']
    print(w)

def Status():
    owm = OWM('88c77e859289463928b17b24f2f7ea99')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Молдова')
    w = observation.weather
    w2 = w.temperature('celsius')['temp']
    print(w)
    print(w2)
    return "В даный момент " + str(w.status)
        
def Temp():
    owm = OWM('88c77e859289463928b17b24f2f7ea99')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Молдова')
    w = observation.weather
    w2 = w.temperature('celsius')['temp']
    print(w)
    print(w2)
    return "В даный момент " + str(w.temperature('celsius')['temp']) + '°'
        
def All():
    owm = OWM('88c77e859289463928b17b24f2f7ea99')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Молдова')
    w = observation.weather
    w2 = w.temperature('celsius')['temp']
    print(w)
    print(w2)
    return "В даный момент температура " + str(w.temperature('celsius')['temp']) + '°' + '\n' + "В даный момент статус " + str(w.status) + '\n' + "В даный момент скорость ветра " + str(w.wind()['speed'])  + 'm/s' + '\n' + "В даный момент влажность " + str(w.humidity)+ '%'

def Wther():
    owm = OWM('88c77e859289463928b17b24f2f7ea99')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place('Молдова')
    w = observation.weather
    w2 = w.temperature('celsius')['temp']
    print(w)
    print(w2)
    return "В даный момент " + str(w.humidity)+ '%'