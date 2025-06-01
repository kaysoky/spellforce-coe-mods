import random
import json

rooms = {
    "Room_Alchemy_Base.asset.odlo"             : [
        "Crafting/Rooms/Extensions/Ext_Research_01.asset", 
        "Crafting/Rooms/Extensions/Ext_CraftingSlot_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Alchemy_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Alchemy_Multiply_T1.asset"
    ],
    "Room_Alchemy_Good.asset.odlo"             : [
        "Crafting/Rooms/Extensions/Ext_Harvesting_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Alchemy_01.asset", 
        "Crafting/Rooms/Extensions/Ext_AriaIncome_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Alchemy_Multiply_T3.asset", 
        "Crafting/Rooms/Extensions/Ext_Primordial_01.asset"
    ],
    "Room_Apprentice.asset.odlo"               : [],
    "Room_Astrology_Base.asset.odlo"           : [
        "Crafting/Rooms/Extensions/Ext_Research_01.asset", 
        "Crafting/Rooms/Extensions/Ext_CraftingSlot_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Astro_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Astro_Base_01.asset"
    ],
    "Room_Astrology_Good.asset.odlo"           : [
        "Crafting/Rooms/Extensions/Ext_Astro_Good_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Astro_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Astro_Good_02.asset", 
        "Crafting/Rooms/Extensions/Ext_Astro_Good_03.asset", 
        "Crafting/Rooms/Extensions/Ext_Astro_Good_04.asset"
    ],
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
    "Room_Demonology_Base.asset.odlo"          : [
        "Crafting/Rooms/Extensions/Ext_Research_01.asset", 
        "Crafting/Rooms/Extensions/Ext_CraftingSlot_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Demon_01.asset", 
        "Crafting/Rooms/Extensions/Ext_DemonBuff_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Demon_02.asset"
    ],
    "Room_Demonology_Good.asset.odlo"          : [
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Demon_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Demon_04.asset", 
        "Crafting/Rooms/Extensions/Ext_ManaUpkeep_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Demon_Item_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Demon_03.asset", 
        "Crafting/Rooms/Extensions/Ext_DemonKin_01.asset"
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
    "Room_Necromancy_Base.asset.odlo"          : [
        "Crafting/Rooms/Extensions/Ext_CraftingSlot_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Soulfind_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Necro_01.asset", 
        "Crafting/Rooms/Extensions/Ext_ManaUpkeep_01.asset", 
        "Crafting/Rooms/Extensions/Ext_StackSlot_01.asset"
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
    "Room_Runesmithing_Base.asset.odlo"        : [
        "Crafting/Rooms/Extensions/Ext_Research_01.asset", 
        "Crafting/Rooms/Extensions/Ext_CraftingSlot_01.asset", 
        "Crafting/Rooms/Extensions/Ext_UnitArmor_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Runesmithing_01.asset"
    ],
    "Room_Runesmithing_Good.asset.odlo"        : [
        "Crafting/Rooms/Extensions/Ext_Mining_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Runesmithing_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Ore_04.asset", 
        "Crafting/Rooms/Extensions/Ext_UnitDamage_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Domain_Burn_01.asset"
    ],
    "Room_Shop.asset.odlo"                     : [
        "Crafting/Rooms/Extensions/Ext_Gold_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Shopprices_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Itemfind_02.asset", 
        "Crafting/Rooms/Extensions/Ext_RareItems_01.asset"
    ],
    "Room_Soulwell.asset.odlo"                 : [
        "Crafting/Rooms/Extensions/Ext_Soulfind_01.asset", 
        "Crafting/Rooms/Extensions/Ext_Craftspeed_Necro_01.asset", 
        "Crafting/Rooms/Extensions/Ext_ManaUpkeep_01.asset", 
        "Crafting/Rooms/Extensions/Ext_SoulIncome_T3.asset", 
        "Crafting/Rooms/Extensions/Ext_Domain_Enchantment_Soul.asset"
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
}

# Grab the room extensions in a flat list and shuffle it
room_exts = [exts for room_name in rooms for exts in rooms[room_name]]
random.shuffle(room_exts)

# Replace extensions by using the shuffled list
for room_name in rooms:
    for i in range(len(rooms[room_name])):
        rooms[room_name][i] = room_exts.pop()
        
    rooms[room_name] = {
        "AvailableExtensions" : [ { "ContentPath" : x } for x in rooms[room_name] ]
    }

    # Output the new overrides
    with open(room_name, 'w', encoding="utf-8") as f:
        f.write("RoomRecipe\n")
        json.dump(rooms[room_name], f, indent=4)
