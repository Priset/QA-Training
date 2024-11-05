from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ElementBuilder:
    def __init__(self, driver):
        self.driver = driver
        self.by = None
        self.value = None
        self.timeout = 20

    def set_by(self, by_type):
        self.by = by_type
        return self

    def set_value(self, value):
        self.value = value
        return self

    def set_timeout(self, timeout):
        self.timeout = timeout
        return self

    def from_xpath(self, xpath):
        self.by = By.XPATH
        self.value = xpath
        return self

    def from_id(self, element_id):
        self.by = By.ID
        self.value = element_id
        return self

    def build(self):
        if not self.by or not self.value:
            raise ValueError("El 'by' y 'value' deben ser definidos antes de construir el elemento.")
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((self.by, self.value))
        )

    def build_clickable(self):
        if not self.by or not self.value:
            raise ValueError("El 'by' y 'value' deben ser definidos antes de construir el elemento clicable.")
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((self.by, self.value))
        )
