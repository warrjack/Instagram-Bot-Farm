import os
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from firebase import firebase
from random import randint
import emoji
import atexit
import pyautogui


# Configure
#############################
firebaseRef = ''
profilePassword = ''
profileImagePath = ''
numberOfLoops = 0
#############################

driver = webdriver.Chrome()

currentUsernameLogged = ""

# Username IDs (the random parent string)
usernameIdCollection = []
# Usernames (child of Username ID)
usernameCollection = []

# Collection of all data fetched from firebase
ProfileIdCollection = []
ProfileBioCollection = []
ProfileDisplayCollection = []
ProfileFirstNameCollection = []
ProfileLastNameCollection = []
ProfileUsernameCollection = []

loopInt = 0

# Set firebase reference
ref = firebase.FirebaseApplication(firebaseRef)

#Get Usernames from Firebase and put them into list.
def getUsernames():   
    # Fetch username IDs
    usernameResult = ref.get('/usernames', None)
    print("Fetching UsernameID...")
    for a in usernameResult:
      usernameIdCollection.append(a.strip().decode())
    print("Caught all UsernameIDs")
    i = 0
    print("Fetching All Usernames from IDs...")
    #Fetch usernames
    for b in usernameIdCollection:
        username = ref.get('/usernames/'+b+'/emptysUsername', None)
        print(username)
        
    print("... Caught all usernames, usernameCollection Length: ", len(usernameCollection))

# Get Firebase Data
def getProfileData():
    # Fetch all profile IDs
    print("Fetching all ProfileIDs...")
    ProfileResult = ref.get('/profiles', None)
    # Add all credentials into an array as a string
    for c in ProfileResult:
        ProfileIdCollection.append(c.strip().decode())
    i = 0
    print("...Caught all ProfileIDs")
    print("Collectiong all ProfileData...")
    # Fetch individual info from profile data
    for d in ProfileIdCollection:
        Bio = ref.get('/profiles/'+d+'/Bio', None)
        Display = ref.get('/profiles/'+d+'/DisplayName', None)
        FN = ref.get('/profiles/'+d+'/FirstName', None)
        LN = ref.get('/profiles/'+d+'/LastName', None)
        x = 1
        print("Getting Usernames 1-12...")
        # Usernames come in sets of 12 (12 usernames to choose incase of username being taken)
        usernameCollection = []
        for x in range (1,13):
            usernameCollection.append(ref.get('/profiles/'+str(d)+'/Username'+str(x), None))
            print(usernameCollection[x-1])
                                           
        # Save fetched results into array
        print("...Usernames Recieved")
        ProfileBioCollection.append(Bio)
        ProfileDisplayCollection.append(Display)
        ProfileFirstNameCollection.append(FN)
        ProfileLastNameCollection.append(LN)
        ProfileUsernameCollection.append(usernameCollection)
        print('Profiles Built! \n \n')
        i += 1

print("Webdriver Created...")

# Log into Instagram
def logIn(username):
    # Go to login
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    print("Logging In...")
    # Innput Username
    usernameField = driver.find_element_by_name("username")
    usernameField.clear()
    usernameField.send_keys(str(username))
    # Input Password
    passwordField = driver.find_element_by_name("password")
    passwordField.clear()
    passwordField.send_keys(pw)
    # Submit form
    passwordField.send_keys(Keys.ENTER)
    print("Checking if credentials are valid...")
    sleep(2)

#Check if login was successful
def checkLogIn():
    # If driver can fine element "Username"
    if driver.find_element_by_name("username"):
        loopInt += 1
        print(loopInt, "Credentials failed, retrying...")
        # Save credential as not working in local .txt
        f = open("brokenCreds.txt","w+")
        f.write(str(loopInt)+", ")
        f.close()
        # Try again with a different username
        logIn(usernameCollection[loopInt])
    else:
        # Log in worked
        print("Log in successful!")
        # Save current username logged in 
        currentUsernameLogged = str(usernameCollection[loopInt])
        # Save working username to local .txt
        f = open("validCreds.txt","w+")
        f.write(str(loopInt)+", ")
        f.close()

