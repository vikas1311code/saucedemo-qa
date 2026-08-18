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

def test_locked_out_user(driver):
    driver.get("https://www.saucedemo.com")

    # Step 1: locked_out_user se login karo (username field, password field, login button)
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Step 2: Error message wait + verify karo
    # Hint: element locator hai (By.CSS_SELECTOR, "h3[data-test='error']")
    # Hint: WebDriverWait(driver, 10).until(EC.presence_of_element_located(...))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))

    # Step 3: Assert karo error text mein "locked out" shabd hai
    # Hint: error_text = driver.find_element(...).text
    # Hint: assert "locked out" in error_text
    error_text = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "locked out" in error_text