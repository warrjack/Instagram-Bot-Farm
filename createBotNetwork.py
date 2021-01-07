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
profilePassword = ''
firebaseRef = ''
#############################

driver = webdriver.Chrome()

currentUsernameLogged = ""

usernameIdCollection = []
usernameCollection = []

fProfileIdCollection = []
fProfileBioCollection = []
fProfileDisplayCollection = []
fProfileFirstNameCollection = []
fProfileLastNameCollection = []
fProfileUsernameCollection = []

loopInt = 0

ref = firebase.FirebaseApplication(firebaseRef)

#Get Usernames from Firebase and put them into list.
def getUsernames():   
    usernameResult = ref.get('/usernames', None)
    print("Fetching UsernameID...")
    for a in usernameResult:
      usernameIdCollection.append(a.strip().decode())
    print("Caught all UsernameIDs")
    i = 0
    print("Fetching All Usernames from IDs...")
    for b in usernameIdCollection:
        username = ref.get('/usernames/'+b+'/emptysUsername', None)
        print(username)
        
    print("... Caught all usernames, usernameCollection Length: ", len(usernameCollection))

#Get Firebase Data
def getProfileData():
    print("Fetching all ProfileIDs...")
    ProfileResult = ref.get('/profiles', None)
    for c in ProfileResult:
        ProfileIdCollection.append(c.strip().decode())
    i = 0
    print("...Caught all ProfileFIDs")
    print("Collectiong all ProfileData...")
    for d in ProfileIdCollection:
        Bio = ref.get('/profiles/'+d+'/Bio', None)
        Display = ref.get('/profiles/'+d+'/DisplayName', None)
        FN = ref.get('/profiles/'+d+'/FirstName', None)
        LN = ref.get('/profiles/'+d+'/LastName', None)
        x = 1
        print("Getting Usernames 1-12...")
        usernameCollection = []
        for x in range (1,13):
            usernameCollection.append(ref.get('/profiles/'+str(d)+'/Username'+str(x), None))
            print(usernameCollection[x-1])
                                           
        print("...Usernames Recieved")
        ProfileBioCollection.append(Bio)
        ProfileDisplayCollection.append(Display)
        ProfileFirstNameCollection.append(FN)
        ProfileLastNameCollection.append(LN)
        ProfileUsernameCollection.append(usernameCollection)
        print('Profiles Built! \n \n')
        i += 1

print("Webdriver Created...")

#Log into Instagram
def logIn(username):
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    print("Logging In...")
    usernameField = driver.find_element_by_name("username")
    usernameField.clear()
    usernameField.send_keys(str(username))
    passwordField = driver.find_element_by_name("password")
    passwordField.clear()
    passwordField.send_keys("Fr0$tByt3")
    passwordField.send_keys(Keys.ENTER)
    print("Checking if credentials are valid...")
    sleep(2)

#Check if login was successful
def checkLogIn():
    if driver.find_element_by_name("username"):
        loopInt += 1
        print(loopInt, "Credentials failed, retrying...")
        f = open("brokenCreds.txt","w+")
        f.write(str(loopInt)+", ")
        f.close()
        logIn(usernameCollection[loopInt])
    else:
        print("Log in successful!")
        currentUsernameLogged = str(usernameCollection[loopInt])
        f = open("validCreds.txt","w+")
        f.write(str(loopInt)+", ")
        f.close()
        goToProfile()

#Go to And edit profile
def goToProfile():
    driver.get("https://www.instagram.com/accounts/edit/")
    print("Editing Profile")

    nameField = driver.find_element_by_name("pepName")
    nameField.clear()
    nameField.send_keys(str(fProfileFirstNameCollection[loopInt])+" "+fProfileLastNameCollection[loopInt])
    bioField = driver.find_element_by_name("pepBio")
    bioField.clear()
    bioField.send_keys(str(emoji.emojize(fProfileBioCollection[loopInt])))
    sleep(1)
    profilePicButton = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[2]/button")
    profilePicButton.click()
    profilePicYes = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
    profilePicYes.click()
    ####################
    ####################
    ####################
    pyautogui.typewrite("/Path/To/Image/Collection")
    ####################
    ####################
    ####################
    print("Profile set before submit loop...")

    usernameField = driver.find_element_by_name("pepUsername")
    submitBtn = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/form/div[10]/div/div/button[1]")

    for x in range(0, 12):
        usernameSelected = str(usernameCollection[loopInt][x])
        username.clear()
        username.send_keys(usernameSelected)
        print("Username Set x: ", x)
        submitBtn.click()
    
    print("Profile Submitted, Refreshing...")
    driver.get("https://www.instagram.com/accounts/edit/")
    usernameFieldFinal = driver.find_element_by_name("pepUsername")
    usernameText = usernameFieldFinal.text
    currentUsernameLogged = str(usernameText)

    #Recording Data
    w = open("UsernamesSelected.txt", "w+")
    w.write(usernameText+", ")
    w.close()
    
    f = open("UsersCompleted.txt","w+")
    f.write(str(loopInt)+", ")
    f.close()
    sleep(2)

#Follow Other Bots (Chosen Randomly)
def followPeople():
    peopleToFollow = []
    z = randint(6, 18)
    aa = 0
    for aa in range(0, z):
        peopleToFollow.append(usernameCollection(randint(0, len(usernameCollection))))
    for user in peopleToFollow:
        driver.get("https://www.instagram.com/"+str(user)+"/")
        followButton = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[2]/span/span[1]/button")
        followButton.click()
        sleep(randint(600, 1800))
        
def followMe():
    driver.get("https://www.instagram.com/jack.warrr/")
    followButtonMe = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[2]/span/span[1]/button")
    sleep(1)
    
def likeMeRecent():
    driver.get("https://www.instagram.com/p/BtO4S7inpD4/")
    likeButton = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/article/div[2]/section[1]/span[1]/button/span")          
    likeButton.click()

#Log out of current account
def logOut():
    driver.get("https://www.instagram.com/"+str(currentUsernameLogged)+"/")
    settingsButton = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div/button/span")
    settingsButton.click()
    logoutButton = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/button[6]")
    logoutButton.click()

#Dispose Selenium
def close():
    driver.close()
    driver.dispose()

#Close Current VPN
def closeVPN():
    print("Closing VPN")

#Open New VPN
def openVPN():
    print("Opening VPN")
    
#Submit loop, try every(all 12) usernames  
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
    getFProfileData()
    #login
    logIn(usernameCollection[loopInt])
    #check if logged in
    checkLogIn()
    #go to own profile and edit
    goToProfile()
    if loopInt > 19:
        followPeople()    

atexit.register(close)
start()


