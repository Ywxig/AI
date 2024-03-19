import discord
from CuteON import Read_
from sends import main
from time import time
from ChatBot import initBot

BOT = initBot.init("Config.sws")
CMD = Read_.Read_.readAll("Comands.sws")

class MyClient(discord.Client):
    async def on_ready(self):
        start = time()
        print("[Token] - " + BOT["Token"])
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Загрузка систем..."))
        await client.change_presence(status=discord.Status.online, activity=discord.Game(BOT["About"]["PlayIn"] ))
        print('[Time logged is] - ' + str(time() - start))
    async def on_message(self, message):

        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == message.content:
            mes = (message.content).lower()
            mes_list = mes.split()

            if mes_list[0] == '.cls':
                channel = message.channel
                messages = channel.history()
                await message.channel.send("Конечно, сейчас очищю!")
                async for message in messages:
                    await message.delete()

            if mes_list[0] == '.echo':
                del mes_list[0]
                await message.channel.send(" ".join(mes_list))

            if mes_list[0] == '.help':
                await message.channel.send(CMD[mes_list[1]])

            channel = message.channel
            mess = message.content
            if bool(BOT["use_triger"]) == True and mes_list[0] in BOT["triger"]:
                del mes_list[0]
                await message.channel.send(main(mes_list, message.author, BOT))
            if BOT["use_triger"] == False:
                await message.channel.send(main(mes_list, message.author, BOT))
                
intents = discord.Intents.all()
client = MyClient(intents=intents)

client.run(str(BOT["Token"]))
