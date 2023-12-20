from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()
driver.find_element(By.NAME, value="username").send_keys("Admin")
driver.find_element(By.NAME, value="password").send_keys("admin123")
driver.find_element(By.XPATH, value='//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]').click()

Actual_title="OrangeHRM"
Expected_title=driver.title
if Actual_title==Expected_title:
    print("Actual_title and Expected_title both are same")

driver.find_element(by=By.XPATH,value='//span[text()="Admin"]').click()
headers=driver.find_elements(by=By.XPATH,value='//div[@class="oxd-topbar-body"]//li//span[@class="oxd-topbar-body-nav-tab-item"]')
for i in headers:
    if i.is_displayed():
        print(i.text)
driver.quit(