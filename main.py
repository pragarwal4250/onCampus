from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import json

mainWeb = "https://webapp4.asu.edu/myasu/student/finances"

dataFile = "data.json"
userName = None
password = None
resume = None
coverLetter = None

def setCredAndLogin(dataFile, driver, userName, password, resume, coverLetter):
    
    # Read the JSON data from the file
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)

    # Extract the username and password from the JSON data
    userName = data["username"]
    password = data["password"]
    resume = data["resume"]
    coverLetter = data["coverLetter"]

    element = driver.find_element(By.ID, "username")
    element.send_keys(userName)

    element = driver.find_element(By.ID, "password")
    element.send_keys(password)
    element.send_keys(Keys.ENTER)

def openWebPage(webPageName):
    
    # Initialize the WebDriver for your chosen browser
    driver = webdriver.Chrome()  # Use 'webdriver.Firefox()' for Firefox

    driver.maximize_window()

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

def startYourApplication(driver):

    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    results = wait.until(lambda driver: driver.find_element(By.ID, "startapply"))

    element = driver.find_element(By.ID, "startapply")
    element.click()

    return

def applicationInstructions(driver):

    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    results = wait.until(lambda driver: driver.find_element(By.ID, "shownext"))

    # Locate the checkbox element by its ID
    checkbox = driver.find_element(By.ID, "checkbox-87496-Agree")

    # Check the checkbox if it's not already checked
    if not checkbox.is_selected():
        checkbox.click()

    element = driver.find_element(By.ID, "shownext")
    element.click()

    return

def standardApplicationQuestions(driver):

    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    results = wait.until(lambda driver: driver.find_element(By.ID, "shownext"))

    time.sleep(1)

    # Are you currently eligible to work in the United States without ASU sponsorship?
    #
    #
    # Find the radio button element you want to select
    radio_button = driver.find_element(By.ID, "radio-44674-Yes")

    # Check if the radio button is selected; if not, click it to select it
    if not radio_button.is_selected():
        radio_button.click()
    
    # Are you an ASU student?
    #
    #
    # Find the radio button element you want to select
    radio_button = driver.find_element(By.ID, "radio-45523-Yes")

    # Check if the radio button is selected; if not, click it to select it
    if not radio_button.is_selected():
        radio_button.click()
    
    # Are you enrolled in classes at ASU?
    #
    #
    # Find the radio button element you want to select
    radio_button = driver.find_element(By.ID, "radio-45534-Yes")

    # Check if the radio button is selected; if not, click it to select it
    if not radio_button.is_selected():
        radio_button.click()

    # Are you eligible for FWS?
    #
    #
    # Find the radio button element you want to select
    radio_button = driver.find_element(By.ID, "radio-61829-No")

    # Check if the radio button is selected; if not, click it to select it
    if not radio_button.is_selected():
        radio_button.click()
    
    element = driver.find_element(By.ID, "shownext")
    element.click()

    results = wait.until(lambda driver: driver.find_element(By.ID, "custom_44925_1291_fname_slt_0_44925"))

    # Find the dropdown element by its HTML id, name, or other locators
    dropdown = Select(driver.find_element(By.ID, "custom_44925_1291_fname_slt_0_44925"))

    results = wait.until(lambda driver: driver.find_element(By.XPATH, "//option[@value='Website']"))

    element = driver.find_element(By.ID, "custom_44925_1291_fname_slt_0_44925-button")

    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()

    element.send_keys(Keys.ARROW_DOWN)
    element.send_keys(Keys.ARROW_DOWN)
    element.send_keys(Keys.ARROW_DOWN)
    element.send_keys(Keys.ENTER)

    # Wait for an element to be visible (replace with the actual element)
    results = wait.until(lambda driver: driver.find_element(By.ID, "shownext"))

    element = driver.find_element(By.ID, "shownext")
    element.click()    

    return

