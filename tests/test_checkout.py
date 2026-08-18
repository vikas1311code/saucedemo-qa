import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_to_cart_and_checkout(driver):
    driver.get("https://www.saucedemo.com")

    # Login (jaisa pehle kiya tha)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

    # Step 1: Backpack add to cart karo
    # Hint: is product ka add-to-cart button ka ID hai "add-to-cart-sauce-labs-backpack"
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Step 2: Cart icon pe click karo (class: "shopping_cart_link")
    # Hint: driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Step 3: Verify cart page pe product dikh raha hai
    # Hint: WebDriverWait + check karo By.CLASS_NAME "inventory_item_name" ka text "Sauce Labs Backpack" hai
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert cart_item == "Sauce Labs Backpack"

    # Step 4: Checkout button click karo (ID: "checkout")
    driver.find_element(By.ID, "checkout").click()

    # Step 5: First Name, Last Name, Postal Code bharo aur Continue click karo
    # IDs: "first-name", "last-name", "postal-code", button ID "continue"
    driver.find_element(By.ID, "first-name").send_keys("Vikas")
    driver.find_element(By.ID, "last-name").send_keys("Pandey")
    driver.find_element(By.ID, "postal-code").send_keys("800001")
    driver.find_element(By.ID, "continue").click()

    # Step 6: Finish button click karo (ID: "finish")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "finish")))
    driver.find_element(By.ID, "finish").click()

    # Step 7: Assert karo — order complete hone ka message dikh raha hai
    # Hint: class "complete-header" ka text "Thank you for your order!" hona chahiye
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
    message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert message == "Thank you for your order!"
