from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create webdriver object
driver = webdriver.Firefox()

# Get makemytrip.com
driver.get("https://www.makemytrip.com/")
wait = WebDriverWait(driver, 10)
from1 = wait.until(EC.presence_of_element_located((By.ID, "fromCity")))
to1 = wait.until(EC.presence_of_element_located((By.ID, "toCity")))

# Send keys
from1.send_keys("Bangalore")
to1.send_keys("Delhi")