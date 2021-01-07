#1) Configure Firebase//
#2) Initialize Variables
#3) Print IP (ask if ok)
#4) if ok, open instagram; else, close program (at.exit)
#5) after (x) number of loops, stop loop
#6) write all names down in .txt file (edit, don't replace)
#7) close program (at exit)

import socket
import botcore
import random
from time import sleep

# Present a list of functions you can run in the console
def help():
    print("bot.help() .......................................... Request Help from Bot")
    print("GetIP() ............................................. Get Current IP")
    print("record(username, email, name) ....................... Record Current Info to TXT")
    print("retrieve(lineNumber) ................................. Get Info from TXT")
    print("createCredentials() ................................. Create new Credentials")


# *** Fill in These ***
pw = ""
oldRecord = ""
newRecord = ""
# *********************


# Save a reference to a botcore.py driver
bot = botcore.driver
# List of legal characters for a random name, username, and email
letterBank = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890._"
# Save IP to be compared before and after vpn is applied
myIP = ""
# Save bot name, username, and email
botUsername, botEmail, botName = "", "", ""
# Save currently using/new name, username, and email
currentUsername, currentEmail, currentName, currentLine = "", "", "", ""
# Track number of users created in current session
createUserCounter = 1
# Parse record and retrieve functions without using strings explicitly
new = "new"
old = "old"


# Check IP Before Executing
def getIP():
    hostname = socket.gethostname()    
    myIP = socket.gethostbyname(hostname)
    print("My IP is "+myIP)

# Create a random break between actions to mimic human users
def randomTimer():
    time = random.random()
    time = time + (random.randint(1, 3))
    return time

# Register to .txt 
def record(ref):
	# If trying to reference older data records
    if ref == "old":
    	# Open file and save reference
        readFile = open(oldRecord, "r")
        file = open(oldRecord, "+a")
        # Get user number by dividing total number of lines in file by 5, as there are 5 lines per user
        lineNum = (len(readFile.readlines())/5)
        file.write(str(lineNum)+"\n")
        # Insert credentials to database
        file.write(currentUsername+"\n")
        file.write(currentName+"\n")
        file.write(currentEmail+"\n")
        # Close Files
        readFile.close()
        file.close()
	# If trying to reference newer data records
    elif ref == "new":
    	# Open file and save reference
        readFile = open(newRecord, "r")
        file = open(newRecord, "+a")
        # Get user number by dividing total number of lines in file by 5, as there are 5 lines per user
        lineNum = (len(readFile.readlines())/5)
        file.write(str(lineNum)+"\n")
        # Insert credentials to database
        file.write(currentUsername+"\n")
        file.write(currentName+"\n")
        file.write(currentEmail+"\n")
        file.write("\n")
        # Close Files
        readFile.close()
        file.close()
    # If invalid choice was parsed
    else:
    	# Return error
        print("ref: "+ref+" is not recognized (old/new)")

# Retrieve info from .txt
def retrieve(ref, lineNumber):
	# Reference global credential variables to reference later in other functions
    global currentUsername, currentEmail, currentName
    # If trying to referece old records
    if ref == old:
    	# Open file and save reference
        file = open(oldRecord, "r")
        # Get number of lines
        lines = file.readlines()
        # Translate user number to line number
        lineNumber = lineNumber*5
        # Remove "/n"
        currentLine = lines[int(lineNumber)][:-1]
        currentUsername = lines[int(lineNumber)+1][:-1]
        currentName = lines[int(lineNumber)+2][:-1]
        currentEmail = lines[int(lineNumber)+3][:-1]
        # Close File
        file.close()
    # If trying to reference new records
    elif ref == new:
    	# Open file and save reference
        file = open(newRecord, "r")
        # Get number of lines
        lines = file.readlines()
        # Translate user number to line number
        lineNumber = lineNumber*5
        # Remove "/n"
        currentLine = lines[int(lineNumber)][:-1]
        currentUsername = lines[int(lineNumber)+1][:-1]
        currentName = lines[int(lineNumber)+2][:-1]
        currentEmail = lines[int(lineNumber)+3][:-1]
        # Close File
        file.close()
    # If invalid choice was parsed
    else:
    	# Return error to console
        print("ref: "+ref+" is not recognized (old/new)")

# Create a random string of characters for username
def createCredentials():
	# Reference global credential variables to reference later in other functions	
    global currentUsername, currentName, currentEmail
    # Clear current credential variables
    currentEmail = ""
    currentName = ""
    currentUsername = ""

    # Create username
    # Create random username length between 7 and 12 characters long
    randomUsernameLength = random.randint(7, 12)
    # For each letter in username
    for _ in range(randomUsernameLength):
    	# Choose a random letter in the letterBank variable
        randomLetterInt = random.randint(0, len(letterBank))
        randomLetter = letterBank[randomLetterInt]
        # Add letter to username variable
        currentUsername = currentUsername + randomLetter
    
    # Create Email
    # Email domains
    emailEndings = ["@gmail.com", "@hotmail.com", "@mail.com", "@outlook.com"]
    # Email is random username plus random extension from emailEndings array
    currentEmail = currentUsername+emailEndings[random.randint(0, len(emailEndings)-1)]
    
    # Create name
    # Create random name length between 3 and 9 characters long
    nameLength = random.randint(3, 9)
    # For each letter in the name
    for _ in random.range(nameLength):
    	# Choose a random letter from letterBank
        randomLetterInt = random.randint(0, 26)
        # Add random new letter to name
        currentName = currentName+letterBank[randomLetterIntt]
    # Print random credentials
    print("CurrentName:     "+currentName)
    print("CurrentEmail:    "+currentEmail)
    print("CurrentUsername: "+currentUsername)


# Example of bot_center.py working after establishing database and credentials
def main():
	# Create Selenium webdriver via botcore.py
    botcore.createWebdriver()
    # Rerieve credentials from new database
    retrieve(new, 1)
    # Delay
    sleep(randomTimer())
    # Sign in with retrieved data
    botcore.signIn(bot[0], currentUsername)
    # Delay
    sleep(randomTimer())
