import UNBT
 
inputs = (
	  ("Universal NBT", "label"),
	  ("Mode", ("READ","WRITE")),
	  ("adrian@theworldfoundry.com", "label"),
	  ("http://theworldfoundry.com", "label"),
)

def perform(level,box,options): # MCEdit Unified
	global CACHEDRESULTS
	
	# Some global tables - TODO: Optimise this based on likely use cases
	nativeSignIDList = UNBT.getNativeIDs(UNBT.USIGN.TYPE)
	nativeSignIDMetaList = UNBT.getNativeIDsAndMetaData(UNBT.USIGN.TYPE)
	nativeCommandIDList = UNBT.getNativeIDs(UNBT.UCOMMAND.TYPE)
	nativeCommandIDMetaList = UNBT.getNativeIDsAndMetaData(UNBT.UCOMMAND.TYPE)
	print "Level type = ",str(level.gamePlatform)
	print "Level version = ", str(level.gameVersion)
	print "Level name = ", str(level.displayName)
	print "Process mode ", options["Mode"]
	
	if options["Mode"] == "READ":
		CACHEDRESULTS = None

		# For each chunk in the selection, gather the NBT 
		for (chunk, _, _) in level.getChunkSlices(box):
			for e in chunk.TileEntities: # Loop through all the block entities in this chunk
				x = e["x"].value
				y = e["y"].value
				z = e["z"].value
				if (x,y,z) in box: # Only process the entities within the selection, ignore malformed entries
					# At this point we need to identify what type of entity this is based on how it identifies itself
					# TODO: Extend UNBT to provide an enumeration of all the possible block entity identifiers
					#       For this immediate example, we'll hard code the versions we're expecting.
					#		Also need to collapse these checks - they're doing basically the same thing so should be rolled together.
					if e["id"].value in nativeSignIDList: # This is a sign because it has an NBT id which matches one of the known values
						# Find out what architecture this NBT object corresponds to
						print "Found ",UNBT.USIGN.TYPE,": ",str(e)
						
						# Work out which architecture and version this definition is from.
						# TODO: Make this a lookup via dictionary
						foundHandler = False
						for (id,adapter,label,fm,architecture,majorVer,minorVer) in nativeSignIDMetaList:
							print "Working with: ",id,adapter,label,fm,architecture,majorVer,minorVer
							if id == e["id"].value: # Matching definition located. TODO: Handle version precedence when duplicate ids found across versions
								if foundHandler == True:
									print "WARN: ","Duplicate handlers found for ",id
								newObj = UNBT.fromNative(e,UNBT.USIGN.TYPE,architecture,majorVer+"_"+minorVer)
								print "NEW CANONICAL CREATED:",newObj
								foundHandler = True
						if foundHandler == False:
							print "WARN: ","No handler found for ",UNBT.USIGN.TYPE," at ",(x,y,z)
						
					if e["id"].value in nativeCommandIDList: # This is a sign because it has an NBT id which matches one of the known values
						# Find out what architecture this NBT object corresponds to
						print "Found ",UNBT.UCOMMAND.TYPE,": ",str(e)

						# Work out which architecture and version this definition is from.
						# TODO: Make this a lookup via dictionary
						foundHandler = False
						for (id,adapter,label,fm,architecture,majorVer,minorVer) in nativeCommandIDMetaList:
							print "Working with: ",id,adapter,label,fm,architecture,majorVer,minorVer
							if id == e["id"].value: # Matching definition located. TODO: Handle version precedence when duplicate ids found across versions
								if foundHandler == True:
									print "WARN: ","Duplicate handlers found for ",id
								newObj = UNBT.fromNative(e,UNBT.UCOMMAND.TYPE,architecture,majorVer+"_"+minorVer)
								print "NEW CANONICAL CREATED:",newObj
								foundHandler = True
						if foundHandler == False:
							print "WARN: ","No handler found for ",UNBT.UCOMMAND.TYPE," at ",(x,y,z)

						
	elif options["Mode"] == "WRITE":
		print "Not implemented"
	else:
		print "Unknown option selected."
	
