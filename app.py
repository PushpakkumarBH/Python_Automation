from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()


driver.get("https://www.google.com/")
wait = WebDriverWait(driver, 10)

ele=driver.find_element(By.ID,"APjFqb")

ele.send_keys("Bangalore")
driver.quit()