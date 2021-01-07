""" author: feezyhendrix

    main function borcore
 """
import time
from time import sleep
from random import randint

import modules.config as config
#importing generated info
import modules.generateaccountinformation as accnt
from modules.storeusernametofirebase import storeinfirebase 
#library import 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # and Krates
from selenium.common.exceptions import NoSuchElementException


def checkError(driverUsed):
    try:
        driverUsed.find_element_by_id('ssfErrorAlert')
    except NoSuchElementException:
        return False
    return True

def create_account():
    try:
        if config.Config['has_proxy_file'] == False :
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=%s' % config.Config['proxy_server'])

            #creating a chrome object instance to open browser
            driver = webdriver.Chrome(chrome_options=chrome_options)
            driver.get('https://www.instagram.com/')
            sleep(3)

            name = accnt.username()
            #username 
            

            #fill the email value
            email_field = driver.find_element_by_name('emailOrPhone')
            email_field.send_keys(accnt.genEmail())

            #fill the fullname value
            fullname_field = driver.find_element_by_name('fullName')
            fullname_field.send_keys(accnt.genName())

            #fill username value
            username_field = driver.find_element_by_name('username')
            username_field.send_keys(name)

            #fill password value
            password_field  = driver.find_element_by_name('password')
            passW = accnt.generatePassword() 
            password_field.send_keys(passW)

            submit = driver.find_element_by_xpath('/html/body/span/section/main/article/div[2]/div[1]/div/form/div[7]/div/button')
            submit.click()

            print('Registering....')

            sleep(2)
	    if checkError(driver) == True:
		print("Error0")
	    else:
		print("No Error0")
	    	storeinfirebase(name)
            sleep(1)
            driver.quit()
        
        else :
            with open(config.Config['proxy_file']['proxy_server_txt_file_path'], 'r') as file :
                content = file.read().splitlines()
                for proxy in content :
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_argument('--proxy-server=%s' % proxy)

                    #creating a chrome object instance to open browser
                    driver = webdriver.Chrome(chrome_options=chrome_options)

                    amount_per_proxy = config.Config['proxy_file']['profile_per_proxy']

                    if amount_per_proxy != 0 :
                        
                        print("Creating {} amount of users for this proxy".format(amount_per_proxy))

                        for i in range(0, amount_per_proxy) :
                            driver.get('https://www.instagram.com/')
                            sleep(3)
                            #username 
                            name = accnt.username()
                            
                            #fill the email value
                            email_field = driver.find_element_by_name('emailOrPhone')
                            email_field.send_keys(accnt.genEmail())

                            #fill the fullname value
                            fullname_field = driver.find_element_by_name('fullName')
                            fullname_field.send_keys(accnt.genName())

                            #fill username value
                            username_field = driver.find_element_by_name('username')
                            username_field.send_keys(name)

                            #fill password value
                            password_field  = driver.find_element_by_name('password')
                            passW = accnt.generatePassword() 
                            password_field.send_keys(passW)

                            submit = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/span/button')
                            submit.click()

                            print('Registering....')

                            sleep(2)
	                    if checkError(driver) == True:
	                	print("Error1")
	                    else:
	                	print("No Error1")
	    			storeinfirebase(name)
                            sleep(10)
                            driver.close()
                    
                    else :
                        random_number = randint(1, 20)
                        
                        print("Creating {} amount of users for this proxy".format(random_number))
                        for i in range(0, random_number):
                            driver.get('https://www.instagram.com/')
                            sleep(3)
                            #username 
                            name = accnt.username()
                            
                            #fill the email value
                            email_field = driver.find_element_by_name('emailOrPhone')
                            email_field.send_keys(accnt.genEmail())

                            #fill the fullname value
                            fullname_field = driver.find_element_by_name('fullName')
                            fullname_field.send_keys(accnt.genName())

                            #fill username value
                            username_field = driver.find_element_by_name('username')
                            username_field.send_keys(name)

                            #fill password value
                            password_field  = driver.find_element_by_name('password')
                            passW = accnt.generatePassword() 
                            password_field.send_keys(passW)

                            submit = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/span/button')
                            submit.click()

                            print('Registering....')
			    sleep(5)
	                    if checkError(driver) == True:
	                	print("Error2")
	                    else:
	                	print("No Error2")
	    			storeinfirebase(name)
                            sleep(10)
                            driver.close()

    except Exception as e:
        print(e)
        driver.close()

t0 = time.time()
print(t0)
for i in range(0, config.Config['amount_of_run']):
	print(i)
	create_account()
t1 = time.time()
print(t1)
print(t1-t0)

