# Import webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Firefox Driver with WebDriverManger
service = FirefoxService(GeckoDriverManager().install())

# Start the Driver
with webdriver.Firefox(service=service) as driver:
    # Navigate to the URL
    driver.get("https://www.training-support.net/selenium/dynamic-attributes")
    # initialize the wait object
    wait = WebDriverWait(driver, 10)
    # Print the title of the page
    print("Page title is: ", driver.title)
    # Find the username field
    username = driver.find_element(By.XPATH, "//input[contains(@class, '-username')]")
    # Find the password field
    password = driver.find_element(By.XPATH, "//input[contains(@class, '-password')]")
    # Find the confirm password field
    confirm_password = driver.find_element(
        By.XPATH, "//label[contains(text(), 'Confirm Password')]//following::input"
    )
    # Alternatively, following-sibling can also be used
    # confirm_password = driver.find_element_by_xpath("//label[text()='Confirm Password')]/following-sibling::input")
    # Find the email field
    email = driver.find_element(By.XPATH, "//input[contains(@class, 'email-')]")

    # Enter the credentials
    username.send_keys("NewUser")
    password.send_keys("Password")
    confirm_password.send_keys("Password")
    email.send_keys("kopalpython@email.com")
    # Find the Sign Up button and click it
    driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()

    # Wait for the login message to appear
    wait.until(EC.visibility_of_element_located((By.ID, "action-confirmation")))
    # Print the success message
    message = driver.find_element(By.ID, "action-confirmation").text
    print("Success message: ", message)
    # Close the browser
    driver.quit()
