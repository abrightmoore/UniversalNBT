# @TheWorldFoundry

import json

from pymclevel import nbt, TAG_Compound, TAG_List, TAG_Int, TAG_Byte_Array, TAG_Short, TAG_Byte, TAG_String, TAG_Double, TAG_Float

from UNBT import UCOMMAND

def	toNative(canonical): # Version specific mapping to NBT from universal class
	# Data transformation, and any validation
	position = canonical.position
	customname = canonical.customname
	# Not used in Bedrock
	# commandstats = canonical.commandstats # Dictionary {}. This is a runtime artifact. Should it be translated? TODO: Find out.
	command = canonical.command
	successcount = canonical.successcount
	lastoutput = canonical.lastoutput
	trackoutput = canonical.trackoutput
	powered = canonical.powered
	auto = canonical.auto
	conditionmet = canonical.conditionmet
	# Not used in Bedrock
	# updatelastexecution = canonical.updatelastexecution 
	# lastexecution = self.lastexecution
	id = "CommandBlock"
	(x,y,z) = canonical.position
	
	# Create native-compatible NBT and return it
	control = TAG_Compound()
	control["id"] = TAG_String(id)
	control["Command"] = TAG_String(command)
	control["CustomName"] = TAG_String(customname)

	control["LPCommandMode"] = TAG_Int(lpcommandmode) # <---- not in model
	control["LPCondionalMode"] = TAG_Int(lpconditionalmode) # <---- not in model
	control["LPRedstoneMode"] = TAG_Int(lpredstonemode) # <---- not in model

	control["LastOutput"] = TAG_String(lastoutput)

	lastoutputparamsctl = TAG_List()
	control["LastOutputParams"] = lastoutputparamsctl # <---- not in model
	# TODO: parse the params and append to the list
	
	control["SuccessCount"] = TAG_Int(successcount)		
	control["TrackOutput"] = TAG_Byte(trackoutput)

	control["Version"] = TAG_Int(version) # <---- not in model
	
	control["auto"] = TAG_Byte(auto)
	control["conditionMet"] = TAG_Byte(conditionmet)
	control["isMovable"] = TAG_Byte(1) #TODO: Should this be editable?

	
	control["powered"] = TAG_Byte(powered)
	
	# Not used in bedrock
#	control["LastExecution"] = TAG_Long(lastexecution)
#	control["UpdateLastExecution"] = TAG_Byte(updatelastexecution)

	control["x"] = TAG_Int(x)
	control["y"] = TAG_Int(y)
	control["z"] = TAG_Int(z)
	return control
	
def fromNative(nativeNBT): # Version specific mapping from supplied NBT format

	# Data transformation, and any validation
	position = (nativeNBT["x"].value,nativeNBT["y"].value,nativeNBT["z"].value)
	customname = nativeNBT["CustomName"].value
	commandstats = {} # TODO: Find out if this is persisted.
	command = nativeNBT["Command"].value
	successcount = nativeNBT["SuccessCount"].value
	lastoutput = nativeNBT["LastOutput"].value
	trackoutput = nativeNBT["TrackOutput"].value
	powered = nativeNBT["powered"].value
	auto = nativeNBT["auto"].value
	conditionmet = nativeNBT["conditionMet"].value
	updatelastexecution = 0 # TODO: Get a source for this
	lastexecution = 0 # TODO: Get a source for this
	
	# Create canonical and return it
	return UCOMMAND(position, customname, commandstats, command, successcount, lastoutput, trackoutput, powered, auto, conditionmet, updatelastexecution, lastexecution) # Type specific

	