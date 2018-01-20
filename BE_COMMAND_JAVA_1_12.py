# @TheWorldFoundry

import json

from pymclevel import nbt, TAG_Compound, TAG_List, TAG_Int, TAG_Byte_Array, TAG_Short, TAG_Byte, TAG_String, TAG_Double, TAG_Float

from UNBT import UCOMMAND

def	toNative(canonical): # Version specific mapping to NBT from universal class
	# Data transformation, and any validation
	position = canonical.position
	customname = canonical.customname
	commandstats = canonical.commandstats # Dictionary {}
	command = canonical.command
	successcount = canonical.successcount
	lastoutput = canonical.lastoutput
	trackoutput = canonical.trackoutput
	powered = canonical.powered
	auto = canonical.auto
	conditionmet = canonical.conditionmet
	updatelastexecution = canonical.updatelastexecution 
	lastexecution = self.lastexecution
	id = "minecraft:"
	(x,y,z) = canonical.position
	
	# Create native-compatible NBT and return it
	control = TAG_Compound()
	control["id"] = TAG_String(id)
	control["Text1"] = TAG_String(Text1)
	control["Text2"] = TAG_String(Text2)
	control["Text3"] = TAG_String(Text3)
	control["Text4"] = TAG_String(Text4)	
	control["x"] = TAG_Int(x)
	control["y"] = TAG_Int(y)
	control["z"] = TAG_Int(z)
	return control
	
def fromNative(nativeNBT): # Version specific mapping from supplied NBT format
	# Data transformation, and any validation
	x = nativeNBT["x"].value
	y = nativeNBT["y"].value
	z = nativeNBT["z"].value
	Text1 = nativeNBT["Text1"].value
	Text2 = nativeNBT["Text2"].value
	Text3 = nativeNBT["Text3"].value
	Text4 = nativeNBT["Text4"].value
	
	# Create canonical and return it
	return USIGN([Text1,Text2,Text3,Text4],(x,y,z))
	