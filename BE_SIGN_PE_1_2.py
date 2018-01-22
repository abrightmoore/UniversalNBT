# @TheWorldFoundry

from pymclevel import nbt, TAG_Compound, TAG_List, TAG_Int, TAG_Byte_Array, TAG_Short, TAG_Byte, TAG_String, TAG_Double, TAG_Float

from UNBT import USIGN

def getNativeID():
	return "Sign"

def toNative(canonical): # Version specific mapping to NBT from universal class
	# Data transformation, and any validation
	Text1 = canonical.lines[0].replace("\n","")
	Text2 = canonical.lines[1].replace("\n","")
	Text3 = canonical.lines[2].replace("\n","")
	Text4 = canonical.lines[3].replace("\n","")
	id = getNativeID()
	(x,y,z) = canonical.position
	
	# Create native-compatible NBT and return it
	control = TAG_Compound()
	control["id"] = TAG_String(id)
	control["Text"] = TAG_String(Text1+"\n"+Text2+"\n"+Text3+"\n"+Text4) # TODO: Need to prevent appending more newlines than needed
	control["isMovable"] = TAG_Int(1)
	control["x"] = TAG_Int(x)
	control["y"] = TAG_Int(y)
	control["z"] = TAG_Int(z)
	return control
	
def fromNative(nativeNBT): # Version specific mapping from supplied NBT format
	# Data transformation, and any validation
	x = nativeNBT["x"].value
	y = nativeNBT["y"].value
	z = nativeNBT["z"].value
	isMovable = nativeNBT["isMovable"].value
	Text = nativeNBT["Text"].value

	# Map values back into canonical format
	Texts = Text.split("\n")	
	Text1 = ""
	Text2 = ""
	Text3 = ""
	Text4 = ""

	if len(Texts) > 0:
		Text1 = Texts[0]
	if len(Texts) > 1:
		Text2 = Texts[1]
	if len(Texts) > 2:
		Text3 = Texts[2]
	if len(Texts) > 3:
		Text4 = Texts[3]
	if len(Texts) > 4:
		print "WARN: More than 4 lines on a sign at "+str(x)+","+str(y)+","+str(z)+". Discarding excess: "
		for i in xrange(3,len(Texts)):
			print i,": ",Texts[i]

	# Create canonical and return it
	return USIGN([Text1,Text2,Text3,Text4],(x,y,z))
	