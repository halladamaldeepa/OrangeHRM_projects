from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()
driver.find_element(By.NAME, value="username").send_keys("Admin")
driver.find_element(By.NAME, value="password").send_keys("admin123")
driver.find_element(By.XPATH, value='//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]').click()
driver.find_element(By.XPATH, value='//a[@href="/web/index.php/pim/viewPimModule"]').click()

driver.find_element(By.XPATH, '//div[text()="deepa "]/following::div[11]/descendant::i[@class="oxd-icon bi-trash"]').click() # for delete

driver.find_element(By.XPATH,value='//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]').click() #for yes delete


