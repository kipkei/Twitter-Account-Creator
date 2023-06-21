import time
import sys
import random
import selenium.webdriver.chrome.service as service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print("Number of names: ")
ammount = input()

# Email address generator

print("Working...")

service = service.Service('chromedriver/chromedriver')
service.start()
capabilities = {'chrome.binary': ''}  # Enter path to chrome.exe in windows inside the '' tags.

driver = webdriver.Remote(service.service_url, capabilities)
driver.get('https://www.random.org/strings/')

time.sleep(1)

# Enter the amount of emails into random.org to generate that amount of strings
stringNumber = driver.find_element_by_name("num")
stringNumber.clear()
stringNumber.send_keys(ammount)

# Enter the length of the strings
stringLength = driver.find_element_by_name("len")
stringLength.clear()
stringLength.send_keys(15)

# Allow uppercase letters
uppercase = driver.find_element_by_name("upperalpha")
uppercase.click()

# Allow lowercase letters
lowercase = driver.find_element_by_name("loweralpha")
lowercase.click()

# Get strings
lowercase.submit()

# All the strings are stored inside var x, then stored inside an array called emails

x = driver.find_element_by_class_name("data").text

# Now the variable x is stored inside a file for the email generating program to use.

with open("names.txt", "w") as file:
    file.write(x)

# Close opened file
file.close()

print("Successfully created emails.txt\nPlease open up \"EmailAccountGenerator.py\" and enter the same amount of emails as you did here")
driver.close()
