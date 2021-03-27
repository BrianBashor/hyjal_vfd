#!/usr/bin/env python3

import pymongo
from blizzard import Blizzard

blizzard = Blizzard()

dungeon_indexes = blizzard.game_mythic_keystone_dungeons_index()
season_indexes = blizzard.game_mythic_keystone_season_index()
season_index = season_indexes["current_season"]["key"]["href"]
current_season_info = blizzard.generic_call(season_index)
current_season_num = season_indexes["current_season"]["id"]

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
collection = db["m_plus_season_" + str(current_season_num)]

cursor = collection.find({})
last_period_update = 0
for doc in cursor: 
    if doc["period"] > last_period_update:
        last_period_update = doc["period"]

current_period = 0
for current_season in current_season_info["periods"]:
    if current_season["id"] > current_period:
        current_period = current_season["id"]

for period in range(last_period_update, current_period + 1):
    for dungeon_index in dungeon_indexes["dungeons"]:
        search_me = {
            "period": period, 
            "map_challenge_mode_id": dungeon_index["id"]
        }
        insert_me = blizzard.game_mythic_keystone_leaderboard(dungeon_index["id"], period)
        if period == last_period_update: 
            collection.find_one_and_replace(search_me, insert_me)
        else: 
            collection.insert_one(insert_me)

print("Done!")
