from selenium.webdriver.common.by import By


def test_javascript_alert(driver, base_url):
    driver.get(f"{base_url}/javascript_alerts")
    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']").click()

    # switch to alert mode to validate the alert pop-up
    alert = driver.switch_to.alert
    assert "JS Alert" in alert.text

    # click ok
    alert.accept()

    text = driver.find_element(By.ID, "result").text
    assert "You successfully clicked an alert" in text


def test_javascript_confirm_accept(driver, base_url):
    driver.get(f"{base_url}/javascript_alerts")
    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']").click()

    alert = driver.switch_to.alert
    assert "JS Confirm" in alert.text

    alert.accept()

    text = driver.find_element(By.ID, "result").text
    assert "You clicked: Ok" in text


def test_javascript_confirm_cancel(driver, base_url):
    driver.get(f"{base_url}/javascript_alerts")
    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']").click()
    alert = driver.switch_to.alert
    assert "JS Confirm" in alert.text

    # click cancel
    alert.dismiss()

    text = driver.find_element(By.ID, "result").text
    assert "You clicked: Cancel" in text


def test_javascript_prompt(driver, base_url):
    driver.get(f"{base_url}/javascript_alerts")
    driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()

    alert = driver.switch_to.alert
    assert "JS prompt" in alert.text

    # enter text into the alert textbox
    alert.send_keys("hello")
    alert.accept()

    text = driver.find_element(By.ID, "result").text
    assert "You entered: hello" in text
