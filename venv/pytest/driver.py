# test_case_study.py
import pytest
from common_functions import launch_browser, verify_element_present, click_element, right_click, wait_for_clickable
from shopping_actions import add_to_cart, verify_item_added_to_cart, logout, login
from selenium.webdriver.common.by import By

# Test case using pytest
def test_case_study():
    # Step 1: Launch the URL
    url = "https://www.saucedemo.com/"
    driver = launch_browser(url)

    # Step 2: Verify SWAG LABS is present on the Web Page

    swag_labs_logo = "//div[@class ='login_logo' and text() = 'Swag Labs']"
    assert verify_element_present(driver, By.XPATH, swag_labs_logo)

    login(driver, "standard_user", "secret_sauce")
    # Step 3: Add any one of the item to cart
    add_to_cart(driver)

    # Step 4: Click on the right corner of the button and verify item is added to the cart
    verify_item_added_to_cart(driver)

    # Step 5: Click on the left corner of the button and click on LOGOUT button
    #right_click(driver, By.CLASS_NAME, "shopping_cart_link")
    logout(driver)

    # Close the browser
    driver.quit()

# Run the test
if __name__ == "__main__":
    pytest.main(["-v", __file__])
