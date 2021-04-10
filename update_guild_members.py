#!/usr/bin/env python3

import re
import pymongo
from blizzard import Blizzard

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
collection = db["guild_members"]

blizzard = Blizzard()

collection.delete_many({})

with open('guild_members.txt', 'r') as f:
    for line in f:
        if re.match('^[a-z],*', line.lower()):
            line = line.split(' ')
            character_profile = blizzard.profile_character_profile(line[0].lower(), line[1].lower())
            insert_me = {
            "name": line[0].lower().strip(),
            "server": line[1].lower().strip(),
            "b_tag": line[2].lower().strip(),
            "main": line[3].lower().strip(),
            "raid_lead": line[4].lower().strip(),
            "gender": character_profile["gender"]["name"],
            "race": character_profile["race"]["name"],
            "class_name": character_profile["character_class"]["name"],
            "class_id": character_profile["character_class"]["id"],
            "level": character_profile["level"],
            "item_level": character_profile["equipped_item_level"]
            }

            if "covenant_progress" in character_profile.keys():
                insert_me["covenant"] = character_profile["covenant_progress"]["chosen_covenant"]["name"]
                insert_me["renown"] = character_profile["covenant_progress"]["renown_level"]

            print("Inserting: {}".format(insert_me["name"]))
            collection.insert_one(insert_me)
