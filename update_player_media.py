#!/usr/bin/env python3

import os
import urllib
import pymongo
import platform
from blizzard import Blizzard

blizzard = Blizzard()

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
collection = db["player_media"]

if platform.system() == "Darwin":
    IMG_PATH = "/Users/{}/Documents/mongo/hyjal_vfd/player_media/".format(os.environ["USER"])
elif platform.system() == "Linux":
    IMG_PATH = "/home/{}/Pictures/player_media/".format(os.environ["USER"])
if not os.path.isdir(IMG_PATH):
    os.mkdir(IMG_PATH)

collection.delete_many({})

for player in collection.find({}):
    insert_me = {"name": player["name"]}
    assets = blizzard.profile_character_media(player["name"], player["server"])
    for asset in assets["assets"]:
        full_file_path = IMG_PATH + player["name"] + "_" + asset["key"] + ".jpg"
        urllib.request.urlretrieve(asset["value"], full_file_path)
        insert_me[asset["key"]] = full_file_path

    collection.insert_one(insert_me)

print("Done!")
