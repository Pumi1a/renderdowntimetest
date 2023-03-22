import discord
import os
from keep_alive import keep_alive

intents = discord.Intents.none()
intents.messages = True
intents.guilds = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(msg):
    txt_channel = client.get_channel(CHANNEL_ID)
    if txt_channel != msg.channel:
        return
    if msg.content == "test":
        await msg.delete()
    message = await txt_channel.fetch_message(MESSAGE_ID)
    emoji = "👍"
    if get_flag():
        global member
        id = MEMBER_ID
        member = await message.guild.fetch_member(id)
    if not message.reactions:
        await message.add_reaction(emoji)
    else:
        await message.remove_reaction(emoji,member)

def get_flag():
    global get_flag
    def get_flag():
        return False
    return True
    
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
MESSAGE_ID = int(os.getenv("MESSAGE_ID"))
MEMBER_ID = int(os.getenv("MEMBER_ID"))
keep_alive()
client.run(TOKEN)
