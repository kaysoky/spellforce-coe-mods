import random
import json
import os

directories = [
    "_World/Locations/TradeLists/",
    "Campaigns/MainCampaign/Mugwa Trolls/",
    "Campaigns/MainCampaign/Normal Trolls/",
    "Locations/TradeLists/",
]

minor_shops = [
    "_World/Locations/TradeLists/Alchemist.asset.odlo",
    "_World/Locations/TradeLists/Alluvyan_Herbs.asset.odlo",
    "_World/Locations/TradeLists/Alluvyan_Units.asset.odlo",
    "_World/Locations/TradeLists/Coldmark_Units.asset.odlo",
    "_World/Locations/TradeLists/ExoticStore.asset.odlo",
    "_World/Locations/TradeLists/Gillyshire_Shop.asset.odlo",
    "_World/Locations/TradeLists/Goldenfields_Food.asset.odlo",
    "_World/Locations/TradeLists/Goldenfields_Units.asset.odlo",
    "_World/Locations/TradeLists/GuildShop.asset.odlo",
    "_World/Locations/TradeLists/LoreShop.asset.odlo",
    "_World/Locations/TradeLists/MistyCoast_Slaves.asset.odlo",
    "_World/Locations/TradeLists/Runesmith.asset.odlo",
    "_World/Locations/TradeLists/Sevenkeeps_Runes.asset.odlo",
    "_World/Locations/TradeLists/Sevenkeeps_Units.asset.odlo",
    "_World/Locations/TradeLists/SilverDriftHollow_Mines.asset.odlo",
    "_World/Locations/TradeLists/Southwatch_Food.asset.odlo",
    "_World/Locations/TradeLists/Southwatch_Runesmith.asset.odlo",
    "_World/Locations/TradeLists/Westguard_Bookstore.asset.odlo",
    "_World/Locations/TradeLists/Windholme_Smith.asset.odlo",
    "Campaigns/MainCampaign/Mugwa Trolls/Mugwa_City.asset.odlo",
    "Campaigns/MainCampaign/Normal Trolls/Troll_Cannibals.asset.odlo",
    "Locations/TradeLists/DarkElf_Sinistra.asset.odlo",
    "Locations/TradeLists/Demonologist Shop_01.asset.odlo",
    "Locations/TradeLists/Demonologist Shop_02.asset.odlo",
]

minor_promotions = [
    "Units/Promotions/ResourcePromotions/Farmer.asset",
    "Units/Promotions/ResourcePromotions/IncreaseMiningYield.asset",
    "Units/Promotions/ResourcePromotions/IncreasePlantYield.asset",
    "Units/Promotions/ResourcePromotions/Miner.asset",
    "Units/Promotions/SpellPromotions/Water Walking.asset",
    "Units/Promotions/StatPromotions/Health 1.asset",
    "Units/Promotions/StatPromotions/Looter1.asset",
    "Units/Promotions/AdditionalDamage vs Demon.asset",
    "Units/Promotions/AdditionalDamage vs Fantastic.asset",
    "Units/Promotions/AdditionalDamage vs Undead.asset",
    "Units/Promotions/Backstab.asset",
    "Units/Promotions/BleedImmunity.asset",
    "Units/Promotions/Brutal.asset",
    "Units/Promotions/Fast Learner.asset",
    "Units/Promotions/Feral.asset",
    "Units/Promotions/FirstStrike.asset",
    "Units/Promotions/Focusburn.asset",
    "Units/Promotions/ForesterForStack.asset",
    "Units/Promotions/GenerateResearchPerTurn.asset",
    "Units/Promotions/Hunter.asset",
    "Units/Promotions/ImmuneToBurn.asset",
    "Units/Promotions/ImmuneToPoison.asset",
    "Units/Promotions/LessNegativeMoraleImpact.asset",
    "Units/Promotions/MountainGuide.asset",
    "Units/Promotions/NoBorderViolation.asset",
    "Units/Promotions/Parry Master.asset",
    "Units/Promotions/Phalanx.asset",
    "Units/Promotions/QuickReflexes.asset",
    "Units/Promotions/Shielded.asset",
    "Units/Promotions/Slave.asset",
    "Units/Promotions/Slayer.asset",
    "Units/Promotions/StrengthOfThePack.asset",
    "Units/Promotions/Triage.asset",
    "Units/Promotions/vsCavalry.asset",
    "Units/Promotions/VsOrcs.asset",
]

