from selenium.webdriver.common.by import By


def test_multiple_windows(driver, base_url):
    driver.get(f"{base_url}/windows")

    # store main window handle
    main = driver.current_window_handle

    # switch to new window
    driver.find_element(By.CSS_SELECTOR, ".example a").click()

    handles = driver.window_handles
    for h in handles:
        if h != main:
            driver.switch_to.window(h)
            break

    text = driver.find_element(By.TAG_NAME, "h3").text
    assert text == "New Window"
