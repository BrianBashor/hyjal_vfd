#!/usr/bin/env python3

from matplotlib.colors import Normalize
import pymongo
import matplotlib.pyplot as plt

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hyjal"]
collection = db["guild_members"]

covenant_color = {
    "Necrolord": "green",
    "Kyrian": "lightblue",
    "Venthyr": "red",
    "Night Fae": "blue",
}

class_color = {
    "warrior": "#C79C6E",
    "mage": "#40C7EB",
    "rogue": "#FFF569",
    "druid": "#FF7D0A",
    "warlock": "#8787ED",
    "shaman": "#0070DE",
    "monk": "#00FF96",
    "hunter": "#A9D271",
    "paladin": "#F58CBA",
    "demon hunter": "#A330C9",
    "death knight": "#C41F3B",
    "priest": "#FFFFFF"
}

class Chart:
    def player_covenant(self, only_mains=True):
        all_players = []
        if only_mains:
            for player in collection.find({"main": True}):
                if "covenant" in player:
                    all_players.append(player["covenant"])
        else:
            for player in collection.find({}):
                if "covenant" in player:
                    all_players.append(player["covenant"])
        labels = sorted(list(set(all_players)))
        size = []
        colors = []
        for label in labels:
            if only_mains:
                size.append(collection.count_documents({"covenant": label, "main": True}) / len(all_players))
                colors.append(covenant_color[label])
                title = "Current covenants for player mains"
            else:
                size.append(collection.count_documents({"covenant": label}) / len(all_players))
                colors.append(covenant_color[label])
                title = "Current covenants for all players"
        self.create_pie_chart(size, labels, colors, title)

    def player_class(self, only_mains=True):
        all_players = []
        if only_mains:
            for player in collection.find({"main": True}):
                all_players.append(player["class_name"])
        else:
            for player in collection.find({}):
                all_players.append(player["class_name"])
        labels = sorted(list(set(all_players)))
        size = []
        colors = []
        for label in labels:
            if only_mains:
                size.append(collection.count_documents({"class_name": label, "main": True}) / len(all_players))
                colors.append(str(class_color[label.lower()]))
                title = "Current race for player mains"
            else:
                size.append(collection.count_documents({"class_name": label}) / len(all_players))
                colors.append(str(class_color[label.lower()]))
                title = "Current covenants for all players"
        self.create_pie_chart(size, labels, colors, title)

    def create_pie_chart(self, size, labels, colors, title):
        explode = []
        for _ in labels:
            explode.append(0.02)
        _, ax1 = plt.subplots()
        ax1.pie(size, labels=labels, colors=colors, shadow=True, autopct='%1.1f%%', explode=explode, normalize=True)
        ax1.axis('equal')
        plt.title(title)
        plt.savefig("/tmp/my_chart.jpg")
        plt.show()

a = Chart()
a.player_class()
