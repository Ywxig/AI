import discord
import CuteON
import Zoe

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == message.content:
            mes = (message.content).lower()
            mes_list = mes.split()
            await message.channel.send(Zoe.main(mes_list))

intents = discord.Intents.default()
client = MyClient(intents=intents)

print(CuteON.Get_.getLine("Config.sws", "token_Zoe"))
client.run(CuteON.Get_.getLine("Config.sws", "token_Zoe"))