#!/usr/bin/env python3

import re
import pymongo

from blizzard import Blizzard

blizzard = Blizzard()

season_indexes = blizzard.game_mythic_keystone_season_index()
current_season = season_indexes["current_season"]["id"]

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
guild_members = db["guild_members"]
current_season = db["m_plus_season_" + str(current_season)]
m_plus_achievement = db["m_plus_achievement"]

m_plus_achievement.delete_many({})

dungeon_time = {}
for time in db["m_plus_dungeon_time"].find({}):
    dungeon_time[time["name"]] = time["upgrade_level"][0]["1"]

found_b_tags = []
for guild_member in guild_members.find({}):
    if guild_member["b_tag"] not in found_b_tags:
        found_b_tags.append(guild_member["b_tag"])

for b_tag in found_b_tags:
    dungeon_results = {}
    for k in dungeon_time.keys():
        dungeon_results[k] = False
    for guild_member in guild_members.find({"b_tag": b_tag}):
        for doc in current_season.find({}):
            for leading_group in doc["leading_groups"]:
                if leading_group["keystone_level"] >= 15:
                    if leading_group["duration"] < dungeon_time[doc["name"]]:
                        for member in leading_group["members"]:
                            if re.match(guild_member["name"], member["profile"]["name"].lower()):
                                dungeon_results[doc["name"]] = True

    m_plus_achievement.insert_one({
        "name": b_tag,
        "dungeons": dungeon_results
        })
