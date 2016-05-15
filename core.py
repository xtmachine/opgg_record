#!/usr/bin/env python
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start virtual display
display = Display(visible=0, size=(800, 600))
display.start()

# Load op.gg profile and click record button
driver = webdriver.Firefox()
driver.get('http://www.op.gg/summoner/userName=3%EB%85%84%EB%A7%8C%EC%9D%98%ED%9C%B4%EC%8B%9D')

spec_button = driver.find_element_by_id('SpectateButton')
spec_button.click()
try:
    record_button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ExtraView"]/div/div/div[1]/div/div'))
    )
    record_button.click()
    print("Clicked record!")
finally:
    driver.quit()

# Stop virtual display
display.stop()
