# Instagram Bot Farm

## Intro
The objective of this project was to create a large number of Instagram accounts and control the bots in a mass to achieve goals such as follow each other, comment on photos, change names, post photos, and other tasks performed on Instagram. This project contains scripts I've made to create realistic bios and credentials, manage VPNs to avoid banning, download and scrape data off of Google images and other sites, and uploading projects to either Firebase or local text files. This project was nearly fully automated until Instagram updated their sign up procedure, making it significantly more complex to sign up hundreds of accounts at a time. This being said, although this project is a few years outdated, this project still contains Python files I worked on that may still be relevant and helpful. This project was a side hobby along with high school and not everything is to par. But after working on this for so long, some files best represent my Python skills and is worth sharing. If you have any questions or concerns about the project feel free to message or comment in the near future.
 
## Bot_Center.py

Designed to be run in the Python IDLE.

#### Description
bot_center.py was developed to create random credentials to then sign up a new account. After the sign up process is complete, you can save the temporary random sting of credentials to the old database to be referenced later. This script can also sign in previously made accounts with both random credentials or premade credentials. This script was initially made to test and slowly follow the process of automating account creation while also providing a providing a cleaner way to reference botcore.py functions.

#### Functions
**help()** → Present the list of functions you can call.
**getIP()** → Get current IP to check if VPN is working.
**randomTimer** → Create a random time between 1 and 3 seconds to simulate pause time.
**record(ref)** → Record the current username, name, and email to either an old or new profile databank, depending on "ref" string parsing ("old" or "new").
**retrieve(ref, lineNumber)** → Retrieve data from either the old or new databank depending on the "ref" string passed starting from line "lineNumber".
**createCredentials()** → Creates strings for name, username, and email with domain made up of random letters.
**main()** → Automates by creating a new Selenium driver, retrieves credentials from databank to then sign in, then performs a task such as liking a specific photo via URL.

#### How to Setup and Run
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

## Botcore.py

Designed to be run in the Python IDLE and referenced by bot_center.py

#### Description
botcore.py was developed to manage Selenium webdrivers and control the bot accounts. Using the script, you're able to create multiple webdrivers and add each to a list to be referenced as a group or individually. You can then either sign in or sign up, then check whether the credentials worked. After signing in, you can direct the bot to do a number of things such as follow/unfollow a user, change credentials and profile image, and like specific photos via link. Lastly, you can use the script to close specific drivers and sign out of accounts when finished.

#### Functions
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

#### How to Setup and Run
Open the botcore.py script and fill in the following variables:
	**pw** *(String)* → The text/string used to sign in/up each bot.
	**profilePicLocation** *(String)* → The file location of the profile image to be set to.
	**chromeDriver** *(String)* → The file location (including the driver) of the Chrome driver used by Selenium.

1) Run the Python file in the console.
2) Create a new webdriver by running "createWebdriver()".
3) If signing up, use "signUp(driverID, email, fullName, username), otherwise use signIn(driverID, username)."
4) Check if sign in/sign up is successful by running "checkIfSignedUp(driverID)". If failed, check credentials or wait for Instagram time-out to pass.
5) Control the bot(s) by following, unfollowing, liking, or changing account details.
6) When done with one bot, close with "closeWebdriver(driverNumber)". If you're done with all, use [CTRL+Q] to quit, the script will automatically close all drivers.

#### Note:
The argument *driverID* is parsed by referencing bot in array. ex: checkIfSignedUp(driver[2])
This script uses Selenium webdriver, meaning the computer will be in use when running and the program is not considered "Headless".


------------- 

## CreateBotNetwork.py

Designed to be run in the Python IDLE.

#### Description
createBotNetwork.py was developed as my first attempt in making a botcore.py manager. This is outdated and not completely functional. Although this script is not used as much when trying to achieve the task at hand, this script manages VPNs, checks and manages account validity, utilized Google's Firebase as a database, and attempts to control multiple accounts in one go. This script was later abandoned because the methods used were not efficient enough. Firstly, the script references Firebase to collect hundreds of credentials at a time which causes problems for both lag and because Firebase has a bandwidth cap when not using the premium version. Secondly, the code was very clunky as I did not plan this through the first time making it difficult to add and remove features. The method to grab elements is also outdated, as grabbing elements by their HTMLor CSS tag is not as consistent as using either element name or XPath. And lastly, the script never caught exceptions or errors and were hard to implement because of its methods used to compete tasks, therefore creating a lot of problems when running. I posted this script anyway as a reference to manage and check VPNs, input emojis, save accounts that work, and incase I choose to use Firebase again.

#### Functions
**getUsernames()** -> Fetches all usernames from firebase and adds each element to an array.
**getProfileData()** -> Fetches all profile credentials (Bio, DisplayName, First Name, Last Name) from firebase and adds each element to their own array.
**logIn(username)** -> Directs webdriver to login page, then log's in using the *username* string parsed and global password *pw*.
**checkLogIn()** -> Check if user has logged in.
**goToProfile()** -> Directs webdriver to the "Edit Profile" page and changed each element to new credentials depending on a pre-designed loop utilizing *loopInt*.
**followPeople()** -> Follows a bot previously created and added to *peopleToFollow* array.
**logOut()** -> Logs bot out of account.
**close()** -> Effectivly closes bot being used.
**closeVPN()** -> Incomplete function to close vpn using OpenVPN.
**openVPN()** -> Incomplete function to open vpn usin OpenVPN.
**loop()** -> Follows a routine of starting vpn, logging bot into account, follow a few accounts set in array *peopleToFollow*, logs bot out of account, then closes webdriver and vpn.
**done()** -> Prints the results fetched from Firebase, proving no errors were found.
**start()** -> Recommended start making the script work.

