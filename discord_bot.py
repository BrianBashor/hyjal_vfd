#!/usr/bin/env python3

import os
import pymongo
import discord

TOKEN  = os.environ['DISCORD_TOKEN']

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('#plus15'):
        target_player = message.content.split(' ')[1]
        player = db["guild_members"].find_one({"name": target_player.lower()})
        results = db["m_plus_achievement"].find_one({"name": player["b_tag"]})
        send_me = target_player + " ( " + player["b_tag"] + " )\n"
        send_me += "-" * 27
        send_me += "\n"
        for dungeon in results["dungeons"]:
            send_me += dungeon
            send_me += " " * (22 - len(dungeon))
            send_me += " | "
            if results["dungeons"][dungeon]:
                send_me += "\U00002705"
            else:
                send_me += "\U0000274C"
            send_me += '\n'

        await message.channel.send(" ```" + send_me + "```")
    else:
        await message.channel.send("Did not find {}".format(message.content.split(' ')[1]))

client.run(TOKEN)
