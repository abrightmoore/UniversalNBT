# @TheWorldFoundry
# Minecraft's architecture is highly fragmented creating discrepencies 
#  that impact a map maker's ability to work quickly and without error.
# This project seeks to unify the NBT structures in use across the Java 
#  and Bedrock architectures, account for version differences, and simplify
#  the effort of working with tile entities.
# To achieve this, the map maker works with a 'Universal Entity' which 
#  makes just-in-time dynamic calls to version-specific handlers which
#  take care of the property translation into actionable NBT. The rationale
#  for this is that if we have to write a bespoke mapping routine for all
#  the various Minecraft versions, let's do it in one place using a modular
#  and extensible approach.
#
# As an example, a sign in Bedrock is:
#   id: TAG_String = "Sign"
#   Text: TAG_String = "One long line of utf text which gets split by newlines ingame onto 4 lines"
#   isMovable: TAG_Byte = 1
#	x: TAG_Int = 748
#	y: TAG_Int = 86
#	z: TAG_Int = 356
#
# In Java 1.12 this is:
#   id: TAG_String = "minecraft:sign"
#   Text1: TAG_String = "Line 1"
#   Text2: TAG_String = "Line 2"
#   Text3: TAG_String = "Line 3"
#   Text4: TAG_String = "Line 4"
#	x: TAG_Int = 748
#	y: TAG_Int = 86
#	z: TAG_Int = 356
#   
# To manage this, a handler for each version specific sign type is created
#  and a generic 'canonical' universal class used to represent the generic sign type.
# Use cases:
# 1. The map maker instantiates the class, and extracts version-specific versions as
#     needed.
# 2. The map maker starts with a version-specific tile entity and generates the canonical


# Requires: PYMCLEVEL, PyYAML


import glob
import sys
import time
import json

from pymclevel import nbt, TAG_Compound, TAG_List, TAG_Int, TAG_Byte_Array, TAG_Short, TAG_Byte, TAG_String, TAG_Double, TAG_Float

BLOCKENTITYHANDLERPREFIX = "BE_"

def getModule(theModule):
	#imageGenerators = glob.glob(moduleName)
	#theModule = imageGenerators[0]
	#	print sys.path
	return __import__(theModule[:-3])
	
# Dynamic invoke instead of class inheritence for convenience of runtime replace/expansion/modularisation.
# Just drop a file in place
def toNative(tileEntity,form,architecture,version):
	''' Choose a handler from the file system, invoke it, and get an the corresponding object back in return
	'''
	theModule = BLOCKENTITYHANDLERPREFIX+form+"_"+architecture+"_"+version+".py"
	m = getModule(theModule)
	result = m.toNative(tileEntity)
	return result

def fromNative(nativeNBT,form,architecture,version):
	''' Choose a handler from the file system, invoke it, and get an the corresponding object back in return
	'''
	theModule = BLOCKENTITYHANDLERPREFIX+form+"_"+architecture+"_"+version+".py"
	m = getModule(theModule)
	result = m.fromNative(nativeNBT)
	return result

def getNativeIDsAndMetaData(form):
	''' Returns a list of the identifiers with known adapters/handlers
	'''
	pattern = BLOCKENTITYHANDLERPREFIX+form+"_*.py"
	adapters = glob.glob(pattern) # Get the list of available handlers / adapters for various entity types
	print 'Found %s block entity adapters:' % (len(adapters))
	ids = []
	for adapter in adapters:
		meta = adapter.split("_")
		m = getModule(adapter)
		ids.append((m.getNativeID(),adapter,meta[0],meta[1],meta[2],meta[3],meta[4][:-3]))
	return ids

def getNativeIDs(form):
	''' Returns a list of the identifiers with known adapters/handlers
	'''
	idMap = getNativeIDsAndMetaData(form)
	ids = []
	for (id,adapter,label,fm,arch,majorVer,minorVer) in idMap:
		ids.append(id)
	return ids

	
