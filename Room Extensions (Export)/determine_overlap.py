import random
import json
import os

# Change the directory to the script's location, to make sure we're opening files from the right relative location.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

extensions = [x for x in os.listdir() if x.endswith(".asset.odl")]

thresholds = {}

def convert_extension_name(extension):
    return "Crafting/Rooms/Extensions/" + extension[:-4] # Trim the .odl

for extension in extensions:
    with open(extension, 'r') as f:
        f.readline()
        contents = json.load(f)

        thresholds[extension] = contents["Thresholds"]

mapping = {}

for extension in thresholds:
    key = str(thresholds[extension]["ElementalThreshold"]) + str(thresholds[extension]["ArcaneThreshold"]) + str(thresholds[extension]["DeathThreshold"]) + str(thresholds[extension]["LifeThreshold"])

    # For cost to extension mapping
    """
    if key in mapping:
        mapping[key].append(convert_extension_name(extension))
    else:
        mapping[key] = [convert_extension_name(extension)]
    """

    # For extension to cost mapping
    mapping[convert_extension_name(extension)] = key

print(json.dumps(mapping, indent=4))