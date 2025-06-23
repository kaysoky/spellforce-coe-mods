import random
import json
import os

rooms = {
    "Room_Apprentice.asset.odlo"               : [],
    "Room_Barrack_DarkElf.asset.odlo"          : [
        "Crafting/Rooms/Extensions/Ext_HiringSlot_01.asset",
        "Crafting/Rooms/Extensions/Ext_XP_01.asset",
        "Crafting/Rooms/Extensions/Ext_Hire_DarkElves_04.asset",
        "Crafting/Rooms/Extensions/Ext_Hire_DarkElves_01.asset",
        "Crafting/Rooms/Extensions/Ext_Hire_DarkElves_02.asset",
        "Crafting/Rooms/Extensions/Ext_Hire_DarkElves_03.asset"
    ],
    "Room_Barrack_Dwarf.asset.odlo"            : [
        "Crafting/Rooms/Extensions/Ext_HiringSlot_01.asset",
        "Crafting/Rooms/Extensions/Ext_XP_01.asset",
        "Crafting/Rooms/Extensions/Ext_Glyph_01.asset",
        "Crafting/Rooms/Extensions/Ext_Hire_Dwarves_02.asset",
        "Crafting/Rooms/Extensions/Ext_Dwarf_Buff_01.asset",
        "Crafting/Rooms/Extensions/Ext_Hire_Dwarves_01.asset"
    ],
    "Room_Barrack_Elf.asset.odlo"              : [],
    "Room_Barrack_Human.asset.odlo"            : [
        "Crafting/Rooms/Extensions/Ext_HiringSlot_01.asset",
        "Crafting/Rooms/Extensions/Ext_XP_01.asset",
        "Crafting/Rooms/Extensions/Ext_HireWorkers.asset",
        "Crafting/Rooms/Extensions/Ext_Hire_Humans_01.asset",
        "Crafting/Rooms/Extensions/Ext_XP_Bonus_01.asset",
        "Crafting/Rooms/Extensions/Ext_Hire_Humans_02.asset"
    ],
    "Room_Barrack_Orc.asset.odlo"              : [
        "Crafting/Rooms/Extensions/Ext_HiringSlot_01.asset",
        "Crafting/Rooms/Extensions/Ext_XP_01.asset",
        "Crafting/Rooms/Extensions/Ext_Hire_Orc_03.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_Traps_01.asset",
        "Crafting/Rooms/Extensions/Ext_Hire_Orc_01.asset",
        "Crafting/Rooms/Extensions/Ext_Hire_Orc_02.asset"
    ],
    "Room_Barrack_Troll.asset.odlo"            : [
        "Crafting/Rooms/Extensions/Ext_HiringSlot_01.asset",
        "Crafting/Rooms/Extensions/Ext_XP_01.asset",
        "Crafting/Rooms/Extensions/Ext_Troll_Work_01.asset",
        "Crafting/Rooms/Extensions/Ext_Troll_Stomp_01.asset",
        "Crafting/Rooms/Extensions/Ext_Troll_Feral_01.asset",
        "Crafting/Rooms/Extensions/Ext_Troll_Kitchen_01.asset"
    ],
    "Room_BloodPool.asset.odlo"                : [
        "Crafting/Rooms/Extensions/Ext_Domain_Bleed_01.asset",
        "Crafting/Rooms/Extensions/Ext_Arcane_Blood_01.asset",
        "Crafting/Rooms/Extensions/Ext_BloodRage_01.asset"
    ],
    "Room_CombatSchool.asset.odlo"             : [
        "Crafting/Rooms/Extensions/Ext_XP_02.asset",
        "Crafting/Rooms/Extensions/Ext_Archery_01.asset",
        "Crafting/Rooms/Extensions/Ext_Melee_01.asset",
        "Crafting/Rooms/Extensions/Ext_Rider_01.asset"
    ],
    "Room_DarknessGenerator.asset.odlo"        : [
        "Crafting/Rooms/Extensions/Ext_Domain_Ray_Death_01.asset",
        "Crafting/Rooms/Extensions/Ext_ManaUpkeep_01.asset",
        "Crafting/Rooms/Extensions/Ext_BE_Fumes_01.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_Fear_01.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_Tower_01.asset"
    ],
    "Room_Dreamweaving_Observatory.asset.odlo" : [
        "Crafting/Rooms/Extensions/Ext_CrystalBall_01.asset",
        "Crafting/Rooms/Extensions/Dreamweaver_Loom.asset",
        "Crafting/Rooms/Extensions/Dreamweaver_Units.asset",
        "Crafting/Rooms/Extensions/Dreamweaver_Stars.asset",
        "Crafting/Rooms/Extensions/Dreamweaver_Sleep.asset"
    ],
    "Room_Expedition.asset.odlo"               : [
        "Crafting/Rooms/Extensions/Ext_Mining_01.asset",
        "Crafting/Rooms/Extensions/Ext_Itemfind_02.asset",
        "Crafting/Rooms/Extensions/Ext_Ore_01.asset",
        "Crafting/Rooms/Extensions/Ext_Ore_02.asset",
        "Crafting/Rooms/Extensions/Ext_Ore_03.asset"
    ],
    "Room_Fortification.asset.odlo"            : [
        "Crafting/Rooms/Extensions/Ext_RoomCrafting_01.asset",
        "Crafting/Rooms/Extensions/Ext_BE_Walls_01.asset",
        "Crafting/Rooms/Extensions/Ext_BE_Snipers_01.asset",
        "Crafting/Rooms/Extensions/Ext_GuardDogs.asset",
        "Crafting/Rooms/Extensions/Ext_BE_Catapult_01.asset"
    ],
    "Room_HerbGarden.asset.odlo"               : [
        "Crafting/Rooms/Extensions/Ext_Plant_Pumpkin.asset",
        "Crafting/Rooms/Extensions/Ext_Plant_Windweed.asset",
        "Crafting/Rooms/Extensions/Ext_Plant_Mushroom.asset",
        "Crafting/Rooms/Extensions/Ext_Plant_Healroot.asset",
        "Crafting/Rooms/Extensions/Ext_Plant_Lenya.asset"
    ],
    "Room_Inn.asset.odlo"                      : [
        "Crafting/Rooms/Extensions/Ext_Domain_Heal_01.asset",
        "Crafting/Rooms/Extensions/Ext_Hire_Dwarves_02.asset",
        "Crafting/Rooms/Extensions/Ext_Itemfind_02.asset",
        "Crafting/Rooms/Extensions/Ext_GoldUpkeep_01.asset",
        "Crafting/Rooms/Extensions/Ext_Ore_03.asset"
    ],
    "Room_Kennel.asset.odlo"                   : [
        "Crafting/Rooms/Extensions/Ext_Hire_Animals_01.asset",
        "Crafting/Rooms/Extensions/Ext_Hire_Animals_02.asset",
        "Crafting/Rooms/Extensions/Ext_Hire_Animals_03.asset",
        "Crafting/Rooms/Extensions/Ext_Beast_Buff_01.asset",
        "Crafting/Rooms/Extensions/Ext_Beast_Slave_01.asset",
        "Crafting/Rooms/Extensions/Ext_Beast_Follower_01.asset"
    ],
    "Room_Library.asset.odlo"                  : [
        "Crafting/Rooms/Extensions/Ext_Research_01.asset",
        "Crafting/Rooms/Extensions/Ext_CrystalBall_01.asset",
        "Crafting/Rooms/Extensions/Ext_Research_02.asset",
        "Crafting/Rooms/Extensions/Ext_Proficiency_02.asset",
        "Crafting/Rooms/Extensions/Ext_SummonBuff_01.asset",
        "Crafting/Rooms/Extensions/Ext_ApprenticeBuff_01.asset"
    ],
    "Room_LightningGenerator.asset.odlo"       : [
        "Crafting/Rooms/Extensions/Ext_Domain_Ray_White_01.asset",
        "Crafting/Rooms/Extensions/Ext_BE_Lightning_01.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_MagicAmp_01.asset"
    ],
    "Room_Might_Base.asset.odlo"               : [
        "Crafting/Rooms/Extensions/Ext_Research_01.asset",
        "Crafting/Rooms/Extensions/Ext_Mana_01.asset",
        "Crafting/Rooms/Extensions/Ext_Might_01.asset",
        "Crafting/Rooms/Extensions/Ext_MiningTicks_01.asset",
        "Crafting/Rooms/Extensions/Ext_ApprenticeBuff_02.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_Tower_01.asset"
    ],
    "Room_MindMachine.asset.odlo"              : [
        "Crafting/Rooms/Extensions/Ext_Domain_SEimmune_01.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_Fear_01.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_NoUpkeep_01.asset"
    ],
    "Room_Occultism_Apprentice.asset.odlo"     : [
        "Crafting/Rooms/Extensions/Ext_Research_01.asset",
        "Crafting/Rooms/Extensions/Ext_ApprenticeBuff_04.asset",
        "Crafting/Rooms/Extensions/Ext_Lodge_Buff_01.asset",
        "Crafting/Rooms/Extensions/Ext_DarkBuff_01.asset",
        "Crafting/Rooms/Extensions/Ext_Secret_Room_01.asset"
    ],
    "Room_Occultism_DemonPact.asset.odlo"      : [
        "Crafting/Rooms/Extensions/Ext_DemonPact_01.asset",
        "Crafting/Rooms/Extensions/Ext_DemonPact_02.asset",
        "Crafting/Rooms/Extensions/Ext_DemonPact_06.asset",
        "Crafting/Rooms/Extensions/Ext_DemonPact_04.asset",
        "Crafting/Rooms/Extensions/Ext_DemonPact_05.asset"
    ],
    "Room_Shop.asset.odlo"                     : [
        "Crafting/Rooms/Extensions/Ext_Gold_01.asset",
        "Crafting/Rooms/Extensions/Ext_Shopprices_01.asset",
        "Crafting/Rooms/Extensions/Ext_Itemfind_02.asset",
        "Crafting/Rooms/Extensions/Ext_RareItems_01.asset"
    ],
    "Room_Story_B.asset.odlo"                  : [
        "Crafting/Rooms/Extensions/Ext_CrystalIncome_01.asset",
        "Crafting/Rooms/Extensions/Ext_Mana_01.asset",
        "Crafting/Rooms/Extensions/Ext_Focus_01.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_MagicShield_01.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_MagicShield_02.asset"
    ],
    "Room_Study.asset.odlo"                    : [
        "Crafting/Rooms/Extensions/Ext_Research_01.asset",
        "Crafting/Rooms/Extensions/Ext_Soulfind_01.asset",
        "Crafting/Rooms/Extensions/Ext_Itemfind_01.asset",
        "Crafting/Rooms/Extensions/Ext_Proficiency_01.asset"
    ],
    "Room_SummoningCircle.asset.odlo"          : [
        "Crafting/Rooms/Extensions/Ext_Summon_Buff_02.asset",
        "Crafting/Rooms/Extensions/Ext_ManaUpkeep_01.asset",
        "Crafting/Rooms/Extensions/Ext_BE_Phantoms_01.asset"
    ],
    "Room_TortureChamber.asset.odlo"           : [
        "Crafting/Rooms/Extensions/Ext_Soulfind_01.asset",
        "Crafting/Rooms/Extensions/Ext_IronMaiden_03.asset",
        "Crafting/Rooms/Extensions/Ext_Hire_Undead_01.asset",
        "Crafting/Rooms/Extensions/Ext_IronMaiden_01.asset",
        "Crafting/Rooms/Extensions/Ext_IronMaiden_02.asset",
        "Crafting/Rooms/Extensions/Ext_ApprenticeBuff_03.asset"
    ],
    "Room_TroopUpkeep.asset.odlo"              : [
        "Crafting/Rooms/Extensions/Ext_HiringSlot_01.asset",
        "Crafting/Rooms/Extensions/Ext_XP_01.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_Heal_01.asset",
        "Crafting/Rooms/Extensions/Ext_BE_Snipers_01.asset"
    ],
    "Room_Vault.asset.odlo"                    : [
        "Crafting/Rooms/Extensions/Ext_Itemfind_01.asset",
        "Crafting/Rooms/Extensions/Ext_GoldSniffer_01.asset",
        "Crafting/Rooms/Extensions/Ext_Itemfind_02.asset",
        "Crafting/Rooms/Extensions/Ext_Gold_02.asset"
    ],
    "Room_Workshop.asset.odlo"                 : [
        "Crafting/Rooms/Extensions/Ext_CraftingSlot_01.asset",
        "Crafting/Rooms/Extensions/Ext_Gold_01.asset",
        "Crafting/Rooms/Extensions/Ext_RoomCrafting_01.asset"
    ],
    "TEST ROOM CRYSTAL.asset.odlo"             : [
        "Crafting/Rooms/Extensions/Ext_TowerMovement_01.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_Heal_02.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_Ray_Ele_01.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_Ray_White_01.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_Ray_Death_01.asset",
        "Crafting/Rooms/Extensions/Ext_Landmark_01.asset"
    ],
    # Class-specific rooms
    "Room_Alchemy_Base.asset.odlo"             : [
        "Crafting/Rooms/Extensions/Ext_CraftingSlot_01.asset",
        "Crafting/Rooms/Extensions/Ext_Research_01.asset"
    ],
    "Room_Alchemy_Good.asset.odlo"             : [
        "Crafting/Rooms/Extensions/Ext_Harvesting_01.asset",
        "Crafting/Rooms/Extensions/Ext_AriaIncome_01.asset",
        "Crafting/Rooms/Extensions/Ext_Primordial_01.asset"
    ],
    "Room_Astrology_Base.asset.odlo"           : [
        "Crafting/Rooms/Extensions/Ext_CraftingSlot_01.asset",
        "Crafting/Rooms/Extensions/Ext_Research_01.asset"
    ],
    "Room_Astrology_Good.asset.odlo"           : [],
    "Room_Demonology_Base.asset.odlo"          : [
        "Crafting/Rooms/Extensions/Ext_CraftingSlot_01.asset",
        "Crafting/Rooms/Extensions/Ext_Research_01.asset",
        "Crafting/Rooms/Extensions/Ext_DemonBuff_01.asset"
    ],
    "Room_Demonology_Good.asset.odlo"          : [
        "Crafting/Rooms/Extensions/Ext_ManaUpkeep_01.asset",
        "Crafting/Rooms/Extensions/Ext_DemonKin_01.asset"
    ],
    "Room_Necromancy_Base.asset.odlo"          : [
        "Crafting/Rooms/Extensions/Ext_CraftingSlot_01.asset",
        "Crafting/Rooms/Extensions/Ext_Soulfind_01.asset",
        "Crafting/Rooms/Extensions/Ext_ManaUpkeep_01.asset",
        "Crafting/Rooms/Extensions/Ext_StackSlot_01.asset"
    ],
    "Room_Soulwell.asset.odlo"                 : [
        "Crafting/Rooms/Extensions/Ext_Soulfind_01.asset",
        "Crafting/Rooms/Extensions/Ext_ManaUpkeep_01.asset",
        "Crafting/Rooms/Extensions/Ext_SoulIncome_T3.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_Enchantment_Soul.asset"
    ],
    "Room_Runesmithing_Base.asset.odlo"        : [
        "Crafting/Rooms/Extensions/Ext_CraftingSlot_01.asset",
        "Crafting/Rooms/Extensions/Ext_Research_01.asset",
        "Crafting/Rooms/Extensions/Ext_UnitArmor_01.asset"
    ],
    "Room_Runesmithing_Good.asset.odlo"        : [
        "Crafting/Rooms/Extensions/Ext_Mining_01.asset",
        "Crafting/Rooms/Extensions/Ext_Ore_04.asset",
        "Crafting/Rooms/Extensions/Ext_UnitDamage_01.asset"
    ],
}

