# -*- coding: utf-8 -*-
import os
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from firebase import firebase
import atexit

#def closing():
    #driver.close()

#atexit.register(closing)
driver = webdriver.Chrome()
print("Webdriver Created...")
def logIn():
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    if str(driver.title) != "Login • Instagram":
        goToProfile(1)
        return
    print("URL Sent")
    usernameField = driver.find_element_by_name("username")
    print("Username found")
    usernameField.clear()
    usernameField.send_keys("jack.warrr")
    passwordField = driver.find_element_by_name("password")
    passwordField.clear()
    passwordField.send_keys("*D@NKmatt3r*")
    passwordField.send_keys(Keys.ENTER)
def goToProfile(roundNumber):
    driver.get("https://www.instagram.com/accounts/edit/")
    print(driver.title)
    nameField = driver.find_element_by_name("pepName")
    nameField.clear()
    nameField.send_keys("")
    usernameField = driver.find_element_by_name("pepUsername")
    username.clear()
    username.send_keys("")
    bioField = driver.find_element_by_name("pepBio")
    bioField.clear()
    bioField.send_keys("")
    sleep(5)
logIn()
closing()

