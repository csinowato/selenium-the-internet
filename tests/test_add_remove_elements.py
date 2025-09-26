from selenium.webdriver.common.by import By


def test_add_remove_elements(driver, base_url):
    driver.get(f"{base_url}/add_remove_elements/")

    # initially there should be 0 added elements
    elements = driver.find_elements(By.CLASS_NAME, "added-manually")
    assert len(elements) == 0

    # add 2 elements
    add_element_button = driver.find_element(
        By.CSS_SELECTOR, "button[onclick='addElement()']"
    )
    add_element_button.click()
    add_element_button.click()

    # re-find elements
    elements = driver.find_elements(By.CLASS_NAME, "added-manually")
    assert len(elements) == 2

    # delete an element
    driver.find_element(By.CSS_SELECTOR, "button[onclick='deleteElement()']").click()

    # re-find elements
    elements = driver.find_elements(By.CLASS_NAME, "added-manually")
    assert len(elements) == 1
