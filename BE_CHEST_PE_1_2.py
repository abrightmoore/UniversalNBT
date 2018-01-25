# @TheWorldFoundry

from pymclevel import nbt, TAG_Compound, TAG_List, TAG_Int, TAG_Byte_Array, TAG_Short, TAG_Byte, TAG_String, TAG_Double, TAG_Float, TAG_Long

from UNBT import UCHEST,itemNumberToName,itemNameToNumber,updateAssociations

def getNativeID():
	return "Chest"

def toNative(canonical): # Version specific mapping to NBT from universal class
	# Data transformation, and any validation
	associations = updateAssociations()
	position = canonical.position
	customname = canonical.customname
	lock = canonical.lock
	items = canonical.items # list of items, which includes lists of lore and enchants
	loottable = canonical.loottable
	loottableseed = canonical.loottableseed
	id = getNativeID()
	(x,y,z) = canonical.position
	
	# Create native-compatible NBT and return it
	control = TAG_Compound()
	control["id"] = TAG_String(id)
	control["CustomName"] = TAG_String(customname)
	if lock != "": control["Lock"] = TAG_String(lock)
	if loottable != "":
		control["LootTable"] = TAG_String(loottable)
		control["LootTableSeed"] = TAG_Long(loottableseed)
	control["x"] = TAG_Int(x)
	control["y"] = TAG_Int(y)
	control["z"] = TAG_Int(z)
	control["Items"] = TAG_List()
	itemsTag = control["Items"]
	for (item_id,item_damage,item_slot,item_count,item_display_name,item_display_lore_l,item_tag_ench_l) in items:
		item = TAG_Compound()
		item["id"] = TAG_Short(int(itemNameToNumber(item_id,associations)))
		item["Damage"] = TAG_Short(item_damage)
		item["Count"] = TAG_Byte(item_count)
		item["Slot"] = TAG_Byte(item_slot)
		if len(item_tag_ench_l) > 0 or item_display_name != "" or len(item_display_lore_l) > 0:
			item["tag"] = TAG_Compound()
			tag = item["tag"]
			if len(item_tag_ench_l) > 0:
				tag["ench"] = TAG_List()
				ench = tag["ench"]
				for (ench_id,ench_lvl) in item_tag_ench_l:
					theEnch = TAG_Compound()
					theEnch["id"] = TAG_Int(ench_id)
					theEnch["lvl"] = TAG_Int(ench_lvl)
					ench.append(theEnch)
			if len(item_display_name) != "":
				tag["display"] = TAG_Compound()
				display = tag["display"]
				display["Name"] = TAG_String(item_display_name)
			if len(item_display_lore_l) > 0:
				display["Lore"] = TAG_List()
				for lore in item_display_lore_l:
					display["Lore"].append(TAG_String(lore))

		itemsTag.append(item)		
	control["isMovable"] = TAG_Int(1)
	return control

def reterpret(text):
	if text == "":
		return "null"
	else:
		dic = { "text" : text }
		result = json.dumps(dic)
		return result
	
def interpret(text):
	''' Unpickle json, if present.
	'''
	if text == "null":
		return ""
	else:
		print text
		result = json.loads(text)
		return result["text"]
		
def fromNative(nativeNBT): # Version specific mapping from supplied NBT format
	associations = updateAssociations()
	# Data transformation, and any validation
	x = nativeNBT["x"].value
	y = nativeNBT["y"].value
	z = nativeNBT["z"].value
	
	if "CustomName" in nativeNBT: customname = nativeNBT["CustomName"].value
	else: customname = ""
	if "Lock" in nativeNBT: lock = nativeNBT["Lock"].value
	else: lock = ""
	if "Items" in nativeNBT:
		undefinedslot = 0
		items = []
		for item in nativeNBT["Items"]: # JSON?
			print "Parsing Item: ",item
			if "id" in item: item_id = itemNumberToName(item["id"].value,associations)
			else: item_id = ""
			if "Damage" in item: item_damage = item["Damage"].value
			else: item_damage = 0
			if "Slot" in item:
				item_slot = item["Slot"].value
				if item_slot > undefinedslot:
					undefinedslot = item_slot+1 # We don't want to overwrite any existing item slots, so move the cursor for undefined slots past
			else: 
				item_slot = undefinedslot
				undefinedslot += 1
			if "Count" in item: item_count = item["Count"].value
			else: item_count = 1
			item_display_lore_l = []
			item_tag_ench_l = []
			item_display_name = ""
			if "tag" in item:
				item_tag = item["tag"]
				if "display" in item_tag: # compound
					item_display = item_tag["display"]
					if "Name" in item_display: item_display_name = item_display["Name"].value
					if "Lore" in item_display: 
						for lore in item_display["Lore"]:
							item_display_lore_l.append(lore.value)
				if "ench" in item_tag:
					for ench in item_tag["ench"]:
						if "id" in ench: item_tag_ench_id = ench["id"].value
						else: item_tag_ench_id = 0
						if "lvl" in ench: item_tag_ench_lvl = ench["lvl"].value
						else: item_tag_ench_lvl = 0
						item_tag_ench_l.append((item_tag_ench_id,item_tag_ench_lvl))
			items.append((item_id,item_damage,item_slot,item_count,item_display_name,item_display_lore_l,item_tag_ench_l))
	if "LootTable" in nativeNBT: loottable = nativeNBT["LootTable"].value
	else: loottable = ""
	if "LootTableSeed" in nativeNBT: loottableseed = nativeNBT["LootTableSeed"].value
	else: loottableseed = 0
	
	# Create canonical and return it
	return UCHEST((x,y,z),customname,lock,items,loottable,loottableseed)
	