# @TheWorldFoundry

import json

from pymclevel import nbt, TAG_Compound, TAG_List, TAG_Int, TAG_Byte_Array, TAG_Short, TAG_Byte, TAG_String, TAG_Double, TAG_Float

from UNBT import USIGN

def getNativeID():
	return "minecraft:sign"

def	toNative(canonical): # Version specific mapping to NBT from universal class
	# Data transformation, and any validation
	Text1 = canonical.lines[0]
	Text2 = canonical.lines[1]
	Text3 = canonical.lines[2]
	Text4 = canonical.lines[3]
	id = getNativeID()
	(x,y,z) = canonical.position
	
	# Create native-compatible NBT and return it
	control = TAG_Compound()
	control["id"] = TAG_String(id)
	control["Text1"] = TAG_String(reterpret(Text1))
	control["Text2"] = TAG_String(reterpret(Text2))
	control["Text3"] = TAG_String(reterpret(Text3))
	control["Text4"] = TAG_String(reterpret(Text4))
	control["x"] = TAG_Int(x)
	control["y"] = TAG_Int(y)
	control["z"] = TAG_Int(z)
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
	# Data transformation, and any validation
	x = nativeNBT["x"].value
	y = nativeNBT["y"].value
	z = nativeNBT["z"].value
	Text1 = interpret(nativeNBT["Text1"].value)
	Text2 = interpret(nativeNBT["Text2"].value)
	Text3 = interpret(nativeNBT["Text3"].value)
	Text4 = interpret(nativeNBT["Text4"].value)
	
	# Create canonical and return it
	return USIGN([Text1,Text2,Text3,Text4],(x,y,z))
	