#Go to And edit profile
def goToProfile():
    # Open self profile to edit
    driver.get("https://www.instagram.com/accounts/edit/")
    print("Editing Profile")

    # Change name
    nameField = driver.find_element_by_name("pepName")
    nameField.clear()
    nameField.send_keys(str(fProfileFirstNameCollection[loopInt])+" "+fProfileLastNameCollection[loopInt])
    # Change bio
    bioField = driver.find_element_by_name("pepBio")
    bioField.clear()
    bioField.send_keys(str(emoji.emojize(fProfileBioCollection[loopInt])))
    sleep(1)
    # Change profile image
    profilePicButton = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[2]/button")
    profilePicButton.click()
    profilePicYes = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
    profilePicYes.click()
    pyautogui.typewrite(profileImagePath)
    print("Profile set before submit loop...")
    # Change username
    usernameField = driver.find_element_by_name("pepUsername")
    submitBtn = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/form/div[10]/div/div/button[1]")

    #Set username to each username in collection until one is available
    for x in range(0, 12):
        usernameSelected = str(usernameCollection[loopInt][x])
        username.clear()
        username.send_keys(usernameSelected)
        print("Username Set x: ", x)
        submitBtn.click()
    # Submit new profile 
    print("Profile Submitted, Refreshing...")
    driver.get("https://www.instagram.com/accounts/edit/")
    usernameFieldFinal = driver.find_element_by_name("pepUsername")
    usernameText = usernameFieldFinal.text
    # Save new username
    currentUsernameLogged = str(usernameText)

    # Recording username just selected .txt
    w = open("UsernamesSelected.txt", "w+")
    w.write(usernameText+", ")
    w.close()

    #Record user completed in local .txt
    f = open("UsersCompleted.txt","w+")
    f.write(str(loopInt)+", ")
    f.close()
    sleep(2)

# Follow Other Bots (Chosen Randomly)
def followPeople():
    peopleToFollow = []
    z = randint(6, 18)
    aa = 0
    # Add all previously made users to 'peopleToFollow[]'
    for aa in range(0, z):
        peopleToFollow.append(usernameCollection(randint(0, len(usernameCollection))))
    # For each user in 'peopleToFollow[]', follow
    for user in peopleToFollow:
        # Go to selected user profile
        driver.get("https://www.instagram.com/"+str(user)+"/")
        # Find and click follow button
        followButton = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[2]/span/span[1]/button")
        followButton.click()
        sleep(randint(600, 1800))

# Log out of current account
def logOut():
    # Go to profile
    driver.get("https://www.instagram.com/"+str(currentUsernameLogged)+"/")
    # Click on Settings
    settingsButton = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div/button/span")
    settingsButton.click()
    # Click on log out button on pop-up
    logoutButton = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/button[6]")
    logoutButton.click()

# Dispose Selenium
def close():
    driver.close()
    driver.dispose()

# Close Current VPN
def closeVPN():
    print("Closing VPN")

# Open New VPN
def openVPN():
    print("Opening VPN")
    
# Submit loop, try every(all 12) usernames  
def loop():
    print("beginning loop")
    while len(usernameCollection) > loopInt:
        print("(OpenVPN) loop Number: ", loopInt)
        openVPN()
        print("(LogIn) loop Number: ", loopInt)
        logIn(usernameCollection[loopInt])
        print("(followPeople) loop Number: ", loopInt)
        followPeople()
        print("(LogOut) loop Number: ", loopInt)
        logout()
        print("(Close) loop Number: ", loopInt)
        close()
        print("(CloseVPN) loop Number: ", loopInt)
        closeVPN()
        
        loopInt += 1

#Caught all data
def done():
    print(ProfileIdCollection)
    print(ProfileBioCollection)
    print(ProfileDisplayCollection)
    print(ProfileFirstNameCollection)
    print(ProfileLastNameCollection)
    print(ProfileUsernameCollection)
    print("Complete!, No errors!")

def start():
    #fetch username ID's
    getUsernames()
    #fetch firebase data
    getProfileData()
    #login
    logIn(usernameCollection[loopInt])
    #check if logged in
    checkLogIn()
    #go to own profile and edit
    goToProfile()
    if loopInt > numberOfLoops:
        followPeople()    

atexit.register(close)


