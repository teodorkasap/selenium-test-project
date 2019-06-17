import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

 
 
def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver
 
 
def lookup(driver, query):
    driver.get("http://www.google.com")
    try:
        box = driver.find_element_by_name('q')
        box.send_keys(query)
        box.send_keys(Keys.RETURN)
    except TimeoutException:
        print("Box or Button not found in google.com")
 
 
if __name__ == "__main__":
    driver = init_driver()
    lookup(driver, "Selenium")
    time.sleep(5)
    driver.quit()