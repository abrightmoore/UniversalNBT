# coding=UTF-8
import UNBT
from random import randint
import textwrap

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')


inputs = (
	  ("CHEST-A-PLENTY", "label"),
	  ("Select a chest block.", "label"),
	  ("Run the filter.", "label"),
	  ("Randomly generates items.", "label"),
	  ("Places them in the selected chest.", "label"),
	  ("adrian@theworldfoundry.com", "label"),
	  ("http://theworldfoundry.com", "label"),
)

def wrapText(text,length):
	return textwrap.fill(text,length)

def makeLore(ADJECTIVES,lineWrap):
	INDIC = ["signs","hints","feelings","stenches","fingerprints","markings","glyphs","smells","bumps","cracks","shapes","knobs","buttons","stripes","chequers","tassels","wires","colours"]
	NOUNS = ["magic","evil","dread","shame","honey","righteousnous","fear","happiness","sadness","sweat","vegemite","hope","silver","the ocean","lichen","moss","dirt","zombie flesh"]
	QTY = ["all over","covering","dotted around","placed randomly on","sitting low on","climbing all the way up","underneath","on top of","encircling","obscuring","powering","charging"]
	
	result = "There are "+ADJECTIVES[randint(0,len(ADJECTIVES)-1)]+" "+INDIC[randint(0,len(INDIC)-1)]
	if randint(1,10) > 6:
		result = result+" of "+NOUNS[randint(0,len(NOUNS)-1)]
	result = result+" "+QTY[randint(0,len(QTY)-1)]+" this item."
	
	return wrapText(result,lineWrap)
	

def generateItems(ADJECTIVES,qty):
	# Randomly creates new Minecraft items
	formatting = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","m","n","l","k","o"]
	PRO = ["","One ","A ","The ","That ","This "]
	NOUNS = ["AB","Jigarbov","Ron","Dragnoz","The Wandering Wizards","Le Moesh","The World Foundry","The Pathway","Mojang","The Map Maker","The Dragon","The Overworld","The Nether","The End","The Villagers"]
	idMappings = UNBT.updateAssociations() # Master data for Minecraft
	idItems = idMappings["items"]
	idEnchant = idMappings["enchantments"]
	idEnchants = idEnchant.keys()
	# print idEnchant
	
	items = []
	# Structure is (item_id,item_damage,slot,item_count,item_display_name,item_display_lore_l,item_tag_ench_l)
	# Start with the basic item info, then add lore and enchants
	keys = idItems.keys()
	# print keys
	slot = 0
	for i in xrange(0,qty):
		item_id = "minecraft:"+keys[randint(0,len(keys)-1)] # Number or text?
		# print "Item ID",item_id
		item_display_lore_l = []		
		item_tag_ench_l = []
		item_display_name = "§"+formatting[randint(0,14)]+str(item_id.replace("minecraft:","").replace("_"," ").title())
		if randint(1,10) > 8:
			item_display_name = item_display_name+" of "+NOUNS[randint(0,len(NOUNS)-1)]
			loreLines = makeLore(ADJECTIVES,len(item_display_name)).split("\n")
			for lore in loreLines:
				item_display_lore_l.append(lore)
			if randint(1,10) > 3:
				for i in xrange(0,randint(1,3)):
					ench = idEnchants[randint(0,len(idEnchants)-1)]
					lvl = randint(1,5)
				item_tag_ench_l.append((int(idEnchant[ench]),lvl))
		# item_display_name = "\"Custom "+formatting[randint(0,15)]+str(item_id.replace("minecraft:","").replace("_"," ").title())+"\""
		# print "Custom Name ",item_display_name
		item_damage = 0 # Allow randoms?
		item_count = 1
		items.append((item_id,item_damage,slot,item_count,item_display_name,item_display_lore_l,item_tag_ench_l))
		slot += 1
	
	return items
	


