#!/usr/bin/env python3

import pymongo
from datetime import datetime
from blizzard import Blizzard

blizzard = Blizzard()
ah_data = blizzard.auction_house()

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
collection = db["auction_house"]

now = datetime.now()
now = now.strftime("%Y_%m_%d_%H_%M_%S")

for item in ah_data["auctions"]:
    item["date_time"] = now
    collection.insert_one(item)

print("Done!")
