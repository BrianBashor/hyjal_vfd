#!/usr/bin/env python3

import time
import pymongo
import urllib
from datetime import datetime
from blizzard import Blizzard

blizzard = Blizzard()

IMG_PATH = "/mnt/disk1/item_media/"

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
collection = db["auction_house"]
collection_ah = db["auction_house"].distinct("item.id")
collection_id = db["items"].distinct("id")

ah_data = blizzard.auction_house()

for item in ah_data["auctions"]:
    collection.insert_one(item)

for item in db["auction_house"].distinct("item.id"):
    if item not in collection_id:
        asset = blizzard.game_item(item)
        if asset is not None:
            item_media = asset["media"]["key"]["href"]
            item_media = blizzard.generic_call(item_media)
            item_media = item_media["assets"][0]["value"]

            full_file_path = IMG_PATH + str(item) + ".jpg"
            asset["media"] = full_file_path
            urllib.request.urlretrieve(item_media, full_file_path)
            db["items"].insert_one(asset)
            time.sleep(1.1)
