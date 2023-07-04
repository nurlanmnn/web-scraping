# scraping simple text

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

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
    driver.get("https://passworddgenerator.netlify.app/")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/label")
    return element.text

print(main())