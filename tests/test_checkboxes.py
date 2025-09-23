from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_checkboxes(driver, base_url):
    driver.get(f"{base_url}/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    print(f"There are {len(checkboxes)} checkboxes")
    assert len(checkboxes) == 2  # sanity check

    # the first checkbox is unchecked by default
    assert not checkboxes[0].is_selected()
    checkboxes[0].click()
    assert checkboxes[0].is_selected()

    # the second checkbox is selected by default
    assert checkboxes[1].is_selected()
    checkboxes[1].click()
    assert not checkboxes[1].is_selected()