# Class-specific extensions
class_rooms = {
    "Room_Alchemy_Base.asset.odlo"             : [
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Alchemy_01.asset",
        "Crafting/Rooms/Extensions/Ext_Alchemy_Multiply_T1.asset"
    ],
    "Room_Alchemy_Good.asset.odlo"             : [
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Alchemy_01.asset",
        "Crafting/Rooms/Extensions/Ext_Alchemy_Multiply_T3.asset"
    ],
    "Room_Astrology_Base.asset.odlo"           : [
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Astro_01.asset",
        "Crafting/Rooms/Extensions/Ext_Astro_Base_01.asset"
    ],
    "Room_Astrology_Good.asset.odlo"           : [
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Astro_01.asset",
        "Crafting/Rooms/Extensions/Ext_Astro_Good_01.asset",
        "Crafting/Rooms/Extensions/Ext_Astro_Good_02.asset",
        "Crafting/Rooms/Extensions/Ext_Astro_Good_03.asset",
        "Crafting/Rooms/Extensions/Ext_Astro_Good_04.asset"
    ],
    "Room_Demonology_Base.asset.odlo"          : [
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Demon_01.asset",
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Demon_02.asset"
    ],
    "Room_Demonology_Good.asset.odlo"          : [
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Demon_01.asset",
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Demon_04.asset",
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Demon_03.asset"
    ],
    "Room_Necromancy_Base.asset.odlo"          : [
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Necro_01.asset"
    ],
    "Room_Soulwell.asset.odlo"                 : [
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Necro_01.asset"
    ],
    "Room_Runesmithing_Base.asset.odlo"        : [
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Runesmithing_01.asset"
    ],
    "Room_Runesmithing_Good.asset.odlo"        : [
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Runesmithing_01.asset",
        "Crafting/Rooms/Extensions/Ext_Domain_Burn_01.asset"
    ],
}

