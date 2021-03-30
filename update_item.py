#!/usr/bin/env python3

import os
import platform
import urllib
import pymongo
from blizzard import Blizzard

blizzard = Blizzard()

if platform.system() == "Darwin":
    IMG_PATH = "/Users/{}/Documents/mongo/hyjal_vfd/item_media/".format(os.environ["USER"])
else:
    IMG_PATH = "/home/{}/Pictures".format(os.environ["USER"])

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]

ah_id = db["auction_house"].distinct("item.id")
item_id = db["items"].distinct("id")

n_of_items_to_find = len(ah_id) - len(item_id)

for item in ah_id:
    if item not in item_id:
        print("Working on item: {}".format(item), end=" ")
        asset = blizzard.game_item(item)
        if asset is None:
            print(" | NOT FOUND: {}".format(item))
        else:
            item_media = asset["media"]["key"]["href"]
            item_media = blizzard.generic_call(item_media)
            item_media = item_media["assets"][0]["value"]

            save_location = IMG_PATH + str(item) + ".jpg"
            asset["media"] = save_location
            urllib.request.urlretrieve(item_media, save_location)

            db["items"].insert_one(asset)
            
            print(" | {} remain".format(n_of_items_to_find))
            n_of_items_to_find -= 1

print("Done!")
