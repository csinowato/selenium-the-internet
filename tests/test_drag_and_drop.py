from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def test_drag_and_drop(driver, base_url):
    driver.get(f"{base_url}/drag_and_drop")

    colA = driver.find_element(By.ID, "column-a")
    colB = driver.find_element(By.ID, "column-b")
    assert colA.text == "A" and colB.text == "B"

    action = ActionChains(driver)
    action.drag_and_drop(colA, colB).perform()
    assert colA.text == "B" and colB.text == "A"
