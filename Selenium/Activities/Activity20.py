# Import webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# Set up the Firefox Driver with WebDriverManger
service = FirefoxService(GeckoDriverManager().install())

# Start the Driver
with webdriver.Firefox(service=service) as driver:
    # Navigate to the URL
    driver.get("https://training-support.net/selenium/javascript-alerts")
    # initialize the wait object
    wait = WebDriverWait(driver, 10)
    # Print the title of the page
    print("Page title is: ", driver.title)
    # Find the confirm button and click it
    driver.find_element(By.ID, "prompt").click()
    # Switch focus to the alert
    prompt_alert = driver.switch_to.alert
    # Print the text in the alert
    print(prompt_alert.text)
    # Type in the text box
    prompt_alert.send_keys("Awesome")
    # Close the alert with either one of the methods
    # with OK
    prompt_alert.accept()
    # with Cancel
    # confirm_alert.dismiss()