extension_to_cost = {
    "Crafting/Rooms/Extensions/Dreamweaver_Loom.asset": "0102",
    "Crafting/Rooms/Extensions/Dreamweaver_Sleep.asset": "0203",
    "Crafting/Rooms/Extensions/Dreamweaver_Stars.asset": "3100",
    "Crafting/Rooms/Extensions/Dreamweaver_Units.asset": "0210",
    "Crafting/Rooms/Extensions/Ext_Alchemy_Multiply_T1.asset": "0003",
    "Crafting/Rooms/Extensions/Ext_Alchemy_Multiply_T3.asset": "1102",
    "Crafting/Rooms/Extensions/Ext_ApprenticeBuff_01.asset": "2210",
    "Crafting/Rooms/Extensions/Ext_ApprenticeBuff_02.asset": "2300",
    "Crafting/Rooms/Extensions/Ext_ApprenticeBuff_03.asset": "2003",
    "Crafting/Rooms/Extensions/Ext_ApprenticeBuff_04.asset": "0002",
    "Crafting/Rooms/Extensions/Ext_Arcane_Blood_01.asset": "0301",
    "Crafting/Rooms/Extensions/Ext_Archery_01.asset": "2200",
    "Crafting/Rooms/Extensions/Ext_AriaIncome_01.asset": "0202",
    "Crafting/Rooms/Extensions/Ext_Astro_Base_01.asset": "0300",
    "Crafting/Rooms/Extensions/Ext_Astro_Good_01.asset": "1200",
    "Crafting/Rooms/Extensions/Ext_Astro_Good_02.asset": "0220",
    "Crafting/Rooms/Extensions/Ext_Astro_Good_03.asset": "2202",
    "Crafting/Rooms/Extensions/Ext_Astro_Good_04.asset": "3303",
    "Crafting/Rooms/Extensions/Ext_Beast_Buff_01.asset": "0210",
    "Crafting/Rooms/Extensions/Ext_Beast_Follower_01.asset": "3003",
    "Crafting/Rooms/Extensions/Ext_Beast_Slave_01.asset": "0030",
    "Crafting/Rooms/Extensions/Ext_BE_Catapult_01.asset": "3020",
    "Crafting/Rooms/Extensions/Ext_BE_Fumes_01.asset": "3020",
    "Crafting/Rooms/Extensions/Ext_BE_Lightning_01.asset": "0320",
    "Crafting/Rooms/Extensions/Ext_BE_Phantoms_01.asset": "0320",
    "Crafting/Rooms/Extensions/Ext_BE_Snipers_01.asset": "2010",
    "Crafting/Rooms/Extensions/Ext_BE_Walls_01.asset": "2100",
    "Crafting/Rooms/Extensions/Ext_BloodRage_01.asset": "0203",
    "Crafting/Rooms/Extensions/Ext_CraftingSlot_01.asset": "1000",
    "Crafting/Rooms/Extensions/Ext_Craftspeed_Alchemy_01.asset": "0102",
    "Crafting/Rooms/Extensions/Ext_Craftspeed_Astro_01.asset": "0102",
    "Crafting/Rooms/Extensions/Ext_Craftspeed_Demon_01.asset": "2010",
    "Crafting/Rooms/Extensions/Ext_Craftspeed_Demon_02.asset": "1220",
    "Crafting/Rooms/Extensions/Ext_Craftspeed_Demon_03.asset": "2201",
    "Crafting/Rooms/Extensions/Ext_Craftspeed_Demon_04.asset": "2100",
    "Crafting/Rooms/Extensions/Ext_Craftspeed_Necro_01.asset": "0120",
    "Crafting/Rooms/Extensions/Ext_Craftspeed_Runesmithing_01.asset": "2100",
    "Crafting/Rooms/Extensions/Ext_CrystalBall_01.asset": "0200",
    "Crafting/Rooms/Extensions/Ext_CrystalIncome_01.asset": "0110",
    "Crafting/Rooms/Extensions/Ext_DarkBuff_01.asset": "0220",
    "Crafting/Rooms/Extensions/Ext_DemonBuff_01.asset": "3000",
    "Crafting/Rooms/Extensions/Ext_DemonKin_01.asset": "3003",
    "Crafting/Rooms/Extensions/Ext_DemonPact_01.asset": "1100",
    "Crafting/Rooms/Extensions/Ext_DemonPact_02.asset": "0200",
    "Crafting/Rooms/Extensions/Ext_DemonPact_03.asset": "1002",
    "Crafting/Rooms/Extensions/Ext_DemonPact_04.asset": "2100",
    "Crafting/Rooms/Extensions/Ext_DemonPact_05.asset": "2300",
    "Crafting/Rooms/Extensions/Ext_DemonPact_06.asset": "1002",
    "Crafting/Rooms/Extensions/Ext_Demon_Item_01.asset": "3020",
    "Crafting/Rooms/Extensions/Ext_Domain_Bleed_01.asset": "0130",
    "Crafting/Rooms/Extensions/Ext_Domain_Burn_01.asset": "3120",
    "Crafting/Rooms/Extensions/Ext_Domain_Enchantment_Soul.asset": "1220",
    "Crafting/Rooms/Extensions/Ext_Domain_Fear_01.asset": "2030",
    "Crafting/Rooms/Extensions/Ext_Domain_Heal_01.asset": "0002",
    "Crafting/Rooms/Extensions/Ext_Domain_Heal_02.asset": "0103",
    "Crafting/Rooms/Extensions/Ext_Domain_MagicAmp_01.asset": "0303",
    "Crafting/Rooms/Extensions/Ext_Domain_MagicShield_01.asset": "0202",
    "Crafting/Rooms/Extensions/Ext_Domain_MagicShield_02.asset": "0220",
    "Crafting/Rooms/Extensions/Ext_Domain_NoUpkeep_01.asset": "0303",
    "Crafting/Rooms/Extensions/Ext_Domain_Ray_Death_01.asset": "0220",
    "Crafting/Rooms/Extensions/Ext_Domain_Ray_Ele_01.asset": "2200",
    "Crafting/Rooms/Extensions/Ext_Domain_Ray_White_01.asset": "0202",
    "Crafting/Rooms/Extensions/Ext_Domain_SEimmune_01.asset": "0201",
    "Crafting/Rooms/Extensions/Ext_Domain_Tower_01.asset": "0302",
    "Crafting/Rooms/Extensions/Ext_Domain_Traps_01.asset": "2002",
    "Crafting/Rooms/Extensions/Ext_Domain_Willpower_01.asset": "0002",
    "Crafting/Rooms/Extensions/Ext_Dwarf_Buff_01.asset": "1110",
    "Crafting/Rooms/Extensions/Ext_Focus_01.asset": "1101",
    "Crafting/Rooms/Extensions/Ext_Glyph_01.asset": "2100",
    "Crafting/Rooms/Extensions/Ext_GoldSniffer_01.asset": "2200",
    "Crafting/Rooms/Extensions/Ext_GoldUpkeep_01.asset": "2101",
    "Crafting/Rooms/Extensions/Ext_Gold_01.asset": "0102",
    "Crafting/Rooms/Extensions/Ext_Gold_02.asset": "3102",
    "Crafting/Rooms/Extensions/Ext_GuardDogs.asset": "2002",
    "Crafting/Rooms/Extensions/Ext_Harvesting_01.asset": "1002",
    "Crafting/Rooms/Extensions/Ext_HireWorkers.asset": "2001",
    "Crafting/Rooms/Extensions/Ext_Hire_Animals_01.asset": "2001",
    "Crafting/Rooms/Extensions/Ext_Hire_Animals_02.asset": "2010",
    "Crafting/Rooms/Extensions/Ext_Hire_Animals_03.asset": "2100",
    "Crafting/Rooms/Extensions/Ext_Hire_DarkElves_01.asset": "0030",
    "Crafting/Rooms/Extensions/Ext_Hire_DarkElves_02.asset": "3010",
    "Crafting/Rooms/Extensions/Ext_Hire_DarkElves_03.asset": "2300",
    "Crafting/Rooms/Extensions/Ext_Hire_DarkElves_04.asset": "0102",
    "Crafting/Rooms/Extensions/Ext_Hire_Dwarves_01.asset": "3200",
    "Crafting/Rooms/Extensions/Ext_Hire_Dwarves_02.asset": "0003",
    "Crafting/Rooms/Extensions/Ext_Hire_Humans_01.asset": "1110",
    "Crafting/Rooms/Extensions/Ext_Hire_Humans_02.asset": "2030",
    "Crafting/Rooms/Extensions/Ext_Hire_Orc_01.asset": "1120",
    "Crafting/Rooms/Extensions/Ext_Hire_Orc_02.asset": "3020",
    "Crafting/Rooms/Extensions/Ext_Hire_Orc_03.asset": "2010",
    "Crafting/Rooms/Extensions/Ext_Hire_Undead_01.asset": "0120",
    "Crafting/Rooms/Extensions/Ext_HiringSlot_01.asset": "0001",
    "Crafting/Rooms/Extensions/Ext_IronMaiden_01.asset": "2010",
    "Crafting/Rooms/Extensions/Ext_IronMaiden_02.asset": "0220",
    "Crafting/Rooms/Extensions/Ext_IronMaiden_03.asset": "1010",
    "Crafting/Rooms/Extensions/Ext_Itemfind_01.asset": "1001",
    "Crafting/Rooms/Extensions/Ext_Itemfind_02.asset": "2002",
    "Crafting/Rooms/Extensions/Ext_Landmark_01.asset": "2202",
    "Crafting/Rooms/Extensions/Ext_Lodge_Buff_01.asset": "0201",
    "Crafting/Rooms/Extensions/Ext_ManaUpkeep_01.asset": "1210",
    "Crafting/Rooms/Extensions/Ext_Mana_01.asset": "0102",
    "Crafting/Rooms/Extensions/Ext_Melee_01.asset": "2020",
    "Crafting/Rooms/Extensions/Ext_Might_01.asset": "0301",
    "Crafting/Rooms/Extensions/Ext_MiningTicks_01.asset": "3002",
    "Crafting/Rooms/Extensions/Ext_Mining_01.asset": "1002",
    "Crafting/Rooms/Extensions/Ext_Ore_01.asset": "3000",
    "Crafting/Rooms/Extensions/Ext_Ore_02.asset": "3100",
    "Crafting/Rooms/Extensions/Ext_Ore_03.asset": "1120",
    "Crafting/Rooms/Extensions/Ext_Ore_04.asset": "1120",
    "Crafting/Rooms/Extensions/Ext_Plant_Catalysts.asset": "0002",
    "Crafting/Rooms/Extensions/Ext_Plant_Healroot.asset": "0003",
    "Crafting/Rooms/Extensions/Ext_Plant_Honey.asset": "2100",
    "Crafting/Rooms/Extensions/Ext_Plant_Lenya.asset": "1201",
    "Crafting/Rooms/Extensions/Ext_Plant_Mushroom.asset": "1020",
    "Crafting/Rooms/Extensions/Ext_Plant_Pumpkin.asset": "2000",
    "Crafting/Rooms/Extensions/Ext_Plant_Windweed.asset": "0200",
    "Crafting/Rooms/Extensions/Ext_Primordial_01.asset": "2003",
    "Crafting/Rooms/Extensions/Ext_Proficiency_01.asset": "0200",
    "Crafting/Rooms/Extensions/Ext_Proficiency_02.asset": "0210",
    "Crafting/Rooms/Extensions/Ext_RareItems_01.asset": "0220",
    "Crafting/Rooms/Extensions/Ext_Research_01.asset": "0100",
    "Crafting/Rooms/Extensions/Ext_Research_02.asset": "0201",
    "Crafting/Rooms/Extensions/Ext_Rider_01.asset": "2002",
    "Crafting/Rooms/Extensions/Ext_RoomCrafting_01.asset": "2001",
    "Crafting/Rooms/Extensions/Ext_Secret_Room_01.asset": "3200",
    "Crafting/Rooms/Extensions/Ext_Shopprices_01.asset": "0003",
    "Crafting/Rooms/Extensions/Ext_Soulfind_01.asset": "0110",
    "Crafting/Rooms/Extensions/Ext_SoulIncome_T3.asset": "0202",
    "Crafting/Rooms/Extensions/Ext_StackSlot_01.asset": "3101",
    "Crafting/Rooms/Extensions/Ext_SummonBuff_01.asset": "1300",
    "Crafting/Rooms/Extensions/Ext_Summon_Buff_02.asset": "0200",
    "Crafting/Rooms/Extensions/Ext_TowerMovement_01.asset": "1200",
    "Crafting/Rooms/Extensions/Ext_Troll_Feral_01.asset": "1003",
    "Crafting/Rooms/Extensions/Ext_Troll_Kitchen_01.asset": "0230",
    "Crafting/Rooms/Extensions/Ext_Troll_Stomp_01.asset": "2010",
    "Crafting/Rooms/Extensions/Ext_Troll_Work_01.asset": "1002",
    "Crafting/Rooms/Extensions/Ext_UnitArmor_01.asset": "3000",
    "Crafting/Rooms/Extensions/Ext_UnitDamage_01.asset": "3200",
    "Crafting/Rooms/Extensions/Ext_XP_01.asset": "2000",
    "Crafting/Rooms/Extensions/Ext_XP_02.asset": "3000",
    "Crafting/Rooms/Extensions/Ext_XP_Bonus_01.asset": "1002"
}

