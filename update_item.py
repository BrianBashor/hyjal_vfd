#!/usr/bin/env python3

import os
import urllib
import pymongo
from blizzard import Blizzard

blizzard = Blizzard()

IMG_PATH = "/Users/none/Documents/mongo/hyjal_vfd/item_media/"

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
ah_collection = db["auction_house"]
item_collection = db["items"]

ah_item_id = ah_collection.distinct("item.id")
found_items = item_collection.distinct("id")

item_collection.delete_many({})
for item in ah_item_id:
    if item not in found_items:
        print("Working on item: {}".format(item))
        asset = blizzard.game_item(item)
        item_media = asset["media"]["key"]["href"]
        item_media = blizzard.generic_call(item_media)
        item_media = item_media["assets"][0]["value"]

        save_location = IMG_PATH + str(item) + ".jpg"
        asset["media"] = save_location

        urllib.request.urlretrieve(item_media, save_location)

        item_collection.insert_one(asset)

print("Done!")
