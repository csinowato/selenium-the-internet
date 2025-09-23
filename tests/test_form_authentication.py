from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = "tomsmith"
password = "SuperSecretPassword!"


def test_valid_login(driver, base_url):
    driver.get(f"{base_url}/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait until the secure page loads before grabbing header
    WebDriverWait(driver, 10).until(EC.url_contains("/secure"))
    header = driver.find_element(By.TAG_NAME, "h2").text
    assert header == "Secure Area"

    # Also check the flash success message
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "flash")))
    text = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in text


def test_invalid_login(driver, base_url):
    driver.get(f"{base_url}/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait for the flash message
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "flash")))
    text = driver.find_element(By.ID, "flash").text
    assert "Your password is invalid!" in text


def test_empty_credentials(driver, base_url):
    driver.get(f"{base_url}/login")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "flash")))
    text = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in text
