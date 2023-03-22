#!/usr/bin/env python3
import discord
import time 
import datetime

TOKEN = 'YourAccessToken'
MESSAGE_ID = 111111111111111

intents = discord.Intents.none()
intents.reactions = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id != MESSAGE_ID:
        return
    global t_add
    t_add = time.time()
    diff = t_add - t_remove
    func(diff)

@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id != MESSAGE_ID:
        return
    global t_remove
    t_remove = time.time()

def func(diff):
    dt = datetime.datetime.now()
    f = open("./time.log","a")
    f.write("logout:" + str(dt - datetime.timedelta(seconds=diff)) + "\n")
    f.write("login :" + str(dt) + "\n")

client.run(TOKEN)
