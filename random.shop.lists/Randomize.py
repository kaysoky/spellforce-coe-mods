import random
import json

shops = [
    "_World/Locations/TradeLists/Alluvyan_Herbs.asset.odlo",
    "_World/Locations/TradeLists/Alchemist.asset.odlo",
    "_World/Locations/TradeLists/Alluvyan_Units.asset.odlo",
    "_World/Locations/TradeLists/Barracks_Animal_Start.asset.odlo",
    "_World/Locations/TradeLists/Barracks_Dwarf.asset.odlo",
    "_World/Locations/TradeLists/Barracks_Dwarf_Start.asset.odlo",
    "_World/Locations/TradeLists/Barracks_Goblin.asset.odlo",
    "_World/Locations/TradeLists/Barracks_Human.asset.odlo",
    "_World/Locations/TradeLists/Barracks_Human_Start.asset.odlo",
    "_World/Locations/TradeLists/Barracks_Orc.asset.odlo",
    "_World/Locations/TradeLists/Barracks_Orc_Start.asset.odlo",
    "_World/Locations/TradeLists/Coldmark_Units.asset.odlo",
    "_World/Locations/TradeLists/ExoticStore.asset.odlo",
    "_World/Locations/TradeLists/Gillyshire_Shop.asset.odlo",
    "_World/Locations/TradeLists/Gillyshire_Units.asset.odlo",
    "_World/Locations/TradeLists/Goldenfields_Food.asset.odlo",
    "_World/Locations/TradeLists/Goldenfields_Units.asset.odlo",
    "_World/Locations/TradeLists/GuildShop.asset.odlo",
    "_World/Locations/TradeLists/LoreShop.asset.odlo",
    "_World/Locations/TradeLists/MistyCoast_Shaman.asset.odlo",
    "_World/Locations/TradeLists/MistyCoast_Slaves.asset.odlo",
    "_World/Locations/TradeLists/Runesmith.asset.odlo",
    "_World/Locations/TradeLists/Sevenkeeps_Priests.asset.odlo",
    "_World/Locations/TradeLists/Sevenkeeps_Runes.asset.odlo",
    "_World/Locations/TradeLists/Sevenkeeps_Units.asset.odlo",
    "_World/Locations/TradeLists/SilverDriftHollow_Mines.asset.odlo",
    "_World/Locations/TradeLists/Southwatch_Food.asset.odlo",
    "_World/Locations/TradeLists/Southwatch_Runesmith.asset.odlo",
    "_World/Locations/TradeLists/Southwatch_Units.asset.odlo",
    "_World/Locations/TradeLists/Westguard_Bookstore.asset.odlo",
    "_World/Locations/TradeLists/Westguard_Units.asset.odlo",
    "_World/Locations/TradeLists/Windholme_Smith.asset.odlo",
    "_World/Locations/TradeLists/Windholme_Units.asset.odlo",
    "Locations/TradeLists/Barracks_DarkElf_Start.asset.odlo",
    "Locations/TradeLists/Barracks_Troll.asset.odlo",
    "Locations/TradeLists/DarkElf_Archon.asset.odlo",
    "Locations/TradeLists/DarkElf_Dracon.asset.odlo",
    "Locations/TradeLists/DarkElf_Sinistra.asset.odlo",
    "Locations/TradeLists/Demonologist Shop_01.asset.odlo",
    "Locations/TradeLists/Demonologist Shop_02.asset.odlo",
    "Locations/TradeLists/Uram Gor Demon Shop.asset.odlo",
    "Campaigns/MainCampaign/Mugwa Trolls/Mugwa_City.asset.odlo",
    "Campaigns/MainCampaign/Mugwa Trolls/Mugwa_Units.asset.odlo",
    "Campaigns/MainCampaign/Normal Trolls/Troll_Cannibals.asset.odlo",
    "Campaigns/MainCampaign/Normal Trolls/Troll_Units.asset.odlo",
]

# Returns a mapping from "rid" to "ReputationLevel"
def extract_reputation(refs):
    levels = {}
    for ref in refs:
        if ref["type"]["class"] == "ShopDefinition/EntryRank":
            for entry in ref["data"]["PossibleEntries"]:
                levels[str(entry["rid"])] = ref["data"]["ReputationLevel"]
    return levels


def is_shop_entry(name):
    return name == "ShopDefinition/ItemEntry" or name == "ShopDefinition/UnitEntry" or name == "ShopDefinition/ResearchEntry"

# One list for each reputation level
entries = [[], [], [], []]

# Read all the shoplists and save the "type" and "data" for each.
for shop in shops:
    with open(shop, 'r') as f:
        f.readline()
        contents = json.load(f)

        refs = contents["references"]["RefIds"]
        levels = extract_reputation(refs)

        for ref in refs:
            if is_shop_entry(ref["type"]["class"]):
                entries[levels[str(ref["rid"])]].append({ "type" : ref["type"], "data" : ref["data"] })

# Shuffle!
random.shuffle(entries[0])
random.shuffle(entries[1])
random.shuffle(entries[2])
random.shuffle(entries[3])

# Read the shoplist again but replace shop entries and overwrite the file.
for shop in shops:
    with open(shop, 'r') as f:
        file_header = f.readline()
        contents = json.load(f)

        levels = extract_reputation(contents["references"]["RefIds"])

        for i in range(len(contents["references"]["RefIds"])):
            if is_shop_entry(contents["references"]["RefIds"][i]["type"]["class"]):
                # Keep the rid but replace the rest
                replacement = entries[levels[str(contents["references"]["RefIds"][i]["rid"])]].pop()
                contents["references"]["RefIds"][i]["type"] = replacement["type"]
                contents["references"]["RefIds"][i]["data"] = replacement["data"]

    with open(shop, 'w', encoding="utf-8") as f:
        f.write("ShopDefinition\n")
        json.dump(contents, f, indent=4)
