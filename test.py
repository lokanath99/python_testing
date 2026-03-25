from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os, time

if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

def take_screenshots(driver, name):
    path = f"screenshots/{name}.png"
    driver.save_screenshot(path)

driver = webdriver.Chrome()

try:
    driver.get('http://127.0.0.1:5000')
    driver.find_element(By.ID, "username").send_keys('admin')
    driver.find_element(By.ID, "password").send_keys('1234')

    take_screenshots(driver, "before_login")
    driver.find_element(By.ID, "login-btn").click()
    take_screenshots(driver, "after_login")
    time.sleep(2)
    assert "login successful" in driver.page_source

    print("testing complete login success ")

except Exception as e:
    print("test failed,")
    take_screenshots(driver, "failed")
    print(e.message)
    raise e

finally: 
    driver.quit()