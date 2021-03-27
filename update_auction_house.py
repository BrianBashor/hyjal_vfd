#!/usr/bin/env python3

import pymongo
from blizzard import Blizzard

blizzard = Blizzard()
ah_data = blizzard.auction_house()

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
collection = db["auction_house"]

for item in ah_data["auctions"]:
    collection.insert_one(item)
    
print("Done!")
