class LoginSection:
    SIGN_IN_BUTTON = "//a[text()='Sign In']"
    EMAIL_INPUT = "//input[@autocomplete='username']"
    PASSWORD_INPUT = "//input[@autocomplete='current-password']"
    SIGN_UP_BUTTON = "//button[contains(@class, 'button__3eXSs')]"

class TaskSection:
    NEW_TASK_BUTTON = "//a[contains(@class, 'block relative w-[40px] h-[40px] relative px-[9px] py-[9px] active_3xqKF active special_2dY-B')]"
    HOVER_LIST = "//*[@id='project-list-scroller']/div[2]/section[1]/div[1]/li/a"
    NEW_LIST_BUTTON = "(//button[contains(@class, 'add-icon')])[1]"
    TASK_NAME_INPUT = "//input[@id='edit-project-name']"
    COLOR_PICKER = "//div[contains(@class, 'rounded-full') and contains(@class, 'cursor-pointer') and contains(@style, 'background-color: rgb(255, 172, 56)')]"
    ADD_TASK_BUTTON = "//div[contains(@class, 'footer_tjCqK')]//button[@type='button' and contains(@class, 'btn-primary') and text()='Add']"
    TASK_ITEM = "//p[contains(@class, 'text-s') and contains(@class, 'truncate') and text()='{}']"
    EDIT_BUTTON = "{}/following::div[contains(@class, 'peer') and contains(@class, 'absolute') and contains(@class, 'right-0') and contains(@class, 'top-1/2')]"
    EDIT_MENU_ITEM = "//li[@class='dropdown-menu-menu-item' and @data-menu-id='-projectEdit']"
    SAVE_BUTTON = "//button[@type='button' and contains(@class, 'btn-primary') and text()='Save']"
    DELETE_MENU_ITEM = "//li[@class='dropdown-menu-menu-item deleteItem' and @data-menu-id='-projectDelete']"
    DELETE_BUTTON = "//button[@type='button' and contains(@class, 'btn-primary') and text()='Delete']"
