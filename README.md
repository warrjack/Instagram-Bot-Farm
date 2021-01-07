# Instagram Bot Farm
 
### Bot_Center.py

Designed to be run in the Python IDLE.

##### Description
bot_center.py was developed to create random credentials to then sign up a new accound. After the sign up prcess is complete, you can save the temporary random sting of credentials to the old database to be referenced later. This script can also sign in previously made accounts with both random credentials or premade credentials. This script was initially made to test and slowly follow the process of automating account creation while also providing a providing a cleaner way to reference botcore.py functions.

##### Functions
**help()** → Present the list of functions you can call.
**getIP()** → Get current IP to check if VPN is working.
**randomTimer** → Create a random time between 1 and 3 seconds to simulate pause time.
**record(ref)** → Record the current username, name, and email to either an old or new profile databank, depending on "ref" string parsing ("old" or "new").
**retrieve(ref, lineNumber)** → Retrieve data from either the old or new databank depenin gon the "ref" string passed starting from line "lineNumber".
**createCredentials()** → Creates strings for name, username, and email with domain made up of random letters.
**main()** → Automates by creating a new Selenium driver, retrieves credentials from databak to then sign in, then performs a task such as liking a specific photo via URL.

##### How to Setup and Run
Open the bot_center.py script and fill in the following variables:
	**pw** *(String)* → The text/string used to be the password for all the accounts created
	**oldRecord** *(String)* -> The text/string used to locate a .txt file to reference newly made profile credentials (with random strings)
	**newRecord** *(String)* -> The text/string used to locate the .txt file to reference profile credentials that have been altered to replicate a realistic name/username

1) Run the file in a Python console.
2) Create a profile by running "createCredentials()".
3) Create a webdriver by running "botcore.createWebdriver()".
4) Sign up by running "botcore.signUp(driverID, email, fullName, username)".
5) Check if credentials worked programatically by running "checkIfSignedUp(driverID)" or checking the website itself.
6) If sign up was successful, record results by running reord(old), otherwise close the webdriver and repeat steps 2-6 to try signing up with different random credentials.

------------- 

### Botcore.py

Designed to be run in the Python IDLE and referenced by bot_center.py

##### Description
botcore.py was developed to manage Selenium webdrivers and control the bot accounts. Using the script, you're able to create multiple webdrivers and add each to a list to be referenced as a group or individually. You can then either sign in or sign up, then check whether the credentials worked. After signing in, you can direct the bot to do a number of things such as follow/unfollow a user, change credentials and profile image, and like specific photos via link. Lastly, you can use the script to close specific drivers and sign out of accounts when finished.

##### Functions
**help()** → Present the list of functions you can call.
**randomTimer()** → Create a random time between 1 and 3 seconds to simulate pause time.
**createWebdriver** → Create a new Selenium driver/browser.
**closeWebdriver(driverNumber)** → Closes a Selenium driver/browser by parsing a specific driver number.
**exitHandler()** → Closes all Selenium drivers before closing the script. Runs when quitting script.
**signIn(driverID, username)** → Uses a bot - selected using *driverID* - to sign an account in using the *username* parsed.
**signUp(driverID, email, fullName, username)** → Uses a bot - selected using *driverID* - to sign an account up using the credentials parsed.
**checkIfSignedUp(driverID)** → Check's if bot - selected using *driverID* - has signed in/up correctly.
**changeCredentials(driverID, currentUsername, name, username, bio)** → Directs a bot - selected using *driverID* - to the selected profile with *currentUsername* and selects "Edit profile". Then changes the name, username, and bio to the text parsed.
**follow(driverID, username)** → Directs a bot - selected using *driverID* - to the selected *username* link and follows the account.
**unfollow(driverID, username)** → Directs a bot - selected using *driverID* - to the selected *username* link and unfollows the account.
**likeSpec(driverID, link)** → Directs a bot - selected using *driverID* - to the link parsed to then "like" the photo posted.

##### How to Setup and Run
Open the botcore.py script and fill in the following variables:
	**pw** *(String)* → The text/string used to sign in/up each bot.
	**profilePicLocation** *(String)* → The file location of the profile image to be set to.
	**chromeDriver** *(String)* → The file location (including the driver) of the Chrome driver used by Selenium.

1) Run the Python file in the console.
2) Create a new webdriver by running "createWebdriver()".
3) If signing up, use "signUp(driverID, email, fullName, username), otherwise use signIn(driverID, username)."
4) Check if sign in/sign up is successful by running "checkIfSignedUp(driverID)". If failed, check credentials or wait for instagram time-out to pass.
5) Control the bot(s) by following, unfollowing, liking, or changing account details.
6) When done with one bot, close with "closeWebdriver(driverNumber)". If you're done with all, use [CTRL+Q] to quit, the script will automatically close all drivers.

###### Note:
The argument *driverID* is parsed by referencing bot in array. ex: checkIfSignedUp(driver[2])

This script uses Selenium Webdriver, meaning the computer will be in use when running and the program is not considered "Headless".
------------- 

### CreateBotNetwork.py

##### Description

##### Functions

##### How to Setup and Run

------------- 


### Botcore.py

##### Description

##### Functions

##### How to Setup and Run