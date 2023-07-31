import discord
import CuteON
import sends
import ChatBot
import time
import CMFIO



modul_list = ["discord", "CuteON", "sends", "ChatBot", "time", "Command_runer"]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Загрузка систем..."))
        print("Добро пожаловать, Загрузка систем...")
        time.sleep(2)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Ассиастент" + CuteON.Get_.getLine("Config.sws", "Version")))
    async def on_message(self, message):

        if message.content == '.cls':
            channel = message.channel
            messages = channel.history()
            await message.channel.send("Конечно, сейчас очищю!")
            async for message in messages:
                await message.delete()


        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content == message.content:
            #try:
                mes = (message.content).lower()
                mes_list = mes.split()
                channel = message.channel
                mess = message.content
                await message.channel.send(sends.main(mes_list))
                for i in mes_list:
                    if ChatBot.is_word("расписание", i) >= 0.78:
                        CMFIO.Compilator.comp(CuteON.Get_.getAll("template/Defolt/CFG.sws"), "Defolt/main.html", "card.html")
                        await message.channel.send(content ='Карточька на сегоднешний день', file=discord.File("card.html"))
                        return " "

                    if mes_list[0] == ".version":
                        await message.channel.send("Алгоритм генерации `" + CuteON.Get_.getLine("Config.sws", "Alghoritm") + "`")
                        await message.channel.send("Версия бота `" + CuteON.Get_.getLine("Config.sws", "Version") + "`")
                        await message.channel.send("Используемые модули `" + str(modul_list) + "`")
                        await message.channel.send("Поисковая система `" + CuteON.Get_.getLine("Config.sws", "Searcher") + "`")
                        await message.channel.send("Метео служба `" + CuteON.Get_.getLine("Config.sws", "Wather") + "`")
                        await message.channel.send("Доступые команды `" + CuteON.Get_.getLine("Config.sws", "Commands") + "`")
                        await message.channel.send("Используемый датасет `" + CuteON.Get_.getLine("Config.sws", "Text") + "`")
                        return " "
            
                    if mes_list[0] == ".doc":
                        await message.channel.send(content ='Фаил с документацией', file=discord.File("Doc/doc.html"))
                        return " "
            
                    if mes_list[0] == ".text":
                        await message.channel.send(content ='Фаил с текстом для генератора сообщений', file=discord.File("education/text.txt"))
                        return " "
                    
                    if mes_list[0] == ".help":
                        await message.channel.send(content ='Хороший вопрос, думаю стоит почитать документацию, пропадёт ощющение что я загадка', file=discord.File("Doc/doc.html"))
                        return " "

                    if mes_list[0] == ".is_word":
                        
                        await message.channel.send("слово: " + mes_list[1] + " похоже на  слово: " + mes_list[2] + " с процентом: " + str(ChatBot.is_word(mes_list[1], mes_list[2])))
                        return " "
                    
                    if mes_list[0] == ".test":
                        await message.channel.send("Тест систем...")
                        try:
                            if ChatBot.Generator:
                                print("[ChatBot] - OK")
                                print(CuteON.Get_.getAll("Config.sws"))
                                open("education/BaseData.sws").read()
                                open("education/text.txt").read()
                                open("education/hybrid.txt").read()
                            else:
                                await message.channel.send("Тест провален, генератор не определён похоже, что вы используете старую версию фала ChatBot.py!!!")
                        except:
                            await message.channel.send("Тест провален, проверте папки или файлы на предмет правельность наименования!")
                        await message.channel.send("Тест завершён, ошибок нет файлы на местах, классы определены правельно!")
                        return " "

                
intents = discord.Intents.all()
client = MyClient(intents=intents)

print(CuteON.Get_.getLine(file="Config.sws", nameString="Token"))
client.run(str(CuteON.Get_.getLine(file="Config.sws", nameString="Token")))
