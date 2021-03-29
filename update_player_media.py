#!/usr/bin/env python3

import urllib
import pymongo
from blizzard import Blizzard

blizzard = Blizzard()

IMG_PATH = "/Users/none/Documents/mongo/hyjal_vfd/player_media/"

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
collection = db["player_media"]

collection.delete_many({})

for player in db["guild_members"].find({}):
    print("Working on: {}".format(player["name"]))
    assets = blizzard.profile_character_media(player["name"], player["server"])
    insert_me = {"name": player["name"]}
    for asset in assets["assets"]:
        save_location = IMG_PATH + player["name"] + "_" + asset["key"] + ".jpg"
        urllib.request.urlretrieve(asset["value"], save_location)
        insert_me[asset["key"]] = save_location

    collection.insert_one(insert_me)

print("Done!")