# Change the directory to the script's location, to make sure we're opening files from the right relative location.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Grab a list of room names, which will be one axis of randomization
room_names = [x for x in rooms]

# Bucket the random extensions into groups with the same cost
buckets = {}
for room_name in rooms:
    for i in range(len(rooms[room_name])):
        extension = rooms[room_name][i]
        cost = extension_to_cost[extension]
        if cost in buckets:
            buckets[cost].append(extension)
        else:
            buckets[cost] = [extension]

# Determine which buckets to randomize first, based on which ones contain overlap with class-specific extensions
priority_buckets = set([])
for room_name in class_rooms:
    for i in range(len(class_rooms[room_name])):
        priority_buckets.add(extension_to_cost[class_rooms[room_name][i]])

# Create a separate dictionary with the randomized rooms
random_rooms = { x: [] for x in room_names }

# Now place the priority buckets into the randomized rooms
for bucket in priority_buckets:
    # Change the order we check rooms each time
    random.shuffle(room_names)

    for i in range(len(room_names)):
        if bucket not in buckets or len(buckets[bucket]) <= 0:
            # No more extensions to place from this bucket
            break

        if room_names[i] in class_rooms:
            if any(bucket == extension_to_cost[x] for x in class_rooms[room_names[i]]):
                # This room will have an overlap with the current bucket, so skip it
                continue

        # This room isn't full yet, so add the extension
        if len(random_rooms[room_names[i]]) < len(rooms[room_names[i]]):
            random_rooms[room_names[i]].append(buckets[bucket].pop())
            continue

    if bucket in buckets and len(buckets[bucket]) > 0:
        print("Uh oh, couldn't find a match for " + json.dumps(buckets[bucket]))

