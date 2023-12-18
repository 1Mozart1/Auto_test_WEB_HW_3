import time
import logging
from testpage import OperationHelper

username = "Neo1"
password = "9aedda8a1f"


def test_step_1(browser):
    logging.info("Testing step 1")
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login(username)
    test_page1.enter_pswd(password)
    test_page1.click_button()
    time.sleep(3)

    test_page1.click_contact()
    time.sleep(3)

    test_page1.enter_cont_name(username)
    test_page1.enter_cont_email("test@test.ru")
    test_page1.enter_cont_text("test")
    time.sleep(2)

    test_page1.click_button()
    time.sleep(2)

    assert test_page1.get_alert_text() == "Form successfully submitted"
