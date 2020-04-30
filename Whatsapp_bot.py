from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time

browser = webdriver.Chrome(executable_path = '/mnt/c/ProgramData/chocolatey/bin/chromedriver.exe')  # Optional argument, if not specified will search path.
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser,600)        #wait for sipulated time given to open browser


target = '"ME"'        #name of target
string = "HELLO WORLD"          #message to be sent
x_args = '//span[contains(@title, ' + target + ' )]'       #find the target
target = wait.until(ec.presence_of_element_located((By.XPATH, x_args)))   #wait until target is found
target.click()             #clicks the target


input_box = browser.find_element_by_class_name('_1Plpp')
for i in range(5) :
    input_box.send_keys(string + Keys.ENTER)