#### How to Setup and Run
Open the createBotNetwork.py script and fill in the following variables: 
	**firebaseRef** *(String)* -> Firebase address used to store and reference credentials.
	**profilePassword** *(String)* -> Global password used for all profiles.
	**profileImagePath** *(String)* -> Path to file on computer to the image to be posted.
	**numberOfLoops** *(Int)* -> Number of times the **start()** script runs.
1) Run the file in a Python console.
2) Running "start()" will run the program as expected, otherwise fetch data first by running "getUsernames()" followed by "getProfileData()".
3) Log in to account by running "logIn(username)" and parsing the username you wish to use.
4) After logging into account, you can proceed to follow other accounts ("followPeople()"), edit the account ("goToProfile()"), and log out ("logOut()").


------------- 

## FirstName.py

#### Description
firstName.py is a script used to scrape first names from https://www.randomlists.com/random-first-names in big quantities, then save them as strings and store them in Firebase.

#### Functions
**storeInFirebase(name)** -> Sends the parsing *name* to firebase as a value of "firstName".
**start()** -> The main function of the script that fetches all the names on one page and adds them to an array (in sets of 12)

#### How to Setup and Run
Open the firstName.py and fill in the following variables:
	**firebaseRef** *(String)* -> Firebase address used to store and reference credentials.
	**numberOfNames** *(int)* -> Number of sets of names you want to gather (1 set has 12 names).

1) Set up the variables and make sure you're connected to wifi.
2) Run the script, which should open up a webdriver with Selenium and start gathering names.
3) After the loop has finished, everything should close properly with names saved to firebase.

###### Note:
This script uses Selenium webdriver, meaning the computer will be in use when running and the program is not considered "Headless".


------------- 

## LastName.py

#### Description
lastName.py is a script used to scrape first names from https://www.randomlists.com/last-names in big quantities, then save them as strings and store them in Firebase.

#### Functions
**storeInFirebase(name)** -> Sends the parsing *name* to firebase as a value of "lastName".
**start()** -> The main function of the script that fetches all the names on one page and adds them to an array (in sets of 12)

#### How to Setup and Run
Open the lastName.py and fill in the following variables:
	**firebaseRef** *(String)* -> Firebase address used to store and reference credentials.
	**numberOfNames** *(int)* -> Number of sets of names you want to gather (1 set has 12 names).

1) Set up the variables and make sure you're connected to Wi-Fi.
2) Run the script, which should open up a webdriver with Selenium and start gathering names.
3) After the loop has finished, everything should close properly with names saved to firebase.

###### Note:
This script uses Selenium webdriver, meaning the computer will be in use when running and the program is not considered "Headless".


------------- 

## PhotoDownloader.py

#### Description
photoDownloader.py was designed to download many images off a google image seach at a time. In this project, this was used for finding profile images as well as photos for the bots to post to seem active.

#### How to Setup and Run
Open the photoDownloader.py script and fill in the following variables:
	**collection[]** *(String)* -> This is the word used to search for the images on google images. Fill the array with different key words to get multiple image results.
	**limit** *(Int)* -> This is the number of photos to download off of google images per keyword (Limit: 99)
1) Set up the variables and make sure you're connected to Wi-Fi.
2) Run the script in a Python compiler.
3) After the loop has finished, the photos should be downloaded locally in separate files.


------------- 

## ProfileGenerator.py

#### Description
profileGenerator.py was developed to create a massive amount of very individual public credentials for each account made. Using data taken using *firstName.py* and *lastName.py*, we can create unique bios as well as fake social media usernames and many Instagram usernames to ensure availability and uniqueness. This script takes the names scraped into a **data.json** file and adds a number of characteristics such as hobbies, professions, and other media outlets to create a realistic bio text for many different accounts quickly and efficiently. When the bios and usernames are complete, the script then sends all the data directly to firebase while staying neat and organized.

#### Functions
**createBio()** -> Creates random bio elements such as hobbies and professions.
**formatBio()** -> Combines the bio into a random order with different punctuation dividers such as "Hobby | School".
**storeinFirebase(FirstName, LastName, Username1 -> Username13, Bio, DisplayName)** -> Uploads the final profile information to Firebase.

#### How to Setup and Run
open the profileGenerator.py Script and fill in the following variables:
	**firebaseRef** *(String)* -> Firebase address used to store and reference credentials.
	**password** *(String)* -> Password used for all accounts.
	**collectionD[]** *(String)* -> Array of dates for bios
	**collectionG[]** *(String)* -> Array of graduation dates
	**collectionU[]** *(String)* -> Array of Schools
 1) Download the names created from *firstName.py* and *lastName.py* as a .json file.
 2) Rename the file to data.txt and put the file in the same location as profileGenerator.py
 3) Set up the variables and make sure you're connected to Wi-Fi.
 4) Run the script in a Python compiler.
 5) After the loop has finished, the Firebase referenced should be filled with different bios as string elements.


------------- 

## VPNHandler.py

#### Description
vpnHandler.py was created to easily handle and change the VPN when running into errors with Instagram regarding creating too many accounts or changing accounts too quickly. This script utilized OpenVPN and NordVPN to change from one VPN to another on a Linux machine. This eventually stopped when I created *createBotNetwork.py* to take this scripts place.

#### Functions
**openVPN()** -> Starts the random VPN.
**closeVPN()** -> Closes the random VPN.
**checkVPN()** -> Compares initial IP to current IP.
**closing()** -> Registered exit function when script closes.

#### How to Setup and Run
1) Make sure you have OpenVPN installed.
2) Run the script while parsing "openVPN" to start.
3) When done, run the script again while parsing "closeVPN" to close.

--------------


If you have any questions or concerns feel free to message me about this project!
