from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()
userName=driver.find_element(By.NAME,value="username")
print("display status is: ",userName.is_displayed())
print("enable status is: ", userName.is_enabled())
if userName.is_displayed() and userName.is_enabled():
    userName.send_keys("Admin")

driver.find_element(By.XPATH,value='//p[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]').click()
driver.find_element(By.NAME,value="username").send_keys("Admin")
driver.find_element(By.XPATH,value='//button[@class="oxd-button oxd-button--large oxd-button--secondary orangehrm-forgot-password-button orangehrm-forgot-password-button--reset"]').click()

driver.quit()