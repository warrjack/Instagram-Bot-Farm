import json
import emoji
import random as rand
import time
from firebase import firebase

# Configure
#############################
firebaseRef = ''
password = ''	
collectionD = [] # Dates
collectionG = [] # Grad Dates
collectionU = [] # School (U=6, H=3)
#############################

# Setting Firebase URL
firebase = firebase.FirebaseApplication(firebaseRef, None)

# Arrays to save bio information
collectionM = [] #Male First Names
collectionF = [] #Female First Names
collectionL = [] #Last Names
#collectionU = [] #Usernames
collectionB = [] #Bios

# Save current bio being used
bio = ""
schoolBio = ""
snapBio = ""
locatBio = ""
hobbyBio = ""
randomDate = rand.randint(0, (len(collectionD)-1))

lastNameCount = 0

def createBio():
	#Bio
	randomBio = rand.randint(0, 21)
	randHobby = rand.randint(0,2)

	global snapBio
	global schoolBio
	global hobbyBio
	global locatBio
	global randomDate
	
	
	#Snap
	randSnap = rand.randint(0,7)
	if randSnap == 0:
		snapBio = "snap: "+firstName+lastName+lastLetterL
	elif randSnap == 1:
		snapBio = "sc: "+firstName+lastLetterF+lastName
	elif randSnap == 2:
		snapBio = emoji.emojize(":ghost: snap: "+firstName+lastName)
	elif randSnap == 3:
		snapBio = emoji.emojize("snapchat: "+firstName+lastName+collectionD[randomDate])
	elif randSnap == 4:
		snapBio = emoji.emojize(":ghost: snapchat: "+lastName+firstName+lastLetterF)
	else:
		snapBio = ""

	# University
	if randomDate == 0 or randomDate == 1 or randomDate == 2 or randomDate == 3:
		randUniFormat = rand.randint(0,8)
		randUni = rand.randint(0,6)
		if randUniFormat == 0:
			schoolBio = collectionU[randUni]
		elif randUniFormat == 1:
			schoolBio = collectionU[randUni]+" "+collectionG[randomDate]
		elif randUniFormat == 2:
			schoolBio = collectionU[randUni]+" | "+collectionG[randomDate]
		elif randUniFormat == 3:
			schoolBio = emoji.emojize(":books: "+collectionG[randomDate]+" | "+collectionU[randUni])
		elif randUniFormat == 4:
			schoolBio = collectionU[randUni]+" U"
		elif randUniFormat == 5:
			schoolBio = collectionU[randUni]+" Uni "+collectionG[randomDate] 
		else:
			schoolBio = ""
		
	# HighSchool
	else:
		randUni = rand.randint(6, len(collectionU)-2)
		randSchoolFormat = rand.randint(0,7)
		#randSchool = rand.randint(6, len(collectionU))
		if randSchoolFormat == 0:
			schoolBio = collectionU[randUni]
		elif randSchoolFormat == 1:
			schoolBio = collectionU[randUni]+" "+collectionG[rand.randint(5,6)]
		elif randSchoolFormat == 2:
			schoolBio = collectionU[randUni]+" > "+collectionU[rand.randint(0,6)]
		elif randSchoolFormat == 3:
			schoolBio = emoji.emojize(":books:"+collectionU[randUni])
		elif randSchoolFormat == 4:
			schoolBio = emoji.emojize(collectionU[randUni]+' :apple:')
		else:
			schoolBio = ""
	# Location
	randLocation = rand.randint(0,7)
	# Halifax
	if randUni == 0 or randUni == 5 or randUni == 6 or randUni == 7 or randUni == 8:
		if randLocation == 0:
			locatBio = "LDN"
		elif randLocation == 1:
			locatBio = "london"
		elif randLocation == 2:
			locatBio = "London"
		elif randLocation == 3:
			locatBio = "London Eng"
		elif randLocation == 4:
			locatBio = emoji.emojize(":round_pushpin: England") 
		elif randLocation == 5:
			locatBio = emoji.emojize(":england:")
		else:
			locatBio = ""
	elif randUni == 2 or randUni == 4:
		if randLocation < 1:
			locatBio = "ON"
		elif randLocation == 2 or randLocation == 3:
			locatBio = "Ontario"
		elif randLocation == 4:
			locatBio = emoji.emojize(":house: Ontario")
		else: 
			locatBio = ""
	elif randUni == 3:
		if randLocation > 2:
			locatBio = "New York"
		elif randLocation == 3 or randLocation == 4:
			locatBio = "New York, NY"
		else:	
			locatBio = ""
	# Hobby&Extra
	if randHobby == 1:
		randHobbyEmoji = rand.randint(0,13)
		if randHobbyEmoji == 0:
			hobbyBio = emoji.emojize(":soccer:")
		elif randHobbyEmoji == 1:
			hobbyBio = emoji.emojize(":football:")
		elif randHobbyEmoji == 2:
			hobbyBio = emoji.emojize(":hockey:")
		elif randHobbyEmoji == 3:
			hobbyBio = emoji.emojize(":snowboarder:")
		elif randHobbyEmoji == 4:
			hobbyBio = emoji.emojize(":sailboat:")
		elif randHobbyEmoji == 5:
			hobbyBio = emoji.emojize(":swimmer:")
		elif randHobbyEmoji == 6:
			hobbyBio = emoji.emojize(":baseball:")
		elif randHobbyEmoji == 7:
			hobbyBio = emoji.emojize(' :headphones:')
		elif randHobbyEmoji == 8:
			hobbyBio = emoji.emojize(":tennis:")
		elif randHobbyEmoji == 9 or randHobbyEmoji == 10:
			hobbyBio = emoji.emojize(":basketball:")
		else:
			hobbyBio = ""

