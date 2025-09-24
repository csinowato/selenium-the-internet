from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

number_input_field = "input[type='number']"


def test_input(driver, base_url):
    driver.get(f"{base_url}/inputs")
    driver.find_element(By.CSS_SELECTOR, number_input_field).send_keys("5")

    # use the 'value' attribute instead of .text because input fields don't expose their contents as inner text
    number = driver.find_element(By.CSS_SELECTOR, number_input_field).get_attribute(
        "value"
    )
    assert number == "5"


def test_input_increment(driver, base_url):
    driver.get(f"{base_url}/inputs")
    driver.find_element(By.CSS_SELECTOR, number_input_field).send_keys("7")

    # check increment using ARROW_UP
    driver.find_element(By.CSS_SELECTOR, number_input_field).send_keys(Keys.ARROW_UP)

    num_increment = driver.find_element(
        By.CSS_SELECTOR, number_input_field
    ).get_attribute("value")
    assert num_increment == "8"


def test_input_decrement(driver, base_url):
    driver.get(f"{base_url}/inputs")
    driver.find_element(By.CSS_SELECTOR, number_input_field).send_keys("7")

    # check decrement using ARROW_DOWN
    driver.find_element(By.CSS_SELECTOR, number_input_field).send_keys(Keys.ARROW_DOWN)

    num_decrement = driver.find_element(
        By.CSS_SELECTOR, number_input_field
    ).get_attribute("value")
    assert num_decrement == "6"


def test_inputs_nonnumeric(driver, base_url):
    driver.get(f"{base_url}/inputs")
    driver.find_element(By.CSS_SELECTOR, number_input_field).send_keys("a")

    text = driver.find_element(By.CSS_SELECTOR, number_input_field).get_attribute(
        "value"
    )
    assert text == ""
