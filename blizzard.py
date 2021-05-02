import requests
import json
import time
import os

class Blizzard:
    api_count = 0
    def __init__(self):
        CLIENT = os.environ['B_CLIENT']
        SECRET = os.environ['B_SECRET']
        r = requests.post('https://us.battle.net/oauth/token', data={'grant_type': 'client_credentials'}, auth=(CLIENT, SECRET))
        self.access_token = json.loads(r.text)['access_token']
        
    def send_it(self, r):
        self.api_count += 1
        if r.status_code == 200:
            return json.loads(r.text)
        else:
            print('ERROR: {}'.format(r.status_code))
            return None

    # Game API Call #
    def game_mythic_keystone_season_index(self):
        r = requests.get('https://us.api.blizzard.com/data/wow/mythic-keystone/season/index?namespace=dynamic-us&locale=en_US&access_token={}'.format(self.access_token))
        return self.send_it(r)

    def game_professions_index(self):
        r = requests.get('https://us.api.blizzard.com/data/wow/profession/index?namespace=static-us&locale=en_US&access_token={}'.format(self.access_token))
        return self.send_it(r)

    def game_profession(self, n):
        r = requests.get('https://us.api.blizzard.com/data/wow/profession/{}?namespace=static-us&locale=en_US&access_token={}'.format(str(n), self.access_token))
        return self.send_it(r)

    def game_mythic_keystone_dungeons_index(self):
        r = requests.get('https://us.api.blizzard.com/data/wow/mythic-keystone/dungeon/index?namespace=dynamic-us&locale=en_US&access_token={}'.format(self.access_token))
        return self.send_it(r)

    def game_mythic_keystone_dungeons(self, index):
        r = requests.get('https://us.api.blizzard.com/data/wow/mythic-keystone/dungeon/{}?namespace=dynamic-us&locale=en_US&access_token={}'.format(str(index), self.access_token))
        return self.send_it(r)

    def game_mythic_keystone_period_index(self):
        r = requests.get('https://us.api.blizzard.com/data/wow/mythic-keystone/period/index?namespace=dynamic-us&locale=en_US&access_token={}'.format(self.access_token))
        return self.send_it(r)

    def game_mythic_keystone_leaderboard(self, dungeon_id, period, cr_id=1426):
        r = requests.get('https://us.api.blizzard.com/data/wow/connected-realm/{}/mythic-leaderboard/{}/period/{}?namespace=dynamic-us&locale=en_US&access_token={}'.format(str(cr_id), str(dungeon_id), str(period), self.access_token))
        return self.send_it(r)

    def game_playable_class_index(self):
        r = requests.get('https://us.api.blizzard.com/data/wow/playable-class/index?namespace=static-us&locale=en_US&access_token={}'.format(self.access_token))
        return self.send_it(r)

    def game_playable_class(self, class_id):
        r = requests.get('https://us.api.blizzard.com/data/wow/playable-class/{}?namespace=static-us&locale=en_US&access_token={}'.format(str(class_id), self.access_token))
        return self.send_it(r)

    def game_playable_class_media(self, class_id):
        r = requests.get('https://us.api.blizzard.com/data/wow/media/playable-class/{}?namespace=static-us&locale=en_US&access_token={}'.format(str(class_id), self.access_token))
        return self.send_it(r)

    def game_playable_specialization(self, id):
        r = requests.get('https://us.api.blizzard.com/data/wow/playable-specialization/{}?namespace=static-us&locale=en_US&access_token={}'.format(str(id), self.access_token))
        return self.send_it(r)

    def game_playable_specialization_index(self):
        r = requests.get('https://us.api.blizzard.com/data/wow/playable-specialization/index?namespace=static-us&locale=en_US&access_token={}'.format(self.access_token))
        return self.send_it(r)

    def game_mythic_keystone_seasons(self):
        r = requests.get('https://us.api.blizzard.com/data/wow/mythic-keystone/season/index?namespace=dynamic-us&locale=en_US&access_token={}'.format(self.access_token))
        return self.send_it(r)

    def game_item(self, item_id):
        r = requests.get('https://us.api.blizzard.com/data/wow/item/{}?namespace=static-us&locale=en_US&access_token={}'.format(str(item_id), self.access_token))
        return self.send_it(r)

    def game_item_media(self, item_id):
        r = requests.get('https://us.api.blizzard.com/data/wow/media/item/{}?namespace=static-us&locale=en_US&access_token={}'.format(str(item_id), self.access_token))
        return self.send_it(r)

    def profile_character_equipment(self, name, server):
        r = requests.get('https://us.api.blizzard.com/profile/wow/character/{}/{}/equipment?namespace=profile-us&locale=en_US&access_token={}'.format(server, name, self.access_token))
        return self.send_it(r)

    def profile_character_profession(self, name, server):
        r = requests.get('https://us.api.blizzard.com/profile/wow/character/{}/{}/professions?namespace=profile-us&locale=en_US&access_token={}'.format(server, name, self.access_token))
        return self.send_it(r)

    def profile_character_profile(self, name, server, n=5):
        r = requests.get('https://us.api.blizzard.com/profile/wow/character/{}/{}?namespace=profile-us&locale=en_US&access_token={}'.format(server, name, self.access_token))
        return self.send_it(r)

    def profile_character_pvp(self, name, server, bracket):
        r = requests.get('https://us.api.blizzard.com/profile/wow/character/{}/{}/pvp-bracket/{}?namespace=profile-us&locale=en_US&access_token={}'.format(server, name, bracket, self.access_token))
        return self.send_it(r)

    def profile_character_media(self, name, server):
        r = requests.get('https://us.api.blizzard.com/profile/wow/character/{}/{}/character-media?namespace=profile-us&locale=en_US&access_token={}'.format(server, name, self.access_token))
        return self.send_it(r)

    def profile_specialization(self, url):
        r = requests.get(url)
        return self.send_it(r)

    def generic_call(self, url):
        r = requests.get(url + '&access_token=' + self.access_token)
        return self.send_it(r)

    def auction_house(self, cr_id=1426):
        r = requests.get('https://us.api.blizzard.com/data/wow/connected-realm/{}/auctions?namespace=dynamic-us&locale=en_US&access_token={}'.format(str(cr_id), self.access_token))
        return self.send_it(r)

