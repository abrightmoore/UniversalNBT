# coding=UTF-8
import UNBT
from random import randint
import textwrap
import os
import directories
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

# @TheWorldFoundry

inputs = (
			("I-AM-THE-LORE", "label"),

			("Item ID:",("string","value=golden_sword")),
			("Item Hint (not used):",
						(
							u'daylight_detector', u'end_rod', u'totem', u'red_sandstone_stairs', u'carpet', u'golden_helmet', u'golden_pickaxe', u'emerald_block', u'melon', u'gravel', u'iron_leggings', u'double_plant', u'hopper', u'activator_rail', u'wooden_hoe', u'emerald_ore', u'golden_boots', u'dark_oak_fence_gate', u'diamond_leggings', u'tallgrass', u'sand', u'lever', u'beetroot_soup', u'wooden_slab', u'spider_eye', u'fence', u'noteblock', u'sign', u'daylight_detector_inverted', u'cactus', u'info_update', u'clock', u'stone_hoe', u'netherbrick', u'water', u'beacon', u'diamond_horse_armor', u'light_weighted_pressure_plate', u'ghast_tear', u'leaves', u'bow', u'deadbush', u'ender_eye', u'powered_comparator', u'end_portal_frame', u'red_sandstone', u'apple', u'lime_glazed_terracotta', u'chorus_flower', u'jungle_door', u'end_gateway', u'chainmail_leggings', u'camera', u'bedrock', u'dragon_breath', u'border_block', u'diamond_hoe', u'lit_redstone_torch', u'diamond', u'rabbit_hide', u'glass', u'stick', u'rabbit', u'glass_bottle', u'muttonraw', u'tnt', u'quartz_ore', u'netherreactor', u'pumpkin', u'diamond_ore', u'dropper', u'reeds', u'unlit_redstone_lamp', u'unpowered_repeater', u'wooden_pressure_plate', u'carrot', u'sticky_piston', u'flowing_lava', u'string', u'grass_path', u'sandstone', u'furnace', u'nether_brick_stairs', u'redstone_torch', u'ladder', u'concrete_powder', u'birch_stairs', u'iron_helmet', u'spawn_egg', u'prismarine', u'coal', u'gold_block', u'fireball', u'egg', u'magma_cream', u'netherrack', u'paper', u'podzol', u'command_block', u'brick_stairs', u'wooden_door', u'slimeball', u'trapped_chest', u'end_stone', u'gold_nugget', u'cooked_rabbit', u'chest_minecart', u'unlit_redstone_torch', u'double_stone_slab2', u'stone_pickaxe', u'wooden_sword', u'snowball', u'birch_door', u'flint', u'emerald', u'bread', u'melon_seeds', u'quartz_block', u'stone_slab', u'potatoes', u'enchanting_table', u'iron_boots', u'invisiblebedrock', u'fishing_rod', u'arrow', u'bone', u'pistonarmcollision', u'purpur_block', u'hay_block', u'golden_hoe', u'fish', u'torch', u'rabbit_foot', u'flowing_water', u'lapis_block', u'fermented_spider_eye', u'poisonous_potato', u'diamond_shovel', u'lit_pumpkin', u'iron_sword', u'iron_bars', u'log2', u'dirt', u'redstone_ore', u'name_tag', u'iron_hoe', u'cookie', u'shulker_box', u'chorus_fruit', u'farmland', u'stonecutter', u'clownfish', u'shears', u'slime_ball', u'red_flower', u'rabbit_stew', u'wooden_button', u'end_portal', u'stone_brick_stairs', u'stone_sword', u'double_stone_slab', u'stonebrick', u'enchanted_book', u'beetroot_seeds', u'golden_apple', u'stone_pressure_plate', u'wooden_pickaxe', u'pumpkin_pie', u'bed', u'iron_axe', u'dispenser', u'jungle_fence_gate', u'diamond_sword', u'brewing_stand', u'wooden_axe', u'carrots', u'purple_glazed_terracotta', u'blue_glazed_terracotta', u'stone_slab2', u'standing_sign', u'soul_sand', u'chainmail_chestplate', u'leaves2', u'melon_stem', u'hardened_clay', u'snow', u'chest', u'fence_gate', u'mycelium', u'written_book', u'cooked_fish', u'allow', u'iron_block', u'lapis_ore', u'salmon', u'red_glazed_terracotta', u'stained_hardened_clay', u'deny', u'red_mushroom', u'iron_ore', u'obsidian', u'painting', u'planks', u'rotten_flesh', u'gold_ingot', u'chain_command_block', u'cooked_porkchop', u'portfolio', u'chicken', u'anvil', u'minecart', u'sugar', u'black_glazed_terracotta', u'wool', u'stone_shovel', u'acacia_fence_gate', u'stained_glass', u'diamond_helmet', u'compass', u'dye', u'end_crystal', u'heavy_weighted_pressure_plate', u'leather', u'golden_leggings', u'chainmail_boots', u'stone_axe', u'netherStar', u'observer', u'frame', u'vine', u'gray_glazed_terracotta', u'pink_glazed_terracotta', u'iron_trapdoor', u'mutton', u'waterlily', u'cooked_chicken', u'redstone_wire', u'piston', u'acacia_door', u'wooden_shovel', u'glowstone', u'green_glazed_terracotta', u'frosted_ice', u'stone_stairs', u'light_blue_glazed_terracotta', u'nether_brick_fence', u'iron_nugget', u'shulker_shell', u'cooked_beef', u'diamond_block', u'blaze_rod', u'dark_oak_stairs', u'nether_wart', u'filled_map', u'white_glazed_terracotta', u'boat', u'diamond_boots', u'beetroot', u'beef', u'trapdoor', u'monster_egg', u'orange_glazed_terracotta', u'chalkboard', u'gold_ore', u'brick', u'water_bucket', u'fire', u'baked_potato', u'brown_mushroom_block', u'golden_chestplate', u'blaze_powder', u'dragon_egg', u'gunpowder', u'stained_glass_pane', u'comparator', u'milk_bucket', u'air', u'spruce_stairs', u'elytra', u'totem_of_undying', u'tripwire', u'leather_leggings', u'sapling', u'repeating_command_block', u'wall_sign', u'glowingobsidian', u'bowl', u'lava', u'flint_and_steel', u'splash_potion', u'golden_shovel', u'gold_horse_armor', u'leather_horse_armor', u'rail', u'end_bricks', u'portal', u'stone_button', u'mushroom_stew', u'concrete', u'pumpkin_seeds', u'golden_sword', u'leather_helmet', u'iron_horse_armor', u'jungle_stairs', u'slime', u'spruce_door', u'ender_chest', u'web', u'board', u'brown_mushroom', u'cobblestone_wall', u'writable_book', u'ender_pearl', u'silver_glazed_terracotta', u'clay_ball', u'sandstone_stairs', u'glass_pane', u'grass_block', u'lit_furnace', u'dark_oak_door', u'experience_bottle', u'clay', u'prismarine_crystals', u'diamond_pickaxe', u'redstone_lamp', u'red_mushroom_block', u'yellow_flower', u'sponge', u'yellow_glazed_terracotta', u'potion', u'speckled_melon', u'iron_pickaxe', u'leather_chestplate', u'redstone', u'golden_carrot', u'info_update2', u'lead', u'quartz_stairs', u'chorus_plant', u'ice', u'golden_rail', u'wheat', u'prismarine_shard', u'tipped_arrow', u'packed_ice', u'stone', u'saddle', u'lava_bucket', u'hopper_minecart', u'iron_ingot', u'double_wooden_slab', u'birch_fence_gate', u'diamond_axe', u'acacia_stairs', u'brick_block', u'iron_shovel', u'cauldron', u'cocoa', u'command_block_minecart', u'appleenchanted', u'spruce_fence_gate', u'glowstone_dust', u'log', u'iron_chestplate', u'tnt_minecart', u'iron_door', u'coal_block', u'pumpkin_stem', u'chorus_fruit_popped', u'brown_glazed_terracotta', u'pufferfish', u'repeater', u'tripwire_hook', u'detector_rail', u'bookshelf', u'muttoncooked', u'feather', u'golden_axe', u'porkchop', u'skull', u'lit_redstone_ore', u'bucket', u'cyan_glazed_terracotta', u'cake', u'grass', u'purpur_stairs', u'cooked_salmon', u'coal_ore', u'flower_pot', u'powered_repeater', u'movingblock', u'reserved6', u'unpowered_comparator', u'sealantern', u'chainmail_helmet', u'leather_boots', u'emptymap', u'melon_block', u'book', u'magenta_glazed_terracotta', u'lingering_potion', u'quartz', u'mossy_cobblestone', u'cobblestone', u'oak_stairs', u'redstone_block', u'mob_spanwer', u'crafting_table', u'potato', u'diamond_chestplate', u'wheat_seeds', u'snow_layer', u'nether_brick', u'carrotonastick'					
						)),
			("Damage:",0),
			("Name:",("string","value=Featherblade")),
			("Potion Effect:",("",
					"water",
					"mundane",
					"thick",
					"awkward",
					"night_vision",
					"long_night_vision",
					"invisibility",
					"long_invisibility",
					"leaping",
					"long_leaping",
					"strong_leaping",
					"fire_resistance",
					"long_fire_resistance",
					"swiftness",
					"long_swiftness",
					"strong_swiftness",
					"slowness",
					"long_slowness",
					"water_breathing",
					"long_water_breathing",
					"healing",
					"strong_healing",
					"harming",
					"strong_harming",
					"poison",
					"long_poison",
					"strong_poison",
					"regeneration",
					"long_regeneration",
					"strong_regeneration",
					"strength",
					"long_strength",
					"strong_strength",
					"weakness",
					"long_weakness"
					)),
			("Lore:",("string","value=Legendary,Great War Artifact,+10 points")),
			("Enchantments:",("string","value=sharpness:2,smite:1")),
			("Enchant Hint (not used):",(
					"protection",
					"fire_protection",
					"feather_falling",
					"blast_protection",
					"projectile_protection",
					"respiration",
					"aqua_affinity",
					"thorns",
					"depth_strider",
					"frost_walker",
					"binding_curse",
					"sharpness",
					"smite",
					"bane_of_arthropods",
					"knockback",
					"fire_aspect",
					"looting",
					"sweeping",
					"efficiency",
					"silk_touch",
					"unbreaking",
					"fortune",
					"power",
					"punch",
					"flame",
					"infinity",
					"luck_of_the_sea",
					"lure",
					"mending",
					"vanishing_curse"
					)),
			("Creates an item in your selection.", "label"),
			("Places it in a new chest.", "label"),
			("Use comma seperated lists.", "label"),
			("adrian@theworldfoundry.com", "label"),
			("http://theworldfoundry.com", "label"),
)

