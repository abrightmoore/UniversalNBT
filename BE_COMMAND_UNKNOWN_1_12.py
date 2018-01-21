# @TheWorldFoundry

import json

from pymclevel import nbt, TAG_Compound, TAG_List, TAG_Int, TAG_Long, TAG_Byte_Array, TAG_Short, TAG_Byte, TAG_String, TAG_Double, TAG_Float

from UNBT import UCOMMAND

def getNativeID():
	return "minecraft:command_block"

def	toNative(canonical): # Version specific mapping to NBT from universal class
	# Data transformation, and any validation
	position = canonical.position
	customname = canonical.customname
	commandstats = canonical.commandstats # Dictionary {}. This is a runtime artifact. Should it be translated? TODO: Find out.
	command = canonical.command
	successcount = canonical.successcount
	lastoutput = canonical.lastoutput
	trackoutput = canonical.trackoutput
	powered = canonical.powered
	auto = canonical.auto
	conditionmet = canonical.conditionmet
	updatelastexecution = canonical.updatelastexecution 
	lastexecution = canonical.lastexecution
	id = getNativeID()
	(x,y,z) = canonical.position
	
	# Create native-compatible NBT and return it
	control = TAG_Compound()
	control["id"] = TAG_String(id)
	control["auto"] = TAG_Byte(auto)
	control["powered"] = TAG_Byte(powered)
	control["LastExecution"] = TAG_Long(lastexecution)
	control["SuccessCount"] = TAG_Int(successcount)	
	control["UpdateLastExecution"] = TAG_Byte(updatelastexecution)
	control["conditionMet"] = TAG_Byte(conditionmet)
	control["CustomName"] = TAG_String(customname)
	control["Command"] = TAG_String(command)
	control["LastOutput"] = TAG_String(lastoutput)
	control["TrackOutput"] = TAG_Byte(trackoutput)
	control["x"] = TAG_Int(x)
	control["y"] = TAG_Int(y)
	control["z"] = TAG_Int(z)
	return control
	
def fromNative(nativeNBT): # Version specific mapping from supplied NBT format
	# Data transformation, and any validation
	position = (nativeNBT["x"].value,nativeNBT["y"].value,nativeNBT["z"].value)
	if "CustomName" in nativeNBT: customname = nativeNBT["CustomName"].value
	else: customname = ""
	commandstats = {} # TODO: Find out if this is persisted.
	if "Command" in nativeNBT: command = nativeNBT["Command"].value
	else: command = ""
	if "SuccessCount" in nativeNBT: successcount = nativeNBT["SuccessCount"].value
	else: successcount = 0
	if "LastOutput" in nativeNBT:	lastoutput = nativeNBT["LastOutput"].value
	else: lastoutput = ""
	if "TrackOutput" in nativeNBT: trackoutput = nativeNBT["TrackOutput"].value
	else: trackoutput = 0
	if "powered" in nativeNBT: powered = nativeNBT["powered"].value
	else: powered = 0
	if "auto" in nativeNBT: auto = nativeNBT["auto"].value
	else: auto = 0
	if "conditionMet" in nativeNBT: conditionmet = nativeNBT["conditionMet"].value
	else: conditionmet = 0
	if "UpdateLastExecution" in nativeNBT: updatelastexecution = nativeNBT["UpdateLastExecution"].value
	else: updatelastexecution = 0
	if "LastExecution" in nativeNBT: lastexecution = nativeNBT["LastExecution"].value
	else: lastexecution = 0
	
	# Create canonical and return it
	return UCOMMAND(position, customname, commandstats, command, successcount, lastoutput, trackoutput, powered, auto, conditionmet, updatelastexecution, lastexecution) # Type specific

	