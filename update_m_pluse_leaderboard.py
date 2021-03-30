#!/usr/bin/env python3

import pymongo
from blizzard import Blizzard

blizzard = Blizzard()

dungeon_indexes = blizzard.game_mythic_keystone_dungeons_index()["dungeons"]
current_season = blizzard.game_mythic_keystone_season_index()["current_season"]
season_periods = blizzard.generic_call(current_season["key"]["href"])
season_periods = season_periods["periods"]
current_season = current_season["id"]
current_period = season_periods[-1]["id"]

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
collection = db["m_plus_season_" + str(current_season)]

if collection.count_documents({}) == 0:
    start_period = season_periods[0]["id"]
else:
    start_period = collection.find_one(sort=[("period", pymongo.DESCENDING)])
    start_period = start_period["period"]

for period in range(start_period, current_period + 1):
    for dungeon_index in dungeon_indexes:
        insert_me = blizzard.game_mythic_keystone_leaderboard(dungeon_index["id"], period) 
        if collection.find_one({"period": period, "map_challenge_mode_id": dungeon_index["id"]}):
            print("Replacing for peroid {} : {}".format( period, dungeon_index["name"],))
            collection.replace_one({
                "period": period,
                "map_challenge_mode_id": dungeon_index
                }, insert_me)
        else:
            try:
                if insert_me["leading_groups"]:
                    print("Writing for peroid {} : {}".format(period, dungeon_index["name"]))
                    collection.insert_one(insert_me)
            except Exception as e:
                print("No data for peroid {} : {}".format(period, dungeon_index["name"]))

print("Done!")
