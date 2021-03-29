#!/usr/bin/env python3

import os
import time
import urllib
import pymongo
from blizzard import Blizzard

blizzard = Blizzard()

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
ah_collection = db["auction_house"]
item_collection = db["items"]

ah_item_id = ah_collection.distinct("item.id")
item_id = item_collection.distinct("id")

n_of_item_to_insert = 0
for ah_item in ah_item_id:
    if ah_item not in item_id:
        n_of_item_to_insert += 1

for ah_item in ah_item_id:
    if ah_item not in item_id:
        print("Working on item: {}".format(ah_item))
        insert_me = blizzard.game_item(ah_item)
        item_media = insert_me["media"]["key"]["href"]
        item_media = blizzard.generic_call(item_media)
        item_media = item_media["assets"][0]["value"]
        time.sleep(1)

        urllib.request.urlretrieve(item_media, "/tmp/delete_me.jpg")
        with open("/tmp/delete_me.jpg", 'rb') as img:
            insert_me["media"] = img.read()
        os.remove("/tmp/delete_me.jpg")
        item_collection.insert_one(insert_me)
        time.sleep(1)
        
        print("{} Items remaining".format(n_of_item_to_insert))
        n_of_item_to_insert -= 1

print("Done!")
