import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def test_SetUp():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://staging-social.eclipton.com/login")
    print(driver.title)
    yield
    time.sleep(2)
    driver.quit()

def test_Login1(test_SetUp):

    print("Verify Login Page Detail")
    try:
        loginHeader = driver.find_element("xpath", "//h2[text()='Login']")
        assert loginHeader.is_displayed()
        emailTxt = driver.find_element("name", "email1")
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
    except:
        print("Element not found..")
    else:
        print("All Assertion Passed")


def test_Login2(test_SetUp):
    print("Verify validation for blank email")

    # emailTxt = wait.until(EC.element_to_be_selected(driver.find_element("name", "email")))
    emailTxt = driver.find_element("name", "email")
    # passwordTxt = wait.until(EC.element_to_be_selected(driver.find_element("name", "password")))
    passwordTxt = driver.find_element("name", "password")
    passwordTxt.send_keys("TestPassword")
    # time.sleep(50)
    wait = WebDriverWait(driver, 50)
    emailTxtValidationMessage = "Please fill not out this field."

    try:
        loginBtn = wait.until(EC.element_to_be_clickable(driver.find_element("xpath", "//button[text()='Login1']")))
        # loginBtn = driver.find_element("xpath", "//button[text()='Login']")
        loginBtn.click()
        assert emailTxtValidationMessage == emailTxt.get_attribute(
            "validationMessage"), "Validation Message does not match"
    except AssertionError as e:
        print(e)
    except:
        print("Element not found..")
    else:
        print("No Exception Found..")

    # emailTxtValidationMessage = "Please fill not out this field."

    # try:
    #     assert emailTxtValidationMessage == emailTxt.get_attribute("validationMessage"), "Validation Message does not match"
    # except AssertionError as e:
    #     print(e)
        # print("Assertion Error : Validation Message does not match in except..")

def test_Login3(test_SetUp):
    print("Verify validation for blank password")
    try:
        emailTxt = driver.find_element("name", "email")
        emailTxt.send_keys("test@gmail.com")
        passwordTxt = driver.find_element("name", "password")
        loginBtn = driver.find_element("xpath", "//button[text()='Login']")
        loginBtn.click()
        print(passwordTxt.get_attribute("validationMessage"))
        passwordTxtValidationMessage = "Please fill out this field."
        assert passwordTxtValidationMessage == passwordTxt.get_attribute("validationMessage"), "Validation Message does not match"
    except AssertionError as e:
        print(e)
    except:
        print("Element not found..")
    else:
        print("No Exception Found..")


def test_Login4(test_SetUp):
    print("Verify validation for blank email and password")

    emailTxt = driver.find_element("name", "email")
    passwordTxt = driver.find_element("name", "password")
    loginBtn = driver.find_element("xpath", "//button[text()='Login']")
    loginBtn.click()
    print(emailTxt.get_attribute("validationMessage"))
    emailTxtValidationMessage = "Please fill out this field."
    assert emailTxtValidationMessage == emailTxtValidationMessage, emailTxt.get_attribute("validationMessage")
    print(passwordTxt.get_attribute("validationMessage"))
    passwordTxtValidationMessage = "Please fill out this field."
    assert passwordTxtValidationMessage == passwordTxt.get_attribute("validationMessage"), passwordTxt.get_attribute("validationMessage")


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
    emailTxtValidationMessage = "Please include an '@' in the email address. 'test' is missing an '@'."
    assert emailTxtValidationMessage == emailTxt.get_attribute("validationMessage"), emailTxt.get_attribute("validationMessage")
