#!/usr/bin/env python3

import urllib
import pymongo
from blizzard import Blizzard

blizzard = Blizzard()

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
collection_ah = db["auction_house"].distinct("item.id")
collection_id = db["items"].distinct("id")

IMG_PATH = "/mnt/disk1/item_media/"

n_of_items = len(collection_ah) - len(collection_id)

for item in collection_ah:
    if item not in collection_id:
        asset = blizzard.game_item(item)
        if asset is not None:
            item_media = asset["media"]["key"]["href"]
            item_media = blizzard.generic_call(item_media)
            item_media = item_media["assets"][0]["value"]

            full_file_path = IMG_PATH + str(item) + ".jpg"
            asset["media"] = full_file_path
            urllib.request.urlretrieve(item_media, full_file_path)
            print("{}: {}".format(n_of_items, asset["name"]))
            db["items"].insert_one(asset)
            n_of_items -= 1
