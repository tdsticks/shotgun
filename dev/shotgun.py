import os, sys
from shotgun_api3 import Shotgun

# ----------------------------------------------
# USES API SCRIPT AND ESTABLISHED SG WITH PYTHON
# ---------------------------------------------- 
SERVER_PATH 				= 'ShotgunUrl'
SCRIPT_USER 				= 'ScriptName '
SCRIPT_KEY 					= 'ApiKey'
sg 							= Shotgun(SERVER_PATH, SCRIPT_USER, SCRIPT_KEY)
#print sg



# Define function to make directories
# with some error checking
def makeDir(folderName):
	if not os.path.isdir(folderName):
		os.mkdir(folderName) 
		print "Folder:", folderName, "Created"
		print


# Assign what OS this is to variable
# for OS dectection
osType = os.name

# Conditioanl to Detect what OS we're using
if osType == 'nt':
    root 						= 'C:/projects/shotgun/jobs'

    # Notes for what OS we're using
    os_ver 						= "OS Ver: Windows"            

elif osType == 'posix':
    root 						= "/Users/steves/Documents/workspace/shotgun/dev/jobs"

    # Notes for what OS we're using
    os_ver 						= "OS Ver: OSX/Linux"      

else:
	print "I don't know what OS this is..."


# Make the jobs directory
makeDir(root)


# Change directory
os.chdir(root)


# Start Shotgun calls
fields 						= ['id', 'code', 'name', 'sg_status']
filters						= [
								['sg_status', 'is', 'Active'],
								['id', 'is_not', 4]
							]
projects 					= sg.find("Project",filters,fields)
print projects
print


for p in projects:
	print p

	projectName 			= p['name']

	makeDir(projectName)


	filters 				= [
								['project', 'is', {'type':'Project', 'id':p['id']}]
	]
	fields					= ['code','shots']
	Sequences 				= sg.find('Sequence', filters, fields) 
	#print Sequences
	#print

	for seq in Sequences:
		print seq
		print

		sequenceName  		= seq['code']
		sequencePath  		= projectName + "/" + sequenceName

		makeDir(sequencePath)

		shots 				= seq['shots']
		print shots
		print

		for shot in shots:
			print shot

			shotName 		= shot['name']
			shotPath		= sequencePath + "/" + shotName

			makeDir(shotPath)




#project 					= sg.find_one("Project", [["name", "is", "Demo Project"]] )
#print project

#shot = sg.create("Shot", {"code":"sh001","project":project} )
#print shot

#sg.update("Shot",shot["id"],{"sg_status_list":"ip"})
#sg.delete("Shot",shot["id"])