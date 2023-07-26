from selenium.webdriver.common.by import By


class CallbackLocators:
    BUTTON_ORDER_A_CALL = (By.CSS_SELECTOR, "a[class='callback header_link']")
    NAME = (By.CSS_SELECTOR, "div[class='form-fields-wrap form-generator'] input[name='UF_NAME']")
    PHONE = (By.CSS_SELECTOR, "div[class='form-fields-wrap form-generator'] input[name='UF_PHONE']")
    TIME = (By.CSS_SELECTOR, "div[class='form-fields-wrap form-generator'] input[name='UF_TIME']")
    DEPARTAMENT_WALLPAPER = (By.CSS_SELECTOR, "label[for='UF_CHECKBOX2']")
    DEPARTAMENT_PLATE = (By.CSS_SELECTOR, "label[for='UF_CHECKBOX1']")
    BUTTON_CALL_ME_BACK = (By.CSS_SELECTOR, "button[oma-data-bind='applied']")



