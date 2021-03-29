#!/usr/bin/env python3

import os
import time
import urllib
import pymongo
from blizzard import Blizzard

blizzard = Blizzard()

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
collection = db["player_media"]

collection.delete_many({})

for player in db["guild_members"].find({}):
    print("Working on: {}".format(player["name"]))
    assets = blizzard.profile_character_media(player["name"], player["server"])
    insert_me = {"name": player["name"]}
    for asset in assets["assets"]:
        urllib.request.urlretrieve(asset["value"], "/tmp/delete_me.jpg")
        with open("/tmp/delete_me.jpg", 'rb') as img:
            insert_me[asset["key"]] = img.read()
        os.remove("/tmp/delete_me.jpg")
    collection.insert_one(insert_me)

print("Done!")
