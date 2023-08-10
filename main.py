import discord
from CuteON import Read_
from sends import main
from time import time

CONFIG = Read_.readAll("Config.sws")

class MyClient(discord.Client):
    async def on_ready(self):
        start = time()
        print("[Loading some bot...]")
        print("[Token] - " + CONFIG["Token"])
        print("[GitHub] - " + CONFIG["GitHub"])
        print("[PlayIn] - " + CONFIG["PlayIn"])
        print('Logged on as', self.user)
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Загрузка систем..."))
        await client.change_presence(status=discord.Status.online, activity=discord.Game(CONFIG["PlayIn"] ))
        print('[Time logged is] - ' + str(time() - start))
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
                await message.channel.send(main(mes_list, message.author))
                
intents = discord.Intents.all()
client = MyClient(intents=intents)

print(CONFIG["Token"])
client.run(str(CONFIG["Token"]))
