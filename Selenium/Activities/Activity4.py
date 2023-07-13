# Import webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Set up the Firefox Driver with WebDriverManger
service = FirefoxService(GeckoDriverManager().install())

# Start the Driver
with webdriver.Firefox(service=service) as driver:
    # Open the browser to the URL
    driver.get("https://www.training-support.net/selenium/target-practice")

    #  Get the title of the page and print it to the console
    print("Home page title:" + driver.title)
    # Find the 3rd header element on the page using XPath
    third_heading = driver.find_element(By.XPATH, "//h3[@id='third-header']")
    print("Third heading text is: ", third_heading.text)

    # Find the 5th header element on the page using XPath
    fifth_heading = driver.find_element(By.XPATH, "//h5")
    print("Fifth heading colour is: ", fifth_heading.value_of_css_property("color"))

    # Find the violet button element on the page
    violet_button = driver.find_element(By.CLASS_NAME, "violet")
    print("Violet button's classes are: ", violet_button.get_attribute("class"))

    # Find the grey button element on the page
    grey_button = driver.find_element(By.CLASS_NAME, "grey")
    print("Text in grey button is: ", grey_button.text)
    # Close the browser
    driver.quit()
