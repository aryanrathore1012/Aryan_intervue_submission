'''

Hello - I am Aryan Rathore This is my Assingment SUbmission
This is a demo on how the Code works
THank YOU!!!!
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.intervue.io/")
time.sleep(2)

# menu_items = [
#     "why intervue?",
#     "products", 
#     "solutions",
#     "resources",
#     "contact us"
# ]

# for item in menu_items:
#     element = driver.find_element(By.CSS_SELECTOR, f'[data-submenu-item="{item}"]')
#     ActionChains(driver).move_to_element(element).perform()
#     print(f"Hovered over: {item}")
#     time.sleep(1)


login_button = driver.find_element(By.CLASS_NAME, "loginBtn")
login_button.click()

print("Clicked Login button - you should now be on the login page")

time.sleep(5)  

new_window = driver.window_handles[-1]
driver.switch_to.window(new_window)


new_login=driver.find_element(By.CLASS_NAME, "AccessAccount-ColoredButton")
new_login.click()

print("Clicked both login buttons successfully")

try:

    email_field = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
    email_field.send_keys("neha@intervue.io") 
    time.sleep(1)
    

    password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    password_field.send_keys("Ps@neha@123")
    time.sleep(1)

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'], .ant-btn-primary")
    submit_button.click()
    print("Login form submitted successfully")
    
except Exception as e:
    print(f"Error during login: {e}")
    print(f"Current URL: {driver.current_url}")

time.sleep(5) 
driver.quit()