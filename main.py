from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = 'F:\Coding\Python\Chrome_Selenium\chromedriver.exe'
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get('http://www.facebook.com')

usr = "Your email"
pwd = "Your password"
image_path = r"image path if any"
# message = f"You can either be brave enough to fail or a coward who is afraid of even trying!\n {image_path}"
attach_image = True
with open('mytext.txt', 'r') as content:
    text = content.read()
message = f"{text} \n {image_path}"

group_links = [
    # Your Facebook Groups links.
    'https://www.facebook.com/groups/1',
    'https://www.facebook.com/groups/2',
    'https://www.facebook.com/groups/...',
]

elem = driver.find_element(By.ID, "email")
elem.send_keys(usr)
# Enter user password
elem = driver.find_element(By.ID, "pass")
elem.send_keys(pwd)
# Login
elem.send_keys(Keys.RETURN)
time.sleep(10)

for g in group_links:
    time.sleep(5)

    driver.get(g)
    # print(g)
    # time.sleep(5)

    time.sleep(15)

    searchBtn = driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div')
    # Perform click-and-hold action on the element
    webdriver.ActionChains(driver).click(searchBtn).perform()

    postbox = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]")

    time.sleep(5)
    # .......... Message Area .........
    wrtmessage = driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]")
    webdriver.ActionChains(driver).send_keys(message).perform()

    time.sleep(10)
    # ...... Image Upload Button ........
    # upload = driver.find_element(By.XPATH,
    #                              "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[1]")
    # # upload.click()
    # # webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    # webdriver.ActionChains(driver).click(upload).perform()
    # webdriver.ActionChains(driver).send_keys(image_path).perform()

    # ........ Post Button .........
    post = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div")
    webdriver.ActionChains(driver).click(post).perform()

#
print(f"Script Posts to {len(group_links)} Successfully")