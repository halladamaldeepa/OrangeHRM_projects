from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()
driver.find_element(By.NAME, value="username").send_keys("Admin")
driver.find_element(By.NAME, value="password").send_keys("admin123")
driver.find_element(By.XPATH, value='//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]').click()
driver.find_element(By.XPATH, value='//a[@href="/web/index.php/pim/viewPimModule"]').click()
driver.find_element(By.XPATH, value='//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]').click()

driver.find_element(By.NAME, value="firstName").send_keys("Deepa")
driver.find_element(By.NAME, value="middleName").send_keys("Rahul")
driver.find_element(By.NAME, value="lastName").send_keys("Mali")

driver.find_element(By.XPATH, value="//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").send_keys("108227")
#driver.find_element(By.CSS_SELECTOR, value="button[type='submit']").click()

mywait=WebDriverWait(driver,10)
save=mywait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))
save.click()