def generateItem(id,damage,name,potion,lore,enchants):
	# Creates a new Minecraft item and returns it
	
	# Convenience handler
	idMappings = UNBT.updateAssociations() # Master data for Minecraft
	idItem = idMappings["items"]
	idItems = idItem.keys()
	idEnchant = idMappings["enchantments"]
	idEnchants = idEnchant.keys()
	idPotion = idMappings["potions"]
	idPotions = idPotion.keys()

	NAMESPACEPREFIX = "minecraft:"
	# Structure is (item_id,item_damage,slot,item_count,item_display_name,item_display_lore_l,item_tag_ench_l)
	# Start with the basic item info, then add lore and enchants
	
	# Validation - does the provided item exist?
	foundItem = False
	for itemName in idItems:
		if id.replace(NAMESPACEPREFIX,"") == itemName:
			foundItem = True
			break
	if foundItem == False:
		print "WARN: The specified item name is not known. Try \"golden_sword\"."
		
	theLore_l = lore.split(",")
	enchant_l = enchants.split(",")
	
	# Target mapping
	item_id = NAMESPACEPREFIX+id
	item_display_name = name
	item_count = 1
	item_damage = damage
	item_display_lore_l = theLore_l
	item_tag_ench_l = []
	for enchval in enchant_l:
		part = enchval.split(":")
		item_tag_ench_l.append((int(idEnchant[part[0]]),int(part[1])))
	item_potion = NAMESPACEPREFIX+potion
	
	return (item_id,item_damage,item_count,item_display_name,item_display_lore_l,item_tag_ench_l,item_potion)
	
