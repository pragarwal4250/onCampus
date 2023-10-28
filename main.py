from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

mainWeb = "https://webapp4.asu.edu/myasu/student/finances"

def openWebPage(webPageName):

    # Initialize the WebDriver for your chosen browser
    driver = webdriver.Chrome()  # Use 'webdriver.Firefox()' for Firefox

    # Navigate to a website
    driver.get(webPageName)

    return driver

def waitLogin(driver):

    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    results = wait.until(lambda driver: driver.find_element(By.CLASS_NAME, 'signout'))

    print("Logged In")

def clickOnFindStudentJobs(driver):

    element = driver.find_element(By.LINK_TEXT, "Find student jobs")
    element.click()

    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    results = wait.until(lambda driver: driver.find_element(By.LINK_TEXT, 'Search On-Campus Jobs'))

def closeWindow(driver):
    
    driver.quit()

if __name__ == "__main__":

    driver = openWebPage(mainWeb)

    waitLogin(driver)

    clickOnFindStudentJobs(driver)

    done = False

    while not done:
        done = 1 if input("Should I stop? [Y/N]") == "Y" else 0

    closeWindow(driver)