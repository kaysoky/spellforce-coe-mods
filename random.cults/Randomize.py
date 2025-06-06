import random
import json
import os

cult_file = "Skills/Establish Cult/EstablishCult KotH.asset.odlo"

shop_files = [
    "Locations/TradeLists/Demonologist Shop_01.asset.odlo",
    "Locations/TradeLists/Demonologist Shop_02.asset.odlo",
]

cults = [
    "Items/Demonology/Cults/Cult_Alluvyan.asset",
    "Items/Demonology/Cults/Cult_Coldmark.asset",
    "Items/Demonology/Cults/Cult_Gillyshire.asset",
    "Items/Demonology/Cults/Cult_Goldenfields.asset",
    "Items/Demonology/Cults/Cult_MistyCoast.asset",
    "Items/Demonology/Cults/Cult_Norgate.asset",
    "Items/Demonology/Cults/Cult_Sevenkeeps.asset",
    "Items/Demonology/Cults/Cult_SilverDriftHollow.asset",
    "Items/Demonology/Cults/Cult_Southwatch.asset",
    "Items/Demonology/Cults/Cult_UramGor.asset",
    "Items/Demonology/Cults/Cult_Westguard.asset",
    "Items/Demonology/Cults/Cult_Windholme.asset",
    "Items/Demonology/Cults/Cult_DarkElf.asset",
    "Items/Demonology/Cults/Cult_Shop_01.asset",
    "Items/Demonology/Cults/Cult_Shop_02.asset",
]

# Change the directory to the script's location, to make sure we're opening files from the right relative location.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Shuffle!
random.shuffle(cults)

# Open the Establish Cult skill file and read it
with open(cult_file, 'r') as f:
    f.readline()
    skill_contents = json.load(f)

for i in range(len(skill_contents["references"]["RefIds"][0]["data"]["Mappings"])):
    skill_contents["references"]["RefIds"][0]["data"]["Mappings"][i]["Cult"]["ContentPath"] = cults.pop()

# Output the new overrides
with open(cult_file, 'w', encoding="utf-8") as f:
    f.write("WorldKingOfTheHillDefinition\n")
    json.dump(skill_contents, f, indent=4)

# Now handle the shops
for i in range(len(shop_files)):
    with open(shop_files[i], 'w', encoding="utf-8") as f:
        f.write("ShopDefinition\n")
        json.dump({
            "ArtefactModifications": [
                {
                    "UnitModifierItem": {
                        "ContentPath": cults.pop()
                    }
                }
            ]
        }, f, indent=4)
