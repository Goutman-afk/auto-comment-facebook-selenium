from time import sleep, time
from selenium import webdriver
PATH = r"C:\Users\Long\Python\msedgedriver.exe"

options = webdriver.EdgeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
driver = webdriver.Chrome(PATH, options=options)

driver.get("http://facebook.com")
driver.find_element_by_xpath(
    "//input[@class= 'inputtext _55r1 _6luy']").send_keys("huynhlong020709@gmail.com ")
driver.find_element_by_xpath(
    "//input[@class= 'inputtext _55r1 _6luy _9npi']").send_keys("abc123456")
link = driver.find_element_by_xpath(
    "//button[@class= '_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']").click()
sleep(2)
driver.get(
    "https://m.facebook.com/groups/968221704087336/posts/979634599612713/")
sleep(2)
commentBox = driver.find_element_by_id("composerInput")
commentBox.send_keys("auto cmt by bot")
sleep(2)
sendButton = driver.find_elements_by_tag_name("button")[0]

sendButton.click()
sleep(2)
