#!/usr/bin/env python3
import discord
import time

TOKEN = 'YourAccessToken'
CHANNEL_ID = 1111111111111111

intents = discord.Intents.none()
intents.guilds = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')
    channel = client.get_channel(CHANNEL_ID)
    while True:
        await channel.send("test")
        time.sleep(2)
    
client.run(TOKEN)