def perform(level, box, options):
	# UNBT setup
	nativeChestIDList = UNBT.getNativeIDs(UNBT.UCHEST.TYPE)
	nativeChestIDMetaList = UNBT.getNativeIDsAndMetaData(UNBT.UCHEST.TYPE)

	print "UNBT setup complete"
	(item_id,item_damage,item_count,item_display_name,item_display_lore_l,item_tag_ench_l,item_potion) = generateItem(options["Item ID:"],options["Damage:"],options["Name:"],options["Potion Effect:"],options["Lore:"],options["Enchantments:"])
	
	print "NEW ITEM:",item_id,item_damage,item_count,item_display_name,item_display_lore_l,item_tag_ench_l,item_potion
	
	# Create or use provided chest
	x,y,z = box.minx,box.miny,box.minz
	chunk = level.getChunk(x>>4,z>>4) # divide by 16
	newChest = UNBT.UCHEST((x,y,z),"","",[(item_id,item_damage,0,item_count,item_display_name,item_display_lore_l,item_tag_ench_l,item_potion)],"",0)
	
	# Use existing chest, if present
	block = level.blockAt(x,y,z)
	if block in UNBT.UCHEST.BLOCKIDS: # Use this chest

		for e in chunk.TileEntities: # Loop through all the block entities in this chunk
			ex = e["x"].value
			ey = e["y"].value
			ez = e["z"].value
			if ex == x and ey == y and ez == z: # Match... use existing chest
				print "Found ",UNBT.UCHEST.TYPE,": ",str(e)
				foundHandler = False
				for (id,adapter,label,fm,architecture,majorVer,minorVer) in nativeChestIDMetaList:
					print "Working with: ",id,adapter,label,fm,architecture,majorVer,minorVer
					if id == e["id"].value: # Matching definition located. TODO: Handle version precedence when duplicate ids found across versions
						if foundHandler == True:
							print "WARN: ","Duplicate handlers found for ",id
						newChest = UNBT.fromNative(e,UNBT.UCHEST.TYPE,architecture,majorVer+"_"+minorVer)
						
						# Append our item to it if there is room
						if len(newChest.items) < UNBT.UCHEST.SLOTSMAX:
							inv = []
							for i in xrange(0,UNBT.UCHEST.SLOTSMAX):
								inv.append("") # Set up a quick mapping template
						for (chestitem_id,chestitem_damage,chest_slot,chestitem_count,chestitem_display_name,chestitem_display_lore_l,chestitem_tag_ench_l,chestitem_potion) in newChest.items:
							if chestitem_id != "":
								inv[chest_slot] = chestitem_id # Place existing items in the virtual inventory
							else:
								inv[chest_slot] = "USED"

						count = 0
						for i in inv:
							if i == "": # Empty
								newChest.items.append((item_id,item_damage,count,item_count,item_display_name,item_display_lore_l,item_tag_ench_l,item_potion)) # Carefully place the new item
								print "Item placed in slot",i
								break
							count += 1
						else:
							print "WARN: Insufficient space (slots used = ",len(newChest.items),") in the chest at ",x,y,z," to insert the new item."
						
						print "NEW CANONICAL CREATED:",newChest
						foundHandler = True
				if foundHandler == False:
					print "WARN: ","No handler found for ",UNBT.UCHEST.TYPE," at ",(x,y,z)
	
	# Now write the newChest back to the world
	
	architecture = level.gamePlatform.upper() # At the time of writing this is UNKNOWN for Java and PE for Bedrock.
	# Until we've got a way of getting the version out of level, this is static
	version = "1_2" # a default
	for (id,adapter,label,fm,arch,majorVer,minorVer) in nativeChestIDMetaList:
		if architecture == arch:
			version = majorVer+"_"+minorVer # TODO: Choose the latest version? Ask the user? Needs more thought
	# For each object in the box and within CACHEDRESULTS, attempt to write out to the world based on the type of world it is.
	if (x,y,z) in box: # Only make changes within the selection box, otherwise the user won't know what's going on. 
		# Confirm there is a block entity at the target location
		blockID = level.blockAt(x,y,z)
		if blockID in newChest.BLOCKIDS: # This is a candidate for blasting NBT
			# Remove any existing NBT - this can be in a function
			for e in chunk.TileEntities: # Loop through all the block entities in this chunk
				ex = e["x"].value
				ey = e["y"].value
				ez = e["z"].value
				if ex == x and ey == y and ez == z: # Match... purge
					chunk.TileEntities.remove(e) # Goodbye
		else:
			print "Creating a new block"
			level.setBlockAt(x,y,z,UNBT.UCHEST.BLOCKIDS[0]) # Default chest type
			level.setBlockDataAt(x,y,z,randint(2,5)) # Random facing

		# The world has been prepped. Update the NBT!
			
		# Now... make a new 'e'
		# Get the new native nbt...
		e = newChest.toNative(architecture,version)
		chunk.TileEntities.append(e)
	level.markDirtyBox(box)
	
