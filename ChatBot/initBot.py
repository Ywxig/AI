from . import utils
from CuteON import Read_

def init(config : str) -> dict:
    config = Read_.Read_.readAll(config)

    BOT = {}

    BOT["Token"] = config["Token"]
    BOT["Version"] = config["Version"]
    BOT["OWM"] = config["OWM-API-key"]
    BOT["comand_prefix"] = config["comand_prefix"]

    About = {}
    About["Bio"] = open(config["AboutMe"], "r", encoding="utf-8").read()
    About["PlayIn"] = config["PlayIn"]

    BOT["About"] = About


    if config["Text"] != "":
        text = {}
        try:
            text["Contnet"] = Read_.Read_.readAll(config["Text"])
        except:
            text["Contnet"] = {}
        text["Len"] = len(open(config["Text"], "r", encoding="utf-8").read().split())
        text["Paph"] = config["Text"]
        text["Keywords"] = utils.Keywords(config["Text"])

    BOT["Dataset"] = text

    return BOT



