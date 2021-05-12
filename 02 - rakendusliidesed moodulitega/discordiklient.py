import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
        print(message.author, message.channel, message.content)
        
        if message.content.lower() == "reacti sellele":
            await message.add_reaction("\U0001F525")

        if message.content == 'ping' and message.channel.name == "tund":
            print("Sending pong")
            await message.channel.send('pong')
        
        if message.content.startswith("tee kanal "):
            new_channel_name = message.content[10:]
            await message.guild.create_text_channel(new_channel_name)


client = MyClient()
client.run("sinutoken")
