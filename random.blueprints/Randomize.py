import random
import json
import os

shops = [
    "_World/Locations/TradeLists/Alluvyan_City.asset.odlo",
    "_World/Locations/TradeLists/Gillyshire_City.asset.odlo",
    "_World/Locations/TradeLists/Goldenfields_City.asset.odlo",
    "_World/Locations/TradeLists/MistyCoast_City.asset.odlo",
    "_World/Locations/TradeLists/Sevenkeeps_City.asset.odlo",
    "_World/Locations/TradeLists/SilverDriftHollow_City.asset.odlo",
    "_World/Locations/TradeLists/Southwatch_City.asset.odlo",
    "_World/Locations/TradeLists/Westguard_City.asset.odlo",
    "_World/Locations/TradeLists/Windholme_City.asset.odlo",
    "Locations/TradeLists/DarkElf_City.asset.odlo",
    "Campaigns/MainCampaign/Normal Trolls/Troll_City.asset.odlo",
]

def is_shop_entry(name):
    return name == "ShopDefinition/ResearchEntry" or name == "ShopDefinition/UnitEntry"

# Change the directory to the script's location, to make sure we're opening files from the right relative location.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

entries = []

# Read all the shoplists and save the "type" and "data" for each.
for shop in shops:
    with open(shop, 'r') as f:
        f.readline()
        contents = json.load(f)

        refs = contents["references"]["RefIds"]
        for ref in refs:
            if is_shop_entry(ref["type"]["class"]):
                entries.append({ "type" : ref["type"], "data" : ref["data"] })

# Shuffle!
random.shuffle(entries)

# Read the shoplist again but replace shop entries and overwrite the file.
for shop in shops:
    with open(shop, 'r') as f:
        file_header = f.readline()
        contents = json.load(f)

        for i in range(len(contents["references"]["RefIds"])):
            if is_shop_entry(contents["references"]["RefIds"][i]["type"]["class"]):
                # Keep the rid but replace the rest
                replacement = entries.pop()
                contents["references"]["RefIds"][i]["type"] = replacement["type"]
                contents["references"]["RefIds"][i]["data"] = replacement["data"]

    with open(shop, 'w', encoding="utf-8") as f:
        f.write("ShopDefinition\n")
        json.dump(contents, f, indent=4)
