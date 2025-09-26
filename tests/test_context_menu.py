from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


# test right-click interactions
def test_context_menu(driver, base_url):
    driver.get(f"{base_url}/context_menu")

    # use ActionChains to test mouse actions and use .perform() to execute
    action = ActionChains(driver)
    action.context_click(driver.find_element(By.ID, "hot-spot")).perform()

    alert = driver.switch_to.alert
    assert alert.text == "You selected a context menu"
    alert.accept()

    # verify main page after closing alert
    header = driver.find_element(By.TAG_NAME, "h3").text
    assert header == "Context Menu"
