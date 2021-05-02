#!/usr/bin/env python3

import time
import urllib
import pymongo
import threading
from datetime import datetime
from blizzard import Blizzard

blizzard = Blizzard()

current_time = datetime.utcnow()
IMG_PATH = '/mnt/disk1/media/item/'

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['hyjal']

def get_item(item_n: str) -> None:
    item = blizzard.game_item(item_n)
    if item is not None:
        item_media = item['media']['key']['href']
        item_media = blizzard.generic_call(item_media)
        item_media = item_media['assets'][0]['value']
        full_file_path = IMG_PATH + str(item_n) + '.jpg'
        item['media'] = full_file_path
        urllib.request.urlretrieve(item_media, full_file_path)
        db['items'].insert_one(item)

ah_data = blizzard.auction_house()
if ah_data is not None:
    for item in ah_data['auctions']:
        item['date_time'] = current_time
        db['auction_house'].insert_one(item)

new_items = []
for item in db['auction_house'].distinct('item.id'):
    if item not in db['items'].distinct('id'):
        new_items.append(str(item))

for _ in range(10):
    threads = []
    for _ in range(50):
        item_n = str(new_items.pop())
        t = threading.Thread(target=get_item, args=[item_n])
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    time.sleep(3)