def formatBio():
	randBio1 = 6
	randBio2 = 6
	randBio3 = 6
	randBio4 = 6
	randomBio1 = rand.randint(0, 5)
	connectors = [" ", " | "]
	connector = connectors[rand.randint(0, len(connectors)-1)]
	global bio
	bio = ""

	#Snap
	if randomBio1 == 0:
		bio = bio+snapBio
	#School
	elif randomBio1 == 1:
		bio = bio+schoolBio
	#Hobby
	elif randomBio1 == 2:
		bio = bio+hobbyBio
	#Location
	elif randomBio1 == 3:
		bio = bio+locatBio

	randomBio2 = rand.randint(0, 5)
	#Snap2
	if randomBio2 == 0:
		if randomBio1 != 0:
			if bio == "":
				bio = snapBio
			else:
				bio = bio+connector+snapBio
	#School2
	elif randomBio2 == 1:
		if randomBio1 != 1:
			if bio == "":
				bio = schoolBio
			else:
				bio = bio+connector+schoolBio
	#Hobby2
	elif randomBio2 == 2:
		if randomBio1 != 2:
			if bio == "":
				bio = hobbyBio
			else:
				bio = bio+connector+hobbyBio
	#Location2
	elif randomBio2 == 3:
		if randomBio1 != 3:
			if bio == "":
				bio = locatBio
			else:
				bio = bio+connector+locatBio

	randomBio3 = rand.randint(0, 5)
	#Snap3
	if randomBio3 == 0:
		if randomBio1 != 0 and randomBio2 != 0:
			if bio == "":
				bio = snapBio
			else:
				bio = bio+connector+snapBio
	#School3
	elif randomBio3 == 1:
		if randomBio1 != 1 and randomBio2 != 1:
			if bio == "":
				bio = schoolBio
			else:
				bio = bio+connector+schoolBio
	#Hobby3
	elif randomBio3 == 2:
		if randomBio1 != 2 and randomBio2 != 2:
			if bio == "":
				bio = hobbyBio
			else:
				bio = bio+connector+hobbyBio
	#Location3
	elif randomBio3 == 3:
		if randomBio1 != 3 and randomBio2 != 3:
			if bio == "":
				bio = locatBio
			else:
				bio = bio+connector+locatBio

	randomBio4 = rand.randint(0, 5)
	#Snap4
	if randomBio4 == 0:
		if randomBio1 != 0 and randomBio2 != 0 and randomBio3 != 0:
			if bio == "":
				bio = snapBio
			else:
				bio = bio+connector+snapBio
	#School4
	elif randomBio4 == 1:
		if randomBio1 != 1 and randomBio2 != 1 and randomBio3 != 1:
			if bio == "":
				bio = schoolBio
			else:
				bio = bio+connector+schoolBio
	#Hobby4
	elif randomBio4 == 2:
		if randomBio1 != 2 and randomBio2 != 2 and randomBio3 != 2:
			if bio == "":
				bio = hobbyBio
			else:
				bio = bio+connector+hobbyBio
	#Location4
	elif randomBio4 == 3:
		if randomBio1 != 3 and randomBio2 != 3 and randomBio3 != 3:
			if bio == "":
				bio = locatBio
			else:
				bio = bio+connector+locatBio

def storeInFirebaseF(FirstName, LastName, Username1, Username2, Username3, Username4, Username5, Username6, Username7, Username8, Username9, Username10, Username11, Username12, Username13, Bio, DisplayName):
        post = firebase.post('/profilesF', {'FirstName' : FirstName, 'LastName' : LastName, 'Username1' : Username1, 'Username2' : Username2, 'Username3' : Username3, 'Username4' : Username4, 'Username5' : Username5, 'Username6' : Username6, 'Username7' : Username7, 'Username8' : Username8, 'Username9' : Username9, 'Username10' : Username10, 'Username11' : Username11, 'Username12' : Username12, 'Username13' : Username13, 'Bio' : Bio, 'DisplayName' : DisplayName, 'Password' : "Fr0$tByt3"})
        return post

def storeInFirebaseM(FirstName, LastName, Username1, Username2, Username3, Username4, Username5, Username6, Username7, Username8, Username9, Username10, Username11, Username12, Username13, Bio, DisplayName):
        post = firebase.post('/profilesM', {'FirstName' : FirstName, 'LastName' : LastName, 'Username1' : Username1, 'Username2' : Username2, 'Username3' : Username3, 'Username4' : Username4, 'Username5' : Username5, 'Username6' : Username6, 'Username7' : Username7, 'Username8' : Username8, 'Username9' : Username9, 'Username10' : Username10, 'Username11' : Username11, 'Username12' : Username12, 'Username13' : Username13, 'Bio' : Bio, 'DisplayName' : DisplayName, 'Password' : "Fr0$tByt3"})
        return post

