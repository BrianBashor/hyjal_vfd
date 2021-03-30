#!/usr/bin/env python3

import pymongo
from datetime import datetime
from blizzard import Blizzard

blizzard = Blizzard()

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
db["player_gear"]

now = datetime.now()
now = now.strftime("%Y_%m_%d_%H_%M_%S")

for player in db["guild_members"].find({}):
    print("Working on {}".format(player["name"]))
    insert_me = blizzard.profile_character_equipment(player["name"], player["server"])
    insert_me["date_time"] = now
    db["player_gear"].insert_one(insert_me)
