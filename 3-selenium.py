# automated logging in

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service('/Users/nurlanmammadli/Downloads/chromedriver')

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars") # disable infobars(pop-ups), if available in website
    options.add_argument("start-maximized") # size of the screen can change, this blocks it
    options.add_argument("disable-dev-shm-usage") #to avoid linux problems
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://glob.az/")
    return driver

def main():
    driver = get_driver()
    # Wait for the element to be clickable
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/button")))
    # Click the button
    button.click()

    driver.find_element(by="xpath", value="/html/body/header/div[1]/div[1]/div/div/div[2]/a[1]").click()
    time.sleep(1)
    driver.find_element(by="id", value="loginform-email").send_keys("mmmdlinurlan40@gmail.com")
    time.sleep(1)
    driver.find_element(by="id", value="loginform-password").send_keys("nurik2020" + Keys.RETURN)
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/main/div/div/div/div[1]/div[1]/div[2]/p")
    print(element.text)
    print("current address - " + driver.current_url)

main()