import requests
import json
import os

class Blizzard:
    api_count = 0
    def __init__(self):
        CLIENT = os.environ['B_CLIENT']
        SECRET = os.environ['B_SECRET']
        r = requests.post('https://us.battle.net/oauth/token', data={'grant_type': 'client_credentials'}, auth=(CLIENT, SECRET))
        self.access_token = json.loads(r.text)['access_token']

    # Game API Call #
    def game_mythic_keystone_season_index(self):
        self.api_count += 1
        current_season = requests.get("https://us.api.blizzard.com/data/wow/mythic-keystone/season/index?namespace=dynamic-us&locale=en_US&access_token={}".format(self.access_token))
        if current_season.status_code == 200: return json.loads(current_season.text)
        else: return None

    def game_professions_index(self):
        self.api_count += 1
        p_name = requests.get("https://us.api.blizzard.com/data/wow/profession/index?namespace=static-us&locale=en_US&access_token={}".format(self.access_token))
        if p_name.status_code == 200: return json.loads(p_name.text)
        else: return None

    def game_profession(self, n):
        self.api_count += 1
        p_tier = requests.get("https://us.api.blizzard.com/data/wow/profession/{}?namespace=static-us&locale=en_US&access_token={}".format(str(n), self.access_token))
        if p_tier.status_code == 200: return json.loads(p_tier.text)
        else: return None

    def game_mythic_keystone_dungeons_index(self):
        self.api_count += 1
        dungeon = requests.get("https://us.api.blizzard.com/data/wow/mythic-keystone/dungeon/index?namespace=dynamic-us&locale=en_US&access_token={}".format(self.access_token))
        if dungeon.status_code == 200: return json.loads(dungeon.text)
        else: return None

    def game_mythic_keystone_dungeons(self, index):
        self.api_count += 1
        dungeon = requests.get("https://us.api.blizzard.com/data/wow/mythic-keystone/dungeon/{}?namespace=dynamic-us&locale=en_US&access_token={}".format(str(index), self.access_token))
        if dungeon.status_code == 200: return json.loads(dungeon.text)
        else: return None

    def game_mythic_keystone_period_index(self):
        self.api_count += 1
        dungeon = requests.get("https://us.api.blizzard.com/data/wow/mythic-keystone/period/index?namespace=dynamic-us&locale=en_US&access_token={}".format(self.access_token))
        if dungeon.status_code == 200: return json.loads(dungeon.text)
        else: return None

    def game_mythic_keystone_leaderboard(self, dungeon_id, period, cr_id=1426):
        self.api_count += 1
        dungeon = requests.get("https://us.api.blizzard.com/data/wow/connected-realm/{}/mythic-leaderboard/{}/period/{}?namespace=dynamic-us&locale=en_US&access_token={}".format(str(cr_id), str(dungeon_id), str(period), self.access_token))
        if dungeon.status_code == 200: return json.loads(dungeon.text)
        else: return dungeon.status_code

    def game_playable_class_index(self):
        self.api_count += 1
        spec = requests.get("https://us.api.blizzard.com/data/wow/playable-class/index?namespace=static-us&locale=en_US&access_token={}".format(self.access_token))
        if spec.status_code == 200: return json.loads(spec.text)
        else: return None

    def game_playable_class(self, class_id):
        self.api_count += 1
        class_info = requests.get("https://us.api.blizzard.com/data/wow/playable-class/{}?namespace=static-us&locale=en_US&access_token={}".format(str(class_id), self.access_token))
        if class_info.status_code == 200: return json.loads(class_info.text)
        else: return None
        
    def game_playable_class_media(self, class_id):
        self.api_count += 1
        spec = requests.get("https://us.api.blizzard.com/data/wow/media/playable-class/{}?namespace=static-us&locale=en_US&access_token={}".format(str(class_id), self.access_token))
        if spec.status_code == 200: return json.loads(spec.text)
        else: return None

    def game_playable_specialization(self, id):
        self.api_count += 1
        spec = requests.get("https://us.api.blizzard.com/data/wow/playable-specialization/{}?namespace=static-us&locale=en_US&access_token={}".format(str(id), self.access_token))
        if spec.status_code == 200: return json.loads(spec.text)
        else: return None

    def game_playable_specialization_index(self):
        self.api_count += 1
        spec = requests.get("https://us.api.blizzard.com/data/wow/playable-specialization/index?namespace=static-us&locale=en_US&access_token={}".format(self.access_token))
        if spec.status_code == 200: return json.loads(spec.text)
        return None

    def game_mythic_keystone_seasons(self):
        self.api_count += 1
        key_season = requests.get("https://us.api.blizzard.com/data/wow/mythic-keystone/season/index?namespace=dynamic-us&locale=en_US&access_token={}".format(self.access_token))
        if key_season.status_code == 200: return json.loads(key_season.text)
        else: return None

    def game_item(self, item_id):
        self.api_count += 1
        item = requests.get("https://us.api.blizzard.com/data/wow/item/{}?namespace=static-us&locale=en_US&access_token={}".format(str(item_id), self.access_token))
        if item.status_code == 200: return json.loads(item.text)
        else: return None

    def game_item_media(self, item_id):
        self.api_count += 1
        item = requests.get("https://us.api.blizzard.com/data/wow/media/item/{}?namespace=static-us&locale=en_US&access_token={}".format(str(item_id), self.access_token))
        if item.status_code == 200: return json.loads(item.text)
        else: return None

    # Profile API Call
    def profile_character_equipment(self, name, server):
        self.api_count += 1
        p_gear = requests.get("https://us.api.blizzard.com/profile/wow/character/{}/{}/equipment?namespace=profile-us&locale=en_US&access_token={}".format(server, name, self.access_token))
        if p_gear.status_code == 200: return json.loads(p_gear.text)
        else: return None

    def profile_character_profession(self, name, server):
        self.api_count += 1
        p_player = requests.get("https://us.api.blizzard.com/profile/wow/character/{}/{}/professions?namespace=profile-us&locale=en_US&access_token={}".format(server, name, self.access_token))
        if p_player.status_code == 200: return json.loads(p_player.text)
        else: return None

    def profile_character_profile(self, name, server):
        self.api_count += 1
        profile = requests.get("https://us.api.blizzard.com/profile/wow/character/{}/{}?namespace=profile-us&locale=en_US&access_token={}".format(server, name, self.access_token))
        if profile.status_code == 200: return json.loads(profile.text)
        else: return profile

    def profile_character_pvp(self, name, server, bracket):
        self.api_count += 1
        pvp = requests.get("https://us.api.blizzard.com/profile/wow/character/{}/{}/pvp-bracket/{}?namespace=profile-us&locale=en_US&access_token={}".format(server, name, bracket, self.access_token))
        if pvp.status_code == 200: return json.loads(pvp.text)["rating"]
        else: return 0

    def profile_character_media(self, name, server):
        self.api_count += 1
        render = requests.get("https://us.api.blizzard.com/profile/wow/character/{}/{}/character-media?namespace=profile-us&locale=en_US&access_token={}".format(server, name, self.access_token))
        if render.status_code == 200: return json.loads(render.text)
        else: return None

    def profile_specialization(self, url):
        self.api_count += 1
        spec = requests.get(url)
        if spec.status_code == 200: return json.loads(spec.text + "&access_token=" + self.access_token)
        else: return None

    # Generic API CALL
    def generic_call(self, url):
        self.api_count += 1
        external = requests.get(url + "&access_token=" + self.access_token)
        if external.status_code == 200: return json.loads(external.text)
        else: return None

    def auction_house(self, cr_id=1426):
        self.api_count += 1
        external = requests.get("https://us.api.blizzard.com/data/wow/connected-realm/{}/auctions?namespace=dynamic-us&locale=en_US&access_token={}".format(str(cr_id), self.access_token))
        if external.status_code == 200: return json.loads(external.text)
        else: return None
