from time import sleep

#library import 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

from firebase import firebase

# Configure
#############################
firebaseRef = ''
numberOfNames = 0
#############################

#Setting Firebase URL
firebase = firebase.FirebaseApplication(firebaseRef, None)

def storeInFirebase(name):
	post = firebase.post('/firstNames', {'firstName' : name})
	return post



def start():
        chrome_options = webdriver.ChromeOptions()
	driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get('https://www.randomlists.com/random-first-names')
        sleep(1)
        
	generate = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[1]/div[1]/div/button[1]')
	generate.click()
	sleep(2)

	#Get Name
	i = 1
	collection = []
	for i in range(1, 13):
		element = "/html/body/div/div[1]/div[2]/div[1]/div[2]/ol/li["+str(i)+"]/span"
		name = driver.find_element_by_xpath(element).text
		print(str(i)+") "+name)
		collection.append(name)
	print(collection)
	print("Packing Collection")
	x = 1

	print('Preparing to Store to Database.')
	for i in range(0, 11):
		storeInFirebase(collection[i])
		print('Storing....')
	print('Stored')
	driver.close()
	sleep(1)
	
#Number of times code executed (Names in sets of 12)
n = 0
for n in range(0, numberOfNames):
	print(n+1)	
	start()
