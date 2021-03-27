#!/usr/bin/env python3

""" load m + leaderboard info for the current season. """
""" all previous data will be deleted """


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

collection.delete_many({})

for current_period in current_season_info["periods"]:
    for dungeon_index in dungeon_indexes["dungeons"]:
        insert_me = blizzard.game_mythic_keystone_leaderboard(dungeon_index["id"], current_period["id"])
        try:
            if insert_me["leading_groups"]:
                print("Writing for peroid {} : {}".format( current_period["id"], dungeon_index["name"],))
                collection.insert_one(insert_me)
        except Exception as e:
            print("No data for peroid {} : {}".format( current_period["id"], dungeon_index["name"]))

print("Done!")
