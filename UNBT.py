# @TheWorldFoundry
# Minecraft's architecture is highly fragmented creating discrepencies 
#  that impact a map maker's ability to work quickly and without error.
# This project seeks to unify the NBT structures in use across the Java 
#  and Bedrock architectures, account for version differences, and simplify
#  the effort of working with tile entities.
# To achieve this, the map maker works with a 'Universal Tile Entity' which 
#  makes just-in-time dynamic calls to version-specific handlers which
#  take care of the property translation into actionable NBT.
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

def fromNative(tileEntity, nativeNBT,form,architecture,version):
	''' Choose a handler from the file system, invoke it, and get an the corresponding object back in return
	'''
	theModule = BLOCKENTITYHANDLERPREFIX+form+"_"+architecture+"_"+version+".py"
	m = getModule(theModule)
	result = m.fromNative(nativeNBT)
	return result
	
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
		
	def toCanonical(self, nativeNBT, architecture, version): # Stick this in a superclass
		return fromNative(self, nativeNBT, self.TYPE,architecture,version)
	
class USIGN:
	TYPE = "SIGN"
	
	def __init__(self, lines, position): # Type specific
		self.lines = lines
		self.position = position
		
	def toNative(self, architecture, version): # Stick this in a superclass
		return toNative(self,self.TYPE,architecture,version)
		
	def toCanonical(self, nativeNBT, architecture, version): # Stick this in a superclass
		return fromNative(self, nativeNBT, self.TYPE,architecture,version)
		
	def __str__(self):
		result = self.TYPE+" at "+str(self.position[0])+","+str(self.position[1])+","+str(self.position[2])+": "+str(self.lines)
		return result

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
