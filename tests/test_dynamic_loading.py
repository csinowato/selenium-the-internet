from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# element on page that is hidden
def test_dynamic_loading1(driver, base_url):
    driver.get(f"{base_url}/dynamic_loading/1")

    # find element by ID of the parent <div id="start"> + tag <button>Start</button>
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    # wait a few seconds for element to be unhidden
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    text = driver.find_element(By.CSS_SELECTOR, "#finish h4").text
    assert text == "Hello World!"


def test_dynamic_loading2(driver, base_url):
    driver.get(f"{base_url}/dynamic_loading/2")

    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    text = driver.find_element(By.CSS_SELECTOR, "#finish h4").text
    assert text == "Hello World!"
