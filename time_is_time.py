#!/usr/bin/env python3

import pymongo
from blizzard import Blizzard

blizzard = Blizzard()

class TimeIsTime:
    def __init__(self) -> None:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["hyjal"]
        self.collection = db["m_plus_dungeon_time"]

    dungeon_indexes = blizzard.game_mythic_keystone_dungeons_index()

    self.collection.delete_many({})

    for dungeon_index in dungeon_indexes["dungeons"]:
        insert_me = {}
        dungeon_times = blizzard.game_mythic_keystone_dungeons(dungeon_index["id"])
        insert_me["id"] =  dungeon_times["id"]
        insert_me["name"] = dungeon_times["name"]
        insert_me["upgrade_level"] = [
            {"1": dungeon_times["keystone_upgrades"][0]["qualifying_duration"]},
            {"2": dungeon_times["keystone_upgrades"][1]["qualifying_duration"]},
            {"3": dungeon_times["keystone_upgrades"][2]["qualifying_duration"]}
        ]
        collection.insert_one(insert_me)
