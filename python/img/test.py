from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
##from time import sleep
##import os

URL = 'https://www.baruch.cuny.edu/library/reservaroom/'

if __name__ == '__main__':
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        ##chrome_driver = os.getcwd()
        chrome_driver='C:\\Users\\QIZHAOR\\Desktop\\PROGRAM\\WebDevelop\\StudyRoom\\python\\chromedriver.exe'

        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)

        driver.get(URL)

        driver.get_screenshot_as_file('Fig.png')

        
