import os #print os

shotFolders 					= ['dev', 'ren', 'plt'] 
#print shotFolders

renFolders 						= ['ver1', 'ver2', 'dev'] 
#print renFolders


# Assign what OS this is to variable
# for OS dectection
osType = os.name

# Conditioanl to Detect what OS we're using
if osType == 'nt':
    root 						= 'C:/projects/shotgun/seq'

    # Notes for what OS we're using
    os_ver 						= "OS Ver: Windows"            

elif osType == 'posix':
    root 						= "/Users/steves/Documents/workspace/shotgun/dev/seq"

    # Notes for what OS we're using
    os_ver 						= "OS Ver: OSX/Linux"      

else:
	print "I don't know what OS this is..."


# Only make dir if it doesn't already exist 
if not os.path.isdir(root):
	os.mkdir(root)


# Change directory
os.chdir(root)


# Start loop to build folder structure
for i in range(2):

	# Count by multiples of 1 + 10
	i 							= (i+1)*10

	# Build padded shot name
	# Nice work in finding this!!!
	shotName 					= "s%03d" % i #print shotName
 
 	# Create string message for raw_input function
	shotInputMsg 				= "Please enter desc for shot# " + str(shotName) + " :"
	#shotInputMsg 				= "Please enter desc for shot# %s :" % (shotName) # Or you could try this way
	
	# Run raw_input asking for user prompt
	shotDesc 					= raw_input(shotInputMsg)	

	# reassing shotname with the users input
	shotName 					= shotName + "_" + shotDesc
	print shotName

	# Assign shot path based on the root folder and shotname
	shotPath 					= root + "/" + shotName
	print shotPath

	# Detect whether or not the shot folder has been created,
	# if not, then create it
	if not os.path.isdir(shotPath):
		os.mkdir(shotPath)

	# Now loop through the folders to be created under each shot 
	# We can also nest more for loops for creating sub folders
	for shotFldr in shotFolders:
		print "	",shotFldr

		# Assign full path of the folders created under the shotname
		shotFolderPath 			= shotPath + "/" + shotFldr

		# Detect whether or not the folder has been created,
		# if not, then create it
		if not os.path.isdir(shotFolderPath):
			os.mkdir(shotFolderPath)

		# Conditional to create the sub folders for 'ren'
		if (shotFldr == 'ren'):
			#print 'create the ren sub folders'

			# Loop through ren folders
			for renFldr in renFolders:
				print "		",renFldr
				
				# build ren path from parent shot path
				renFolderPath 			= shotFolderPath + "/" + renFldr
				
				if not os.path.isdir(renFolderPath):
					os.mkdir(renFolderPath)



'''
# For searching through folders and files
# You can also add, delete, etc files and folders
pathAry 						= []
for (path, dirs, files) in os.walk(root):
	#print path
	print dirs

	pathAry.append(dirs)
	#print dirs
	#print files

print pathAry
'''