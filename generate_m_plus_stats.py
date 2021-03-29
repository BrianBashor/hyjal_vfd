#!/usr/bin/env python3

import re
import pymongo
import matplotlib.pyplot as plt

from blizzard import Blizzard

blizzard = Blizzard()

season_indexes = blizzard.game_mythic_keystone_season_index()
current_season = season_indexes["current_season"]["id"]

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
current_season = db["m_plus_season_" + str(current_season)]
guild_members = db["guild_members"]
dungeon_times = db["m_plus_dungeon_time"]

def get_player_dungeon_info(player):
    return_me = []
    for doc in current_season.find({}):
        for group in doc["leading_groups"]:
                for member in group["members"]:
                    if player in str(member.values()).lower():
                        append_me = {
                            "keystone_level": group["keystone_level"],
                            "duration": group["duration"],
                        }

                        print(append_me)
                        input("STOP")

    #                 append_me[member["profile"]["name"]] = member["specialization"]["id"]
    #     return_me.append(append_me)
    # return return_me

a = get_player_dungeon_info("opprobriums")
# print(a)
# all_runs = []
# found_object_id = []

# for guild_member in guild_members.find({}):
#     print("Working on: {}".format(guild_member["name"]))
#     run_info = {}
#     for doc in current_season.find({}):
#         for group in doc["leading_groups"]:
#             for group_member in group["members"]:
#                 if re.match(guild_member["name"].lower(), group_member["profile"]["name"].lower()):
#                     for member in group["members"]:
#                         print(member)
                    #     if [member["profile"]["name"]] != guild_member["name"]:
                    #         run_info = {
                    #             "guild_member": guild_member["name"],
                    #             "b_tag": guild_member["b_tag"],
                    #             "key_level": group["keystone_level"],
                    #             "dungeon_name": doc["map"]["name"],
                    #             "dungeon_time": group["duration"],
                    #             "period": doc["period"],
                    #             "team": []
                    #         }
                    #         run_info["team"].append([
                    #             member["profile"]["name"],
                    #             member["specialization"]["id"]
                    #         ])
                    # all_runs.append(run_info)


# def player_key_chart_by_b_tag(player):
#     key_level = {}
#     for run in all_runs:
#         if run["b_tag"] == player:
#             if run["key_level"] in key_level.keys():
#                 key_level[run["key_level"]] += 1
#             else:
#                 key_level[run["key_level"]] = 1

#     high_key = 0
#     for k in key_level.keys():
#         if k > high_key:
#             high_key = k               
            
#     lable = []
#     size = []
        
#     for i in range(2, high_key + 1):
#         if i in key_level.keys():
#             lable.append(i)
#             size.append(key_level[i])

#     plt.xlabel("Key Level")
#     plt.ylabel("Number of keys")
#     plt.title("Key results for: {}".format(player))
#     plt.bar(lable, size, color='#00FF96')
#     plt.show()
    
# # player_key_chart_by_b_tag("opps")

# def who_played_with_who(target_player): # pie chart
#     players = {}
#     total = 0
#     lable = []
#     size = []
#     color = []

#     for run in all_runs:
#         for player in run["team"]:
#             if player[0].lower() != target_player:
#                 if player[0] in players.keys():
#                     players[player[0]] += 1
#                     total += 1
#                 else:
#                     players[player[0]] = 1
#                     total += 1
                    
#                 lable.append(player[0])
                
#                 a = db["class_and_spec_info"].find_one({"spec_id": player[1]})
#                 print(a["class_color"])

#         print(player[1])
                
# who_played_with_who("opprobriums")
            

# found_btag = []
# total_run = 0
# for run in all_runs:
    
#     # current_b_tag = run["b_tag"]
#     # total_run = 0
#     # if current_b_tag not in found_btag:
#     #     found_btag.append(current_b_tag)
#     if run["b_tag"] == "opps":
        
#         total_run += 1



# data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
# names = list(data.keys())
# values = list(data.values())

# fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
# axs[0].bar(names, values)
# axs[1].scatter(names, values)
# axs[2].plot(names, values)
# fig.suptitle('Categorical Plotting')
# plt.show()



# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.show()