major_shops = [
    "_World/Locations/TradeLists/Gillyshire_Units.asset.odlo",
    "_World/Locations/TradeLists/MistyCoast_Shaman.asset.odlo",
    "_World/Locations/TradeLists/Sevenkeeps_Priests.asset.odlo",
    "_World/Locations/TradeLists/Southwatch_Units.asset.odlo",
    "_World/Locations/TradeLists/Westguard_Units.asset.odlo",
    "_World/Locations/TradeLists/Windholme_Units.asset.odlo",
    "Campaigns/MainCampaign/Mugwa Trolls/Mugwa_Units.asset.odlo",
    "Campaigns/MainCampaign/Normal Trolls/Troll_Units.asset.odlo",
    "Locations/TradeLists/DarkElf_Archon.asset.odlo",
    "Locations/TradeLists/DarkElf_Dracon.asset.odlo",
    "Locations/TradeLists/Uram Gor Demon Shop.asset.odlo",
]

major_promotions = [
    "Skills/Trolls/GiveTrollConsumeCorpse.asset",
    "Units/Promotions/Additional Armor Slot.asset",
    "Units/Promotions/Additional Rune Slot.asset",
    "Units/Promotions/Additional Weapon Slot.asset",
    "Units/Promotions/AdditionalDamageBasedOnMissingHealth.asset",
    "Units/Promotions/AlwaysDealMaxDamage.asset",
    "Units/Promotions/CanDaze.asset",
    "Units/Promotions/CauseTorment.asset",
    "Units/Promotions/Charge.asset",
    "Units/Promotions/Dwarven Resilience.asset",
    "Units/Promotions/Elemental Familiar Ice.asset",
    "Units/Promotions/Elemental Familiar.asset",
    "Units/Promotions/Frenzy.asset",
    "Units/Promotions/Give AbsorbPain.asset",
    "Units/Promotions/Give Cleanse Ally.asset",
    "Units/Promotions/GiveParryStance.asset",
    "Units/Promotions/GiveRaiseDead.asset",
    "Units/Promotions/GiveShieldWall.asset",
    "Units/Promotions/GiveSpiderCurse.asset",
    "Units/Promotions/GiveStealSlaveActions.asset",
    "Units/Promotions/GiveSummonDemon.asset",
    "Units/Promotions/GiveSummonSpider.asset",
    "Units/Promotions/GoblinEscort.asset",
    "Units/Promotions/Nature Familiar Wolf.asset",
    "Units/Promotions/Regeneration.asset",
    "Units/Promotions/Vigor.asset",
]

cults = [
    "Bonuses/Ability.asset",
    "Bonuses/Armor.asset",
    "Bonuses/Damage.asset",
    "Bonuses/Elemental.asset",
    "Bonuses/Focus.asset",
    "Bonuses/Healing.asset",
    "Bonuses/Health.asset",
    "Bonuses/MeleeArmor.asset",
    "Bonuses/MeleeWillpower.asset",
    "Bonuses/MissileArmor.asset",
    "Bonuses/MissileWillpower.asset",
    "Bonuses/Proficiency.asset",
    "Bonuses/Research.asset",
    "Bonuses/Scout.asset",
    "Bonuses/SoulFind.asset",
    "Bonuses/White.asset",
    "Bonuses/Willpower.asset",
]

# Change the directory to the script's location, to make sure we're opening files from the right relative location.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Make sure the relevant directories exist.
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Shuffle!
random.shuffle(minor_promotions)
random.shuffle(major_promotions)
random.shuffle(cults)

# Add minor promotions for minor shops
for shop in minor_shops:
    with open(shop, 'w', encoding="utf-8") as f:
        f.write("ShopDefinition\n")
        json.dump({
            "Modifications": [
                {
                    "ContentPath": minor_promotions.pop()
                }
            ]
        }, f, indent=4)

for shop in major_shops:
    with open(shop, 'w', encoding="utf-8") as f:
        f.write("ShopDefinition\n")
        json.dump({
            "Modifications": [
                {
                    "ContentPath": major_promotions.pop()
                }
            ],
            "ArtefactModifications": [
                {
                    "Filter": {
                        "mTags": []
                    },
                    "UnitModifierItem": {
                        "ContentPath": cults.pop()
                    }
                }
            ]
        }, f, indent=4)
