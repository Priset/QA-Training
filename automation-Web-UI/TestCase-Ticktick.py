from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import uuid
import time

from selenium.webdriver.common.by import By

# Random BigDecimal for IDs
def random_bigdecimal():
    return str(uuid.uuid4())

# Password val

password = "12345678"

# Open the browser
service = Service("C:\\workspace-python\\drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the URL
driver.get("https://ticktick.com/")

# Maximize the browser

driver.maximize_window()

# Create an account

sign_up = driver.find_element(By.XPATH, "//a[contains(@class, 'signupBtn_2APvt')]")
sign_up.click()
email_input = driver.find_element(By.XPATH, "//input[@autocomplete='username']")
email_input.send_keys(f"prueba_{random_bigdecimal()}@gmail.com")
password_input = driver.find_element(By.XPATH, "//input[@autocomplete='new-password']")
password_input.send_keys(password)
sign_up_button = driver.find_element(By.XPATH, "//button[contains(@class, 'button__3eXSs')]")
sign_up_button.click()
time.sleep(10)
skip_button = driver.find_element(By.XPATH, "//div[contains(@class, 'text-[16px] leading-[24px] text-grey-40 cursor-pointer')]")
skip_button.click()
time.sleep(7)
# Pause to keep the browser open