# Now handle the rest of the buckets
# The buckets are sorted so the ones with the most extensions are placed first
# This should (almost) guarantee that all of them get placed
for bucket in sorted(buckets, reverse=True, key=lambda x: len(buckets[x])):
    # Change the order we check rooms each time
    random.shuffle(room_names)

    for i in range(len(room_names)):
        if len(buckets[bucket]) <= 0:
            # No more extensions to place from this bucket
            break

        # This room isn't full yet, so add the extension
        if len(random_rooms[room_names[i]]) < len(rooms[room_names[i]]):
            random_rooms[room_names[i]].append(buckets[bucket].pop())
            continue

    if len(buckets[bucket]) > 0:
        print("Uh oh, couldn't find a match for " + json.dumps(buckets[bucket]))

# Finally, output the new overrides
for room_name in random_rooms:
    # Add class-specific extensions back into the list
    if room_name in class_rooms:
        random_rooms[room_name] += class_rooms[room_name]

    random_rooms[room_name] = {
        "AvailableExtensions" : [ { "ContentPath" : x } for x in random_rooms[room_name] ]
    }

    # Output the new overrides
    with open("Crafting/Rooms/" + room_name, 'w', encoding="utf-8") as f:
        f.write("RoomRecipe\n")
        json.dump(random_rooms[room_name], f, indent=4)
