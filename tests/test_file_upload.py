from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

filepath = "/Users/claudia/Desktop/test_upload.rtf"


def test_file_upload(driver, base_url):
    driver.get(f"{base_url}/upload")

    # Selenium can't interact with native OS dialog so set filepath directly
    # target the <input type="file"> element i.e. <input id="file-upload" type="file">
    driver.find_element(By.ID, "file-upload").send_keys(filepath)

    driver.find_element(By.ID, "file-submit").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "uploaded-files"))
    )

    # check that UI displays the name of the uploaded file after submitting
    text = driver.find_element(By.ID, "uploaded-files").text
    assert text == "test_upload.rtf"
