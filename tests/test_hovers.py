from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_hovers(driver, base_url):
    driver.get(f"{base_url}/hovers")

    # use ActionChains to test mouse actions and use .perform() to execute
    action = ActionChains(driver)

    # store all elements in an array
    figures = driver.find_elements(By.CLASS_NAME, "figure")

    # hover over the first figure
    action.move_to_element(figures[0]).perform()
    user1_text = figures[0].find_element(By.CSS_SELECTOR, ".figcaption h5").text
    assert user1_text == "name: user1"

    # hover over the second figure
    action.move_to_element(figures[1]).perform()
    user2_text = figures[1].find_element(By.CSS_SELECTOR, ".figcaption h5").text
    assert user2_text == "name: user2"

    # hover over the third figure
    action.move_to_element(figures[2]).perform()
    user3_text = figures[2].find_element(By.CSS_SELECTOR, ".figcaption h5").text
    assert user3_text == "name: user3"
