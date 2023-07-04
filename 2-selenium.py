# scraping dynamic value (changing)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

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
    driver.get("https://www.timeanddate.com/worldclock/azerbaijan/baku") # here goes the address of the website
    return driver

def clean_text(text):
    # this function extracts only temperature from text
    output = str(text.split(": ")) # after splitting, it returns the list that has a text and temperature, and [1] is to choose the temperature
    return output

def main():
    driver = get_driver()
    time.sleep(1) # due to temperature change, sleep(waiting) is required
    element = driver.find_element(by="xpath", value="/html/body/div[5]/main/article/section[1]/div[1]/div/span[1]") 
    return clean_text(element.text)

print(main())