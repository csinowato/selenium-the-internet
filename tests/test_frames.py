from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Frameset
├── frame-top
│   ├── frame-left
│   ├── frame-middle
│   └── frame-right
└── frame-bottom
"""


def test_nested_frames(driver, base_url):
    driver.get(f"{base_url}/nested_frames")

    # switch to top frame (at index 0)
    driver.switch_to.frame(0)

    # switch to nested top-left frame
    driver.switch_to.frame(
        driver.find_element(By.CSS_SELECTOR, "frame[name='frame-left']")
    )
    text = driver.find_element(By.TAG_NAME, "body").text
    assert text == "LEFT"

    # go back one level (to frame-top)
    driver.switch_to.parent_frame()

    # switch to nested top-middle frame
    driver.switch_to.frame(
        driver.find_element(By.CSS_SELECTOR, "frame[name='frame-middle']")
    )
    text = driver.find_element(By.TAG_NAME, "body").text
    assert text == "MIDDLE"

    # go back one level (to frame-top)
    driver.switch_to.parent_frame()

    # switch to nested top-right frame
    driver.switch_to.frame(
        driver.find_element(By.CSS_SELECTOR, "frame[name='frame-right']")
    )
    text = driver.find_element(By.TAG_NAME, "body").text
    assert text == "RIGHT"

    # go back to main page
    driver.switch_to.default_content()

    # switch to bottom frame (at index 1)
    driver.switch_to.frame(1)
    text = driver.find_element(By.TAG_NAME, "body").text
    assert text == "BOTTOM"


def test_iframe(driver, base_url):
    driver.get(f"{base_url}/iframe")

    # switch to iframe using iframe id
    driver.switch_to.frame(driver.find_element(By.ID, "mce_0_ifr"))
    text = driver.find_element(By.CSS_SELECTOR, "#tinymce p").text
    assert "Your content goes here." in text

    # go back to main page
    driver.switch_to.default_content()
    header = driver.find_element(By.TAG_NAME, "h3").text
    assert "TinyMCE WYSIWYG Editor" in header