with open("data.json") as data_file:
	#Get Json File
	data = json.load(data_file)
	
	#Get First Name (M)
	for name in data['firstNamesM']:
		collectionM.append(data['firstNamesM'][str(name)]['firstNameM'])
	#Get First Names (F)	
	for name in data['firstNamesF']:
		collectionF.append(data['firstNamesF'][str(name)]['firstNameF'])

	#Get Last Names	
	for name in data['lastNames']:
		collectionL.append(data['lastNames'][str(name)]['lastNames'])
	i = 0
	global lastNameCount
	#Create Rand Profile

	#INSERT HERE
	lastNameCount = 407

	for i in range(0,len(collectionF)):
		collectionUsernames = []
		randomProfileInt = rand.randint(0, len(collectionD))
		#Fn, Ln, displayName, Un, Pass, Bio
		#First Name
		firstName = collectionF[i]
		#Last Name			
		lastName = collectionL[lastNameCount]
		#Display Name			
		randomDisplayInt = rand.randint(0, 6)
		displayName = "-"
		if randomDisplayInt == 0 or randomDisplayInt == 1 or randomDisplayInt == 2:
			displayName = str(firstName)+" "+str(lastName)
		elif randomDisplayInt == 3 or randomDisplayInt == 4:
			displayName = str(firstName)
		else:
			displayName = str(firstName)+" "+(lastName[:1])
		#Usernames	
		lastLetterL = str(lastName[-1:])
		lastLetterF = str(firstName[-1:])
		global randomDate
		# Create 12 different usernames to ensure availability
		randomDate = rand.randint(0, (len(collectionD)-1))
		username1 = collectionF[i]+collectionL[lastNameCount]
		username2 = collectionF[i]+"_"+collectionL[lastNameCount]
		username3 = collectionF[i]+"."+collectionL[lastNameCount]
		username4 = collectionF[i]+collectionL[lastNameCount]+lastLetterL+lastLetterL
		username5 = collectionF[i]+collectionL[lastNameCount]+collectionD[randomDate]
		username6 = collectionF[i]+"."+collectionL[lastNameCount]
		username7 = collectionF[i]+collectionL[lastNameCount]+"_"
		username8 = collectionL[lastNameCount]+collectionF[i]
		username9 = collectionL[lastNameCount]+collectionF[i]+lastLetterF
		username10 = collectionF[i]+collectionL[lastNameCount]+str(rand.randint(100, 10000))
		username11 = collectionF[i]+lastLetterF+lastLetterF
		username12 = "_"
		username13 = "_"
		if randomDate == 0 or randomDate == 1 or randomDate == 2:
			username12 = collectionF[i]+collectionL[lastNameCount]+"19"+collectionD[randomDate]
			username13 = collectionF[i]+"."+collectionL[lastNameCount]+"19"+collectionD[randomDate]
		else:
			username12 = collectionF[i]+collectionL[lastNameCount]+"20"+collectionD[randomDate]
			username13 = collectionF[i]+"."+collectionL[lastNameCount]+"20"+collectionD[randomDate]
		
		# Add all usernames to one array
		collectionUsernames.append(str(username1))
		collectionUsernames.append(str(username2))
		collectionUsernames.append(str(username3))
		collectionUsernames.append(str(username4))
		collectionUsernames.append(str(username5))
		collectionUsernames.append(str(username6))
		collectionUsernames.append(str(username7))
		collectionUsernames.append(str(username8))
		collectionUsernames.append(str(username9))
		collectionUsernames.append(str(username10))
		collectionUsernames.append(str(username11))
		collectionUsernames.append(str(username12))
		collectionUsernames.append(str(username13))
		
			
		global bio
		global schoolBio
		global snapBio
		global locatBio
		global hobbyBio
		
		bio = ""
		schoolBio = ""
		snapBio = ""
		locatBio = ""
		hobbyBio = ""
		createBio()	
		# Format
		formatBio()
		print(str(i))
		print(str(lastNameCount)+")F")
		print("First Name: "+firstName)
		print("Last Name: "+lastName)
		print("Username: "+str(collectionUsernames))
		print("Bio: "+bio)
		print("Display Name: "+displayName)
		print("Password: "+password)
		time.sleep(1)
		# Post to Firebase
		print("Uploading To Database")
		storeInFirebaseF(firstName, lastName, collectionUsernames[0], collectionUsernames[1], collectionUsernames[2], collectionUsernames[3], collectionUsernames[4], collectionUsernames[5], collectionUsernames[6], collectionUsernames[7], collectionUsernames[8], collectionUsernames[9], collectionUsernames[10], collectionUsernames[11], collectionUsernames[12], bio, displayName)
		print("Upload Complete!")
		time.sleep(2)
		
		lastNameCount = lastNameCount+1
		