# Types
class UCOMMAND:
	TYPE = "COMMAND"
	
	def __init__(self, position, customname, commandstats, command, successcount, lastoutput, trackoutput, powered, auto, conditionmet, updatelastexecution, lastexecution): # Type specific
		self.position = position
		self.customname = customname
		self.commandstats = commandstats # Dictionary {}
		self.command = command
		self.successcount = successcount
		self.lastoutput = lastoutput
		self.trackoutput = trackoutput
		self.powered = powered
		self.auto = auto
		self.conditionmet = conditionmet
		self.updatelastexecution = updatelastexecution
		self.lastexecution = lastexecution
		
	def toNative(self, architecture, version): # Stick this in a superclass
		return toNative(self,self.TYPE,architecture,version)
		
	def __str__(self):
		# print json.dumps(self.commandstats)
		result = self.TYPE+" at "+str(self.position[0])+","+str(self.position[1])+","+str(self.position[2])+": "
		result = result+"\ncustomname = "+self.customname
		result = result+"\ncommandstats = "+json.dumps(self.commandstats)
		result = result+"\ncommand = "+self.command
		result = result+"\nsuccesscount = "+str(self.successcount)
		result = result+"\nlastoutput = "+json.dumps(self.lastoutput) # TODO: Dictionary
		result = result+"\ntrackoutput = "+str(self.trackoutput)
		result = result+"\npowered = "+str(self.powered)
		result = result+"\nauto = "+str(self.auto)
		result = result+"\nconditionmet = "+str(self.conditionmet)
		result = result+"\nupdatelastexecution = "+str(self.updatelastexecution)
		result = result+"\nlastexecution = "+str(self.lastexecution)
		
		return result
		
class USIGN:
	TYPE = "SIGN"
	
	def __init__(self, lines, position): # Type specific
		self.lines = lines
		self.position = position
		
	def toNative(self, architecture, version): # Stick this in a superclass
		return toNative(self,self.TYPE,architecture,version)
		
	def __str__(self):
		# TODO: Formatting for visibility/debugging
		result = self.TYPE+" at "+str(self.position[0])+","+str(self.position[1])+","+str(self.position[2])+": "+str(self.lines)
		return result

##########################
###		UNIT TESTS     ###
##########################
		
def testSign():
	usign = USIGN(["Line 1", "Line 2", "Line 3", "Line 4"],(1,2,3)) # Canonical
	javasign = usign.toNative("JAVA","1_12")
	bedrocksign = usign.toNative("BEDROCK","1_2")
	
	# Java format example
	control = TAG_Compound()
	control["id"] = TAG_String("minecraft:sign")
	control["Text1"] = TAG_String("Text1")
	control["Text2"] = TAG_String("Text2")
	control["Text3"] = TAG_String("Text3")
	control["Text4"] = TAG_String("Text4")	
	control["x"] = TAG_Int(111)
	control["y"] = TAG_Int(2222)
	control["z"] = TAG_Int(33333)
	usignFromJava = usign.toCanonical(control,"JAVA","1_12")
	usignFromJava2 = usign.toCanonical(javasign,"JAVA","1_12")
	
	# Bedrock format example
	control = TAG_Compound()
	control["id"] = TAG_String("Sign")
	control["Text"] = TAG_String("Text1\nText2\nText3\nText4")
	control["isMovable"] = TAG_Int(1)
	control["x"] = TAG_Int(111111)
	control["y"] = TAG_Int(22222)
	control["z"] = TAG_Int(3333)	
	usignFromBedrock = usign.toCanonical(control,"BEDROCK","1_2")

#	bedrocksign = usign.toCanonical("BEDROCK","1_2")
	
	print usign,"\n",javasign,"\n",bedrocksign,"\n",usignFromJava,"\n",usignFromJava2,"\n",usignFromBedrock

def testCommand():
	ucommand = UCOMMAND((7654,9347,123), "customname", "commandstats", "command", 1, "lastoutput", 1, 0, 1, 1, 234, 456) # Type specific
	javacommand = ucommand.toNative("JAVA","1_12")
	
	print ucommand,"\n",javacommand