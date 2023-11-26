import discord
from CuteON import Read_
from sends import main
from time import time
from ChatBot import initBot

BOT = initBot.init("Config.sws")

class MyClient(discord.Client):
    async def on_ready(self):
        start = time()
        print("[Loading some bot...]")
        print("[Token] - " + BOT["Token"])
        print("[PlayIn] - " + BOT["About"]["PlayIn"])
        print('Logged on as', self.user)
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Загрузка систем..."))
        await client.change_presence(status=discord.Status.online, activity=discord.Game(BOT["About"]["PlayIn"] ))
        print('[Time logged is] - ' + str(time() - start))
    async def on_message(self, message):

        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content == message.content:
            if message.content[0] == BOT["comand_prefix"]:
                if message.content == '.cls':
                    channel = message.channel
                    messages = channel.history()
                    await message.channel.send("Конечно, сейчас очищю!")
                    async for message in messages:
                        await message.delete()

            #try:
                mes = (message.content).lower()
                mes_list = mes.split()
                channel = message.channel
                mess = message.content
                await message.channel.send(main(mes_list, message.author))
                
intents = discord.Intents.all()
client = MyClient(intents=intents)

print(BOT["Token"])
client.run(str(BOT["Token"]))
