import discord
import os

client = discord.Client()


@client.event
async def on_ready():

    print(client.user.name)
    print("start")
    game = discord.Game('/명령어')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content == "a":
        await message.channel.send("b")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
