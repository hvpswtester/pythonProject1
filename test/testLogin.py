import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()
# driver.get("https://staging-social.eclipton.com/login")
# print(driver.title)
# # driver.find_element("xpath", "//h2[text()='Login']")
# driver.quit()
# time.sleep(5)

@pytest.fixture()
def test_SetUp():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://staging-social.eclipton.com/login")
    print(driver.title)
    yield
    time.sleep(2)
    driver.quit()


def test_Login1(test_SetUp):
    print("Verify Login Page Detail")
    loingHeader = driver.find_element("xpath", "//h2[text()='Login']")
    assert loingHeader.is_displayed()
    emailTxt = driver.find_element("name", "email")
    assert emailTxt.is_displayed()
    passwordTxt = driver.find_element("name", "password")
    assert passwordTxt.is_displayed()
    emaiLabel = driver.find_element("xpath", "//label[text()='Email']")
    assert emaiLabel.is_displayed()
    passwordLabel = driver.find_element("xpath", "//label[text()='Password']")
    assert passwordLabel.is_displayed()
    print(driver.title)
    page_title = driver.title
    assert page_title == "Eclipton", page_title
    print("All Assertion Passed")


def test_Login2(test_SetUp):
    print("Verify validation for blank email")
    emailTxt = driver.find_element("name", "email")
    print(emailTxt.get_attribute("validationMessage"))
    passwordTxt = driver.find_element("name", "password")
    passwordTxt.send_keys("TestPassword")
    loginBtn = driver.find_element("xpath", "//button[text()='Login']")
    loginBtn.click()
    emailTxtValidationMessgae = "Please fill out this field."
    assert emailTxtValidationMessgae == emailTxt.get_attribute("validationMessage"), ("Validation message ",emailTxt.get_attribute("validationMessage"))


def test_Login3(test_SetUp):
    print("Verify validation for blank password")
    emailTxt = driver.find_element("name", "email")
    emailTxt.send_keys("test@gmail.com")
    passwordTxt = driver.find_element("name", "password")
    loginBtn = driver.find_element("xpath", "//button[text()='Login']")
    loginBtn.click()
    print(passwordTxt.get_attribute("validationMessage"))
    passwordTxtValidationMessgae = "Please fill out this field."
    assert passwordTxtValidationMessgae == passwordTxt.get_attribute("validationMessage"), passwordTxt.get_attribute("validationMessage")


def test_Login4(test_SetUp):
    print("Verify validation for blank email and password")
    emailTxt = driver.find_element("name", "email")
    passwordTxt = driver.find_element("name", "password")
    loginBtn = driver.find_element("xpath", "//button[text()='Login']")
    loginBtn.click()
    print(emailTxt.get_attribute("validationMessage"))
    emailTxtValidationMessgae = "Please fill out this field."
    assert emailTxtValidationMessgae == emailTxtValidationMessgae, emailTxt.get_attribute("validationMessage")
    print(passwordTxt.get_attribute("validationMessage"))
    passwordTxtValidationMessgae = "Please fill out this field."
    assert passwordTxtValidationMessgae == passwordTxt.get_attribute("validationMessage"), passwordTxt.get_attribute("validationMessage")


def test_Login5(test_SetUp):
    print("Verify validation for invalid email format")
    print("Verify validation for blank email")
    emailTxt = driver.find_element("name", "email")
    emailTxt.send_keys("test")
    passwordTxt = driver.find_element("name", "password")
    passwordTxt.send_keys("TestPassword")
    loginBtn = driver.find_element("xpath", "//button[text()='Login']")
    loginBtn.click()
    print(emailTxt.get_attribute("validationMessage"))
    emailTxtValidationMessgae = "Please include an '@' in the email address. 'test' is missing an '@'."
    assert emailTxtValidationMessgae == emailTxt.get_attribute("validationMessage"), emailTxt.get_attribute("validationMessage")
