import yaml
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    site = testdata["site"]
    site_login = testdata["site_login"]


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = site

    def find_element(self, locator, times=10):
        return WebDriverWait(self.driver, times).until(EC.presence_of_element_located(locator),
                                                       message="Элемент не найден")

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_alert_text(self):
        alert = self.driver.switch_to.alert.text
        return alert
