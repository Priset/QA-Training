import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uuid

# Random BigDecimal for IDs
def random_bigdecimal():
    return str(uuid.uuid4())

# Credentials
password = "TestingQA753159"
email = "testingQA1478963@gmail.com"
nameTask = "Automation - " + random_bigdecimal()

# Open the browser
service = Service("C:\\workspace-python\\drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the URL
driver.get("https://ticktick.com/")

# Maximize the browser
driver.maximize_window()

# Create an account
wait = WebDriverWait(driver, 20)

sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign In']")))
sign_in.click()

email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']")))
email_input.send_keys(email)

password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='current-password']")))
password_input.send_keys(password)

sign_up_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'button__3eXSs')]")))
sign_up_button.click()

new_task = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'block relative w-[40px] h-[40px] relative px-[9px] py-[9px] active_3xqKF active special_2dY-B')]")))
new_task.click()

# Hover over the element
hover_lists = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='project-list-scroller']/div[2]/section[1]/div[1]/li/a")))

# Create an instance of ActionChains to perform the hover
actions = ActionChains(driver)
actions.move_to_element(hover_lists).perform()

new_list_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(@class, 'add-icon')])[1]")))
new_list_button.click()

task_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-project-name']")))
task_name_input.send_keys(nameTask)

color_picker = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'rounded-full') and contains(@class, 'cursor-pointer') and contains(@style, 'background-color: rgb(255, 172, 56)')]")))
color_picker.click()

add_task_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'footer_tjCqK')]//button[@type='button' and contains(@class, 'btn-primary') and text()='Add']")))
add_task_button.click()

# Validar que la tarea se creó exitosamente
task_created_xpath = f"//p[contains(@class, 'text-s') and contains(@class, 'truncate') and text()='{nameTask}']"

try:
    task_created = wait.until(EC.presence_of_element_located((By.XPATH, task_created_xpath)))
    print("Task created successfully.")
except:
    print("Task creation failed.")

# Crear una instancia de ActionChains para realizar el hover sobre la tarea
actions.move_to_element(task_created).perform()

# Esperar a que el botón de edición (icono svg) esté visible y clicable
edit_button_div_xpath = f"{task_created_xpath}/following::div[contains(@class, 'peer') and contains(@class, 'absolute') and contains(@class, 'right-0') and contains(@class, 'top-1/2')]"
edit_button_div = wait.until(EC.element_to_be_clickable((By.XPATH, edit_button_div_xpath)))

# Crear una instancia de ActionChains para realizar el clic después del hover
actions.move_to_element(edit_button_div).click().perform()

edit_menu_item = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='dropdown-menu-menu-item' and @data-menu-id='-projectEdit']")))
edit_menu_item.click()

edit_task_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='edit-project-name']")))

# Limpiar el nombre actual
edit_task_name_input.send_keys(Keys.CONTROL + "a")
edit_task_name_input.send_keys(Keys.BACKSPACE)

# Escribir el nuevo nombre de la tarea
edited_name_task = "Updated - " + random_bigdecimal()
edit_task_name_input.send_keys(edited_name_task)

save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and contains(@class, 'btn-primary') and text()='Save']")))
save_button.click()

# Validar que la tarea se editó exitosamente
edited_task_xpath = f"//p[contains(@class, 'text-s') and contains(@class, 'truncate') and text()='{edited_name_task}']"

try:
    task_edited = wait.until(EC.presence_of_element_located((By.XPATH, edited_task_xpath)))
    print("Task edited successfully.")
except:
    print("Task editing failed.")

actions.move_to_element(task_edited).perform()

delete_button_div_xpath = f"{edited_task_xpath}/following::div[contains(@class, 'peer') and contains(@class, 'absolute') and contains(@class, 'right-0') and contains(@class, 'top-1/2')]"
delete_button_div = wait.until(EC.element_to_be_clickable((By.XPATH, delete_button_div_xpath)))

actions.move_to_element(delete_button_div).click().perform()

delete_menu_item = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='dropdown-menu-menu-item deleteItem' and @data-menu-id='-projectDelete']")))
delete_menu_item.click()

accept_delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and contains(@class, 'btn-primary') and text()='Delete']")))
accept_delete_button.click()

# Validar que la tarea se eliminó exitosamente
try:
    wait.until(EC.invisibility_of_element_located((By.XPATH, edited_task_xpath)))
    print("Task deleted successfully.")
except:
    print("Task deletion failed.")

# Wait until the browser closes
time.sleep(3)