def contactInformation(driver, resume, coverLetter):

    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    results = wait.until(lambda driver: driver.find_element(By.ID, "importprofile"))

    # Resume
    element = driver.find_element(By.LINK_TEXT, "Add résumé/CV")
    element.click()

    # Switch to an iframe by ID, name, or index (replace with your specific iframe locator)
    iframe_element = driver.find_element(By.ID, "profileBuilder")
    driver.switch_to.frame(iframe_element)

    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    results = wait.until(lambda driver: driver.find_element(By.ID, "btnSelectedSavedRC"))

    element = driver.find_element(By.ID, "btnSelectedSavedRC")
    element.click()

    # Wait for an element to be visible (replace with the actual element)
    results = wait.until(lambda driver: driver.find_element(By.CLASS_NAME, "primaryButton"))

    # Find the radio button by its label text
    radio_button = driver.find_element(By.XPATH, f'//label[text()="{resume}"]')
    radio_button.click()

    element = driver.find_element(By.XPATH, "//button[@class='primaryButton']")
    element.click()

    driver.switch_to.default_content()
    
    
    # Cover Letter
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Add cover letter')]")))
    element.click()

    # Switch to an iframe by ID, name, or index (replace with your specific iframe locator)
    iframe_element = driver.find_element(By.ID, "profileBuilder")
    driver.switch_to.frame(iframe_element)

    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    results = wait.until(lambda driver: driver.find_element(By.ID, "btnSelectedSavedRC"))

    element = driver.find_element(By.ID, "btnSelectedSavedRC")
    element.click()

    # Wait for an element to be visible (replace with the actual element)
    results = wait.until(lambda driver: driver.find_element(By.CLASS_NAME, "primaryButton"))

    # Find the radio button by its label text
    radio_button = driver.find_element(By.XPATH, f'//label[text()="{coverLetter}"]')
    radio_button.click()

    # Check if the radio button is selected; if not, click it to select it
    if not radio_button.is_selected():
        radio_button.click()

    element = driver.find_element(By.XPATH, "//button[@class='primaryButton']")
    element.click()

    driver.switch_to.default_content()

    element = driver.find_element(By.ID, "shownext")
    element.click()

def attachments(driver):

    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    element = wait.until(EC.text_to_be_present_in_element((By.ID, "ApplyPageHead"), "Attachments"))

    element = driver.find_element(By.ID, "shownext")
    element.click()

    return

def references(driver):

    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    element = wait.until(EC.text_to_be_present_in_element((By.ID, "ApplyPageHead"), "References"))

    element = driver.find_element(By.ID, "shownext")
    element.click()

    return

def eeoFormGender(driver):

    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    element = wait.until(EC.text_to_be_present_in_element((By.ID, "ApplyPageHead"), "EEO Form - Gender and Hispanic/Latino"))

    element = driver.find_element(By.ID, "shownext")
    element.click()

    return

def eeoFormRace(driver):

    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    element = wait.until(EC.text_to_be_present_in_element((By.ID, "ApplyPageHead"), "EEO form - Race"))

    element = driver.find_element(By.ID, "shownext")
    element.click()

    return

def review(driver):

    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    element = wait.until(EC.text_to_be_present_in_element((By.ID, "ApplyPageHead"), "Review"))

    element = driver.find_element(By.ID, "save")
    element.click()

    return   

def applyJob(driver, resume, coverLetter):
    
    # Define an explicit wait with a timeout of 20 seconds
    wait = WebDriverWait(driver, 60)

    # Wait for an element to be visible (replace with the actual element)
    results = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, 'p.question.thick.ng-binding.ng-scope.jobdescriptionInJobDetails'))

    try:
        # Try to find the link by its text
        link_element = driver.find_element(By.LINK_TEXT, "Check your applications.")
        print(f"Already applied")
        return
    except:
        print(f"Applying")

        element = driver.find_element(By.ID, "applyFromDetailBtn")
        element.click()
        
        startYourApplication(driver)
        applicationInstructions(driver)
        standardApplicationQuestions(driver)
        contactInformation(driver, resume, coverLetter, resume, coverLetter)
        attachments(driver)
        references(driver)
        eeoFormGender(driver)
        eeoFormRace(driver)
        review(driver)

def processParsedLinks(driver, linksList, resume, coverLetter):

    for item in linksList:

        index, link, date = item

        # Simulate opening the link in a new tab using a keyboard shortcut (Ctrl+click)
        link.send_keys(Keys.CONTROL + Keys.RETURN)  # Opens the link in a new tab

        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[1])

        applyJob(driver, resume, coverLetter)

        # Close the new tab (if needed)
        driver.close()

        # Switch back to the original tab (if needed)
        driver.switch_to.window(driver.window_handles[0])

def closeWindow(driver):
    
    driver.quit()

if __name__ == "__main__":

    driver = openWebPage(mainWeb)

    setCredAndLogin(dataFile, driver, userName, password)

    waitLogin(driver)

    clickOnFindStudentJobsAndSearchOnCampusJobs(driver)

    selectCampusAndClick(driver)

    linksList = getAllJobLinksOnPage(driver) #[index, link, date]

    processParsedLinks(driver, linksList, resume, coverLetter)

    done = False

    while not done:
        done = 1 if input("Should I stop? [Y/N]") == "Y" else 0

    closeWindow(driver)