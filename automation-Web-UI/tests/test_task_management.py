import time
from selenium.webdriver import ActionChains, Keys
from config_variables import ConfigVariables
from driver_singleton import DriverSingleton
from element_builder import ElementBuilder
from page_elements import LoginSection, TaskSection

password = ConfigVariables.PASSWORD
email = ConfigVariables.EMAIL
nameTask = ConfigVariables.get_task_name()
edited_name_task = ConfigVariables.get_edited_task_name()
base_url = ConfigVariables.BASE_URL

driver = DriverSingleton.get_instance(browser_name="chrome")

# Crear una instancia del Builder para construir elementos
builder = ElementBuilder(driver)

# Abrir la URL
driver.get(base_url)

# Iniciar con una cuenta
sign_in = builder.from_xpath(LoginSection.SIGN_IN_BUTTON).build_clickable()
sign_in.click()

email_input = builder.from_xpath(LoginSection.EMAIL_INPUT).build()
email_input.send_keys(email)

password_input = builder.from_xpath(LoginSection.PASSWORD_INPUT).build()
password_input.send_keys(password)

sign_up_button = builder.from_xpath(LoginSection.SIGN_UP_BUTTON).build_clickable()
sign_up_button.click()

new_task = builder.from_xpath(TaskSection.NEW_TASK_BUTTON).build_clickable()
new_task.click()

hover_lists = builder.from_xpath(TaskSection.HOVER_LIST).build()

# Crear una instancia de ActionChains para realizar el hover
actions = ActionChains(driver)
actions.move_to_element(hover_lists).perform()

new_list_button = builder.from_xpath(TaskSection.NEW_LIST_BUTTON).build_clickable()
new_list_button.click()

task_name_input = builder.from_xpath(TaskSection.TASK_NAME_INPUT).build()
task_name_input.send_keys(nameTask)

color_picker = builder.from_xpath(TaskSection.COLOR_PICKER).build_clickable()
color_picker.click()

add_task_button = builder.from_xpath(TaskSection.ADD_TASK_BUTTON).build_clickable()
add_task_button.click()

# Validar que la tarea se creó exitosamente
task_created_xpath = TaskSection.TASK_ITEM.format(nameTask)

try:
    task_created = builder.from_xpath(task_created_xpath).build()
    print("Task created successfully.")
except:
    print("Task creation failed.")

# Crear una instancia de ActionChains para realizar el hover sobre la tarea
actions.move_to_element(task_created).perform()

# Esperar a que el botón de edición esté visible y clicable
edit_button_div_xpath = TaskSection.EDIT_BUTTON.format(task_created_xpath)
edit_button_div = builder.from_xpath(edit_button_div_xpath).build_clickable()

# Crear una instancia de ActionChains para realizar el clic después del hover
actions.move_to_element(edit_button_div).click().perform()

edit_menu_item = builder.from_xpath(TaskSection.EDIT_MENU_ITEM).build_clickable()
edit_menu_item.click()

edit_task_name_input = builder.from_xpath(TaskSection.TASK_NAME_INPUT).build()

# Limpiar el nombre actual
edit_task_name_input.send_keys(Keys.CONTROL + "a")
edit_task_name_input.send_keys(Keys.BACKSPACE)

# Escribir el nuevo nombre de la tarea
edit_task_name_input.send_keys(edited_name_task)

save_button = builder.from_xpath(TaskSection.SAVE_BUTTON).build_clickable()
save_button.click()

# Validar que la tarea se editó exitosamente
edited_task_xpath = TaskSection.TASK_ITEM.format(edited_name_task)

try:
    task_edited = builder.from_xpath(edited_task_xpath).build()
    print("Task edited successfully.")
except:
    print("Task editing failed.")

actions.move_to_element(task_edited).perform()

delete_button_div_xpath = TaskSection.EDIT_BUTTON.format(edited_task_xpath)
delete_button_div = builder.from_xpath(delete_button_div_xpath).build_clickable()

actions.move_to_element(delete_button_div).click().perform()

delete_menu_item = builder.from_xpath(TaskSection.DELETE_MENU_ITEM).build_clickable()
delete_menu_item.click()

accept_delete_button = builder.from_xpath(TaskSection.DELETE_BUTTON).build_clickable()
accept_delete_button.click()

# Validar que la tarea se eliminó exitosamente
try:
    builder.from_xpath(edited_task_xpath).build()
    print("Task deletion failed.")
except:
    print("Task deleted successfully.")

time.sleep(3)
