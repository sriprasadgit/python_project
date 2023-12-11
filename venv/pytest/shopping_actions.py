# shopping_actions.py
from selenium.webdriver.common.by import By
from common_functions import click_element, right_click, wait_for_clickable, assert_equal, wait_for_element_and_perform, verify_element_present

# Generic function to add an item to the cart
def add_to_cart(driver):
    item_name = (By.XPATH, "//div[contains(@class,'inventory_item_name') and text () = 'Sauce Labs Backpack']")
    add_to_cart_button = (By.XPATH, "//div[@class = 'pricebar']/button[@data-test='add-to-cart-sauce-labs-backpack']")
    click_element(driver, *add_to_cart_button)

# Generic function to verify item added to the cart
def verify_item_added_to_cart(driver):
    cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")
    cart_count_locator =  "//a[@class='shopping_cart_link']/span"
    # Wait for the cart count element to be visible
    cart_count = wait_for_element_and_perform(driver, By.XPATH, cart_count_locator, lambda element: element.text.strip())
     # Get the text content of the cart count element
    #cart_count = cart_count_element.text.strip()
    assert_equal(cart_count, '1', "Assertion failed: Item count in the cart is not equal to the expected count")
    click_element(driver, *cart_icon)

    cart_item_verify = "//div[@class='cart_list']//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']"
    assert verify_element_present(driver, By.XPATH, cart_item_verify)


# Generic function to perform a logout
def logout(driver):
    menu_btn = (By.ID, "react-burger-menu-btn")
    logout_button = (By.ID, "logout_sidebar_link")
    click_element(driver, *menu_btn)
    wait_for_clickable(driver, By.ID, "logout_sidebar_link").click()
    #click_element(driver, *logout_button)

# Generic function to log in
def login(driver, username, password):
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")

    driver.find_element(*username_field).send_keys(username)
    driver.find_element(*password_field).send_keys(password)

    login_button = (By.ID, "login-button")
    driver.find_element(*login_button).click()
