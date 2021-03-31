#!/usr/bin/env python3

import os
import platform
import urllib
import pymongo
from blizzard import Blizzard

blizzard = Blizzard()

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
collection_ah = db["auction_house"].distinct("item.id")
collection_id = db["items"].distinct("id")

if platform.system() == "Darwin":
    IMG_PATH = "/Users/{}/Documents/mongo/hyjal_vfd/item_media/".format(os.environ["USER"])
elif platform.system() == "Linux":
    IMG_PATH = "/home/{}/Pictures/item_media".format(os.environ["USER"])
if not os.path.isdir(IMG_PATH):
    os.mkdir(IMG_PATH)

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

            db["items"].insert_one(asset)

print("Done!")
