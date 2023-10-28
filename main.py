from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

mainWeb = "https://webapp4.asu.edu/myasu/student/finances"

dataFile = "data.json"
userName = None
password = None

def setCredAndLogin(dataFile, driver, userName, password):
    
    # Read the JSON data from the file
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)

    # Extract the username and password from the JSON data
    userName = data["username"]
    password = data["password"]

    element = driver.find_element(By.ID, "username")
    element.send_keys(userName)

    element = driver.find_element(By.ID, "password")
    element.send_keys(password)
    element.send_keys(Keys.ENTER)

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

def clickOnFindStudentJobsAndSearchOnCampusJobs(driver):

    element = driver.find_element(By.LINK_TEXT, "Find student jobs")
    element.click()

    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    results = wait.until(lambda driver: driver.find_element(By.LINK_TEXT, 'Search On-Campus Jobs'))

    results.click()

    # Wait for an element to be visible (replace with the actual element)
    results = wait.until(lambda driver: driver.find_element(By.XPATH, '//*[@id="mainJobListContainer"]/div/div/div[1]/h2'))

    print("Job search welcome")

def selectCampusAndClick(driver):

    element = driver.find_element(By.NAME, "keyWordSearch")
    element.send_keys("campus:\ tempe")
    element.send_keys(Keys.ENTER)

    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    results = wait.until(lambda driver: driver.find_element(By.ID, 'sortByLabel'))

    print("Tempe jobs")

def getAllJobLinksOnPage(driver):

    # Find all list items with the specified class
    job_list_items = driver.find_elements(By.CSS_SELECTOR, "li.job.baseColorPalette.ng-scope")

    # Create a list to store the extracted data
    data_list = []

    # Loop through the list items and extract the link and date
    for index, job_item in enumerate(job_list_items):
        link_element = job_item.find_element(By.CSS_SELECTOR, "a.jobProperty.jobtitle")
        date_element = job_item.find_element(By.CSS_SELECTOR, "p.jobProperty.position1")

        date = date_element.text

        data_list.append([index, link_element, date])

    return data_list

def closeWindow(driver):
    
    driver.quit()

if __name__ == "__main__":

    driver = openWebPage(mainWeb)

    setCredAndLogin(dataFile, driver, userName, password)

    waitLogin(driver)

    clickOnFindStudentJobsAndSearchOnCampusJobs(driver)

    selectCampusAndClick(driver)

    linksList = getAllJobLinksOnPage(driver) #[index, link, date]

    done = False

    while not done:
        done = 1 if input("Should I stop? [Y/N]") == "Y" else 0

    closeWindow(driver)