#!/usr/bin/env python3

import time
import pymongo
import urllib
from datetime import datetime
from blizzard import Blizzard

blizzard = Blizzard()

IMG_PATH = "/mnt/ext0/media/item/"

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]

ah_data = blizzard.auction_house()
current_time = datetime.utcnow()

for item in ah_data["auctions"]:
    item["date_time"] = current_time
    db["auction_house"].insert_one(item)

my_ah = db["auction_house"].distinct("item.id")
my_items = db["items"].distinct("id")

for item in my_ah:
    if item not in my_items:
        asset = blizzard.game_item(item)
        if asset is not None:
            print("Inserting item: {} : {} remaining".format(item, diff))
            item_media = asset["media"]["key"]["href"]
            item_media = blizzard.generic_call(item_media)
            item_media = item_media["assets"][0]["value"]
            full_file_path = IMG_PATH + str(item) + ".jpg"
            asset["media"] = full_file_path
            urllib.request.urlretrieve(item_media, full_file_path)
            db["items"].insert_one(asset)
            time.sleep(1)
        diff -= 1
