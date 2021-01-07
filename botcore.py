#1) Configure Firebase//
#2) Initialize Variables
#3) Print IP (ask if ok)
#4) if ok, open instagram; else, close program (at.exit)
#5) after (x) number of loops, stop loop
#6) write all names down in .txt file (edit, don't replace)
#7) close program (at exit)

import socket
import atexit
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random
from pynput.keyboard import Key, Controller
keyboard = Controller()

# Configure
#############################
pw = ""
profilePicLocation = ""
chromeDriver = ""
#############################

# Most recent bot number
numberAtOnList = 0
# List of webdrivers
driver = []
# Current credentials using
currentUsername = ""
currentEmail = ""
currentName = ""
# Number of users created
createUserCounter = 1

# Present a list of functions you can run in the console
def help():
    print("createWebdriver().................................... Open New Driver/Browser")
    print("closeWebdriver(driverNumber) ........................ Close Driver/Browser by Number")
    print("signUp(driverID, email, fullName, username) ......... Sign New Account to Instagram By DriverNumber")
    print("createCredentials() ................................. Creates Random Strings for Email, Name, and Username")
    print("signIn(driverID, username)........................... Sign in account")
    print("signUp(driverID, email, fullName, username) ......... Sign up account")
    print("checkIfSignedUp(driverID) ........................... Check If Sign Up Worked (returns True or False)")
    print("follow(driverID, username)........................... Follow Specific User")
    print("unfollow(driverID, username)......................... Unfollow Specific User")
    print("changeCredentials(driverID, name, username, bio) .... Change info of current User")

# Create a random break between actions to mimic human users
def randomTimer():
    time = random.random()
    time = time + (random.randint(1, 3))
    return time

# Create New Chrome Browser
def createWebdriver():
	# Create new driver
    driv = webdriver.Chrome(chromeDriver)
    # Open instagram.com
    driv.get('https://www.instagram.com/')
    # Set window stats
    driv.set_window_size(800, 800)
    driv.set_window_position(0, 0)
    # Add driver to driver collection
    driver.append(driv)
    print("Started Driver " + str(len(driver) - 1))

# Close Chrome Browser(at instance)
def closeWebdriver(driverNumber):
	# Close down driver from driver collection
    driver[driverNumber].quit()
    # Remove driver from driver collection
    del driver[driverNumber]
    loopNumber = 0
    print("Drivers Int Changed.")
    # Show driver position changes 
    for item in driver:
        print("Webdriver " + str(loopNumber) + ": " + str(driver[loopNumber].current_url))
        loopNumber += 1

# Close All Windows When Program is Terminated
def exitHandler():
    for element in driver:
        element.quit()
# Register exit routine to exitHandler()
atexit.register(exitHandler)

# Sign into pre set account
def signIn(driverID, username):
	# Reference global password
    global pw
    # Go to instagram login page
    driverID.get("http://instagram.com/accounts/login/?source=auth_switcher")
    sleep(randomTimer())
    # Attempt to log in with given username and global password
    try:
        driverID.find_element_by_name('username').send_keys(username)
        sleep(randomTimer())
        
        driverID.find_element_by_name('password').send_keys(pw)
        sleep(randomTimer())
        driverID.find_element_by_xpath("//*[text()='Log In']").click()
        # Check for optional pop up after sign in
        try:
            sleep(randomTimer())
            driverID.find_element_by_xpath('//*[text()="Not Now"]').click()
        except:
            print("No Pop Up")
    # Sign in attempt failed
    except NoSuchElementException:
        print("Sign In Failed...")

#Sign Up to Instagram
def signUp(driverID, email, fullName, username):
	# Navigate to Instagram home page
    driverID.get('https://www.instagram.com')
    sleep(2)
    # Fill in credentials
    driverID.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(email)
    sleep(1)
    driverID.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/div/label/input').send_keys(fullName)
    sleep(1.5)
    driverID.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[5]/div/label/input').send_keys(username)
    sleep(2)
    driverID.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/div/label/input').send_keys(pw)
    sleep(3)
    # Submit
    driverID.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[7]/div/button').click()

#Check if login textfield still exist to see if signed up
def checkIfSignedUp(driverID):
	# Check for element exists after sign in/up
    try:
        driverID.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
    except NoSuchElementException:
        print("Login/Sign Up Failed")
        return False
    print("Login/Sign up Succeeded")
    return True

# Edits Profile to change current profile info
def changeCredentials(driverID, currentUsername, name, username, bio):
    # Go To Profile
    driverID.get("https://www.instagram.com/"+currentUsername)
    driverID.find_element_by_xpath("//*[text()='Edit Profile']").click()
    sleep(randomTimer())
    # Name
    driverID.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[1]/div/input").clear()
    driverID.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[1]/div/input").send_keys(name)
    sleep(randomTimer())
    # Username
    driverID.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[2]/div/input").clear()
    driverID.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[2]/div/input").send_keys(username)
    sleep(randomTimer())
    # Bio
    driverID.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[4]/div/textarea").clear()
    driverID.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[4]/div/textarea").send_keys(bio)
    sleep(randomTimer())
    # ProfileImage
    driverID.find_element_by_xpath("//*[text()='Change Profile Photo']").click()
    sleep(randomTimer())
    sleep(randomTimer())
    # Choose photo on computer
    keyboard.type(profilePicLocation+str(createUserCounter)+".jpg")
    sleep(randomTimer())
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(randomTimer())
    # Submit changes
    driverID.find_element_by_xpath("//*[text='Submit']")

# Follows specific user
def follow(driverID, username):
	# Go to user's page
    driverID.get("https://www.instagram.com/"+str(username))
    sleep(randomTimer())
    try:
        driverID.find_element_by_xpath("//*[text()='Follow']").click()
        print("Followed: "+username)
    except NoSuchElementException:
        print("unable to find follow button")

# Unfollows specific user
def unfollow(driverID, username):
	# Go to users page
    driverID.get("https://www.instagram.com/"+str(username))
    sleep(randomTimer())
    # Check if able to follow
    try:
        driverID.find_element_by_xpath("//*[text()='Unfollow']").click()
        print("Unfollowed: "+username)
    except NoSuchElementException:
        print("unable to find follow button")

# Like specific photo
def likeSpec(driverID, link):
	# Navigate bot to page with photo (only)
    driverID.get(link)
    sleep(randomTimer())
    driverID.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()












    
