from selenium.webdriver.common.by import By
import pytest


@pytest.mark.skip(reason="flaky due to session reuse")
# Note: for sorting tests, jQuery tablesorter toggles between ascending/descending with each click
# If the driver/browser session is reused across tests the previous sort state bleeds into the next run
# (this causes the table sorting test to be inconsistent)
def test_table_sorting(driver, base_url):
    driver.get(f"{base_url}/tables")

    # sort by last name (click header)
    # in CSS selectors, nth-child() is 1-indexed not 0-indexed
    driver.find_element(By.CSS_SELECTOR, "#table2 th:nth-child(1)").click()

    # extract all elements in the last-name column
    last_name_elements = driver.find_elements(By.CSS_SELECTOR, "#table2 td.last-name")

    # store last names in an array (ignore column header)
    last_names = [l.text for l in last_name_elements]
    print("Last names:", last_names)
    assert last_names == sorted(last_names)


def test_data_validation(driver, base_url):
    driver.get(f"{base_url}/tables")

    # validate email format
    email_elements = driver.find_elements(By.CSS_SELECTOR, "#table2 td.email")
    emails = [e.text for e in email_elements]
    print("Emails:", emails)
    assert all("@" in e for e in emails)

    # check that amount due is a number
    due_elements = driver.find_elements(By.CSS_SELECTOR, "#table2 td.dues")
    dues = [float(d.text.replace("$", "")) for d in due_elements]
    print("Due amounts:", dues)
    assert all(d >= 0 for d in dues)
