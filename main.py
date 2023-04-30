import discord
import CuteON
import sends
import Zoe
import BotHubAPI
import time

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Загрузка систем..."))
        print("Добро пожаловать, Загрузка систем...")
        time.sleep(2)
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Ассиастент Zoe 5.4"))
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content == message.content:
            mes = (message.content).lower()
            mes_list = mes.split()
            try:
                await message.channel.send((Zoe.return_commad(mes_list)))
            except:
                print("ERR IN 'await message.channel.send((Zoe.return_commad(mes_list)))' ")

            try:
                await message.channel.send(sends.main(mes_list))       
            except:
                print("ERR IN 'await message.channel.send(sends.main(mes_list))' ")
                Zoe.Generator.Markov(mes)

        if message.content.startswith('.cls'):
            channel = message.channel
            messages = channel.history()
            await message.channel.send("Конечно, сейчас очищю!")
            async for message in messages:
                await message.delete()
                
intents = discord.Intents.all()
client = MyClient(intents=intents)

print(CuteON.Get_.getLine(file="Config.sws", nameString="token_Zoe"))
client.run(str(CuteON.Get_.getLine(file="Config.sws", nameString="token_Zoe")))

"""
print(BotHubAPI.Config.Get(name="Zoe"))
client.run(BotHubAPI.Config.Get(name="Zoe"))
"""

"""
client.run("ODU0MjQ3MDk2Mzg2NDUzNTA0.GI-hsg.FUBJTFoT1WLITT423g3W98CJ5KjDRP0XtGrJuA")
"""