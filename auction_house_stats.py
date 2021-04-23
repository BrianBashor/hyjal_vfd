#!/usr/bin/env python3

import time
import pymongo
import urllib
from datetime import datetime
from blizzard import Blizzard

IMG_PATH = "/mnt/ext0/media/item/"

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]

my_ah = db["auction_house"].distinct("item.id")

for items in my_ah:
    date_times = db["auction_house"].find({"item.id": items}).sort("date_time", pymongo.ASCENDING).distinct("date_time")
    for date_time in date_times:
        current_itme = db["auction_house"].find({"item.id": items, "date_time": date_time})
        for i in current_itme:
            print(i)
        print("#######")
    break
