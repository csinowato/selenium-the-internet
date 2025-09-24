from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_control_remove_add(driver, base_url):
    driver.get(f"{base_url}/dynamic_controls")

    # checkbox is displayed by default
    checkbox = driver.find_element(By.ID, "checkbox")
    assert checkbox.is_displayed()

    # remove checkbox
    toggle_button = "button[onclick='swapCheckbox()']"
    driver.find_element(By.CSS_SELECTOR, toggle_button).click()

    # staleness_of is the opposite of presence_of_element_located
    WebDriverWait(driver, 10).until(EC.staleness_of(checkbox))
    message = driver.find_element(By.ID, "message").text
    assert message == "It's gone!"

    # add back the checkbox
    driver.find_element(By.CSS_SELECTOR, toggle_button).click()

    # wait for new checkbox element
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "checkbox")))
    new_message = driver.find_element(By.ID, "message").text
    assert new_message == "It's back!"


def test_dynamic_control_enable_disable(driver, base_url):
    driver.get(f"{base_url}/dynamic_controls")

    # field is disabled by default
    field = driver.find_element(By.CSS_SELECTOR, "#input-example input")
    assert not field.is_enabled()

    # enable field
    toggle_button = "button[onclick='swapInput()']"
    driver.find_element(By.CSS_SELECTOR, toggle_button).click()

    # wait for field to be enabled
    # note: can't use the previous field variable because that stores a WebElement reference
    # (so Selenium would just keep checking that same object and since it was captured when it was disabled, it never flips to 'clickable')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example input"))
    )

    message = driver.find_element(By.ID, "message").text
    assert message == "It's enabled!"

    # disable field again
    driver.find_element(By.CSS_SELECTOR, toggle_button).click()

    # selenium doesnt have built in element disabled check so use lambda function for the wait
    WebDriverWait(driver, 10).until(
        lambda d: not d.find_element(
            By.CSS_SELECTOR, "#input-example input"
        ).is_enabled()
    )

    new_message = driver.find_element(By.ID, "message").text
    assert new_message == "It's disabled!"
