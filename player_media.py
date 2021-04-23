#!/usr/bin/env python3

import urllib
import pymongo
from blizzard import Blizzard

blizzard = Blizzard()

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
collection = db["player_media"]

IMG_PATH = "/mnt/ext0/media/player/"

collection.delete_many({})

for player in db["guild_members"].find({}):
    insert_me = {"name": player["name"]}
    print("Inserting: {}".format(player["name"]))
    assets = blizzard.profile_character_media(player["name"], player["server"])
    for asset in assets["assets"]:
        full_file_path = IMG_PATH + player["name"] + "_" + asset["key"] + ".jpg"
        urllib.request.urlretrieve(asset["value"], full_file_path)
        insert_me[asset["key"]] = full_file_path
    collection.insert_one(insert_me)
