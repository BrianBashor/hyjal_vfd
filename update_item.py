#!/usr/bin/env python3

import os
import urllib
import pymongo
from blizzard import Blizzard

blizzard = Blizzard()

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
ah_collection = db["auction_house"]
item_collection = db["items"]


ah_item_id = ah_collection.distinct("item.id")
item_item_id = item_collection.distinct("id")

for i in ah_collection:
    print(i)

# for item_id in ah_item_id:
#     if item_id not in  item_item_id:
#         print("Working on item: {}".format(item_id))
#         insert_me = blizzard.game_item(item_id)
#         item_media = insert_me["media"]["key"]["href"]
#         item_media = blizzard.generic_call(item_media)
#         item_media = item_media["assets"][0]["value"]

#         urllib.request.urlretrieve(item_media, "/tmp/delete_me.jpg")
#         with open("/tmp/delete_me.jpg", 'rb') as img:
#             insert_me["media"] = img.read()
#         os.remove("/tmp/delete_me.jpg")
#         item_collection.insert_one(insert_me)
#         time.sleep(1)

# print("Done!")