def perform(level,box,options): # MCEdit Unified
	
	# Read the adjectives list
	ADJECTIVES = loadLinesFromFile("adjectives.txt")
	CONTAINERS = ["Chest","Locker","Box","Suitcase"]
	
	# Generate items and place in the selected chest block
	lock = ""
	loottable = ""
	loottableseed = 0
	
	
	arch = level.gamePlatform.upper()
	ver = "1_12" # Static until we can get the version from MCEdit
	if arch == "PE":
		ver = "1_2" # Static until we can get the version from MCEdit
	
	nativeChestIDList = UNBT.getNativeIDs(UNBT.UCHEST.TYPE)
	nativeChestIDMetaList = UNBT.getNativeIDsAndMetaData(UNBT.UCHEST.TYPE)
	# For each chunk in the selection, gather the NBT 
	for (chunk, _, _) in level.getChunkSlices(box):
		for e in chunk.TileEntities: # Loop through all the block entities in this chunk
			x = e["x"].value
			y = e["y"].value
			z = e["z"].value
			if (x,y,z) in box: # Only process the entities within the selection, ignore malformed entries
				if e["id"].value in nativeChestIDList: # This is a sign because it has an NBT id which matches one of the known values
					# Find out what architecture this NBT object corresponds to
					print "Found ",UNBT.UCHEST.TYPE,": ",str(e)
					blockID = level.blockAt(x,y,z)
					if blockID in UNBT.UCHEST.BLOCKIDS: # This is a candidate for blasting NBT

						foundHandler = False
						for (id,adapter,label,fm,architecture,majorVer,minorVer) in nativeChestIDMetaList:
							if arch == architecture and ver == majorVer+"_"+minorVer:
								print "Working with: ",id,adapter,label,fm,architecture,majorVer,minorVer
								if id == e["id"].value: # Matching definition located. TODO: Handle version precedence when duplicate ids found across versions
									if foundHandler == True:
										print "WARN: ","Duplicate handlers found for ",id
									chestObj = UNBT.fromNative(e,UNBT.UCHEST.TYPE,architecture,majorVer+"_"+minorVer) # Extract the existing chest from the world for editing.
									print "NEW CANONICAL CREATED:",chestObj
									# DEP: newChest = UNBT.UCHEST((x,y,z),customname,lock,items,loottable,loottableseed)
									qty = UNBT.UCHEST.SLOTSMAX - len(chestObj.items)
									if qty > 0: # Only make changes if there are empty slots in the inventory
										newItems = generateItems(ADJECTIVES,randint(1,qty)) # Get a grab-bag of items
										# Now, try to place the items in the chest. Give up if it's all too hard
										# Strategy - make a new item list up to the container capacity (use an empty placeholder) and randomise the item order, then place into the chest slots.
										for item in chestObj.items: # (item_id,item_damage,item_slot,item_count,item_display_name,item_display_lore_l,item_tag_ench_l)
											newItems.append(item)
										for i in xrange(len(newItems),UNBT.UCHEST.SLOTSMAX):
											newItems.append(("PLACEHOLDER",0,0,0,"PLACEHOLDER",[],[])) # Junk entry to take up a slot in the chest
										
										# Reorder the item list
										reorderedItems = []
										for i in xrange(0,len(newItems)):
											reorderedItems.append(newItems.pop(randint(0,len(newItems)-1))) # Shrink the newItems, grow the reorderedItems
																	
										newItems = []
										slot = 0
										for (item_id,item_damage,item_slot,item_count,item_display_name,item_display_lore_l,item_tag_ench_l) in reorderedItems:
											if item_id != "PLACEHOLDER":
												newItems.append((item_id,item_damage,slot,item_count,item_display_name,item_display_lore_l,item_tag_ench_l)) # Put into the corresponding slot
											slot += 1
										# Adjust the chest to suit... pop generated items into slots
										chestObj.items = newItems # Replace what's on the object, discarding the original

										
										# Rename the chest
										PRO = ["","One ","A ","The ","That ","This "]
										customname = ADJECTIVES[randint(0,len(ADJECTIVES)-1)] # Pick a describing word
										customname = customname + " " + CONTAINERS[randint(0,len(CONTAINERS)-1)] # Pick a describing word
										chestObj.customname = PRO[randint(0,len(PRO)-1)]+customname.title() # Relabel
										
										# Remove any existing NBT - this can be in a function
										chunk.TileEntities.remove(e) # Goodbye old e
										version = majorVer+"_"+minorVer
										e = chestObj.toNative(architecture,version) # Get the new native nbt...
										chunk.TileEntities.append(e) # Now... make a new 'e'

								foundHandler = True
					if foundHandler == False:
						print "WARN: ","No handler found for ",UNBT.UCHEST.TYPE," at ",(x,y,z)					
	level.markDirtyBox(box)	
	
def loadLinesFromFile(filename):
	fileOfLines = open(filename, 'r+')
	keys = fileOfLines.read().split("\n")
	fileOfLines.close()
	return keys