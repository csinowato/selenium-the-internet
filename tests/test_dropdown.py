from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_dropdown(driver, base_url):
    driver.get(f"{base_url}/dropdown")
    text = driver.find_element(By.ID, "dropdown").text
    assert "Please select an option" in text

    option1 = driver.find_element(By.CSS_SELECTOR, "option[value='1']")
    option1.click()
    assert option1.is_selected()

    option2 = driver.find_element(By.CSS_SELECTOR, "option[value='2']")
    option2.click()
    assert option2.is_selected()


def test_dropdown_with_select(driver, base_url):
    driver.get(f"{base_url}/dropdown")

    # use Selenium's Select helper
    dropdown = Select(driver.find_element(By.ID, "dropdown"))

    # select by value
    dropdown.select_by_value("1")

    # first_selected_option shows the currently selected option in the <select> element
    selected_option = dropdown.first_selected_option.text
    assert selected_option == "Option 1"

    dropdown.select_by_value("2")
    next_selected_option = dropdown.first_selected_option.text
    assert next_selected_option == "Option 2"
