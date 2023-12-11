# common_functions.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Generic function to launch the browser and open the URL
def launch_browser(url, driver_type="chrome"):
    if driver_type.lower() == "chrome":
        from selenium import webdriver
        driver = webdriver.Chrome()
    elif driver_type.lower() == "firefox":
        from selenium.webdriver.firefox.options import Options
        driver = webdriver.Firefox(options=Options())
    else:
        raise ValueError(f"Unsupported driver type: {driver_type}")

    driver.get(url)
    return driver

# Generic function to verify the presence of an element on the page
def verify_element_present(driver, by, value):
    try:
        element = driver.find_element(by, value)
        assert element.is_displayed()
        return True
    except:
        return False

# Generic function to click an element
def click_element(driver, by, value):
    element = driver.find_element(by, value)
    element.click()

# Generic function to perform a right-click on an element
def right_click(driver, by, value):
    element = driver.find_element(by, value)
    action_chains = ActionChains(driver)
    action_chains.context_click(element).perform()

# Generic function to perform a left-click on an element
def left_click(driver, by, value):
    element = driver.find_element(by, value)
    action_chains = ActionChains(driver)
    action_chains.click(element).perform()

# Generic function to wait for an element to be clickable
def wait_for_clickable(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, value))
    )

# Generic function to wait for an element to be clickable and perform an action
def wait_for_element_and_perform(driver, by, value, action, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, value))
    )
    return action(element)


def assert_equal(actual, expected, message="Assertion failed: Values are not equal"):
    assert actual == expected, message
