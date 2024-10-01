from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


class DriverFactory:
    @staticmethod
    def get_driver(browser_name="chrome"):
        if browser_name.lower() == "chrome":
            service = ChromeService("C:\\workspace-python\\QA\\projectQA-Training\\automation-Web-UI\\drivers\\chromedriver.exe")
            driver = webdriver.Chrome(service=service)
        elif browser_name.lower() == "firefox":
            service = FirefoxService("C:\\workspace-python\\QA\\projectQA-Training\\automation-Web-UI\\drivers\\geckodriver.exe")
            driver = webdriver.Firefox(service=service)
        elif browser_name.lower() == "edge":
            service = EdgeService("C:\\workspace-python\\QA\\projectQA-Training\\automation-Web-UI\\drivers\\msedgedriver.exe")
            driver = webdriver.Edge(service=service)
        else:
            raise ValueError(f"Browser '{browser_name}' is not supported.")

        driver.maximize_window()
        return driver
