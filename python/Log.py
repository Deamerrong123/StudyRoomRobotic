from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import os

class Loger:
    username_dic = {
        'q.rong','y.bai1'
    }

    def __init__(self,URL,username,password):
        self.URL = URL
        self._username = username
        self._password = password

        ## PWD = "C:\Users\QIZHAOR\Desktop\PROGRAM\WebDevelop\StudyRoom\python\chromedriver.exe"
        self._browser = webdriver.Chrome('{}/chromedriver.exe'.format(os.getcwd()))
        self._browser.get(URL)
        self._wait = WebDriverWait(self._browser,2)


        ## automatically enter the username and passward
        self._browser.find_element_by_id('usernamefield').send_keys(self._username)
        self._browser.find_element_by_id('passwordfield').send_keys(self._password)

        ## get the log_in button
        self._log_in_btn = self._browser.find_element_by_id('loginsubmitbutton')

    def log(self):
        if (self._username in Loger.username_dic):
            self._log_in_btn.click()
            # self._wait.until(ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Logout')))
            return True
        else:
            raise ValueError

    def browserKiller(self):
        self._browser.quit()


    def ReserseRoom(self,room,timeS):
        para_1 = int(room.split()[1])+1
        para_2 = (int(timeS.split(':')[0])-8+1)*2
        para_2 += 1 if (int(timeS.split(':')[1]) > 0) else 0

        self._browser.find_element_by_xpath('//*[@id="calendarModule"]/input[2]').click()
        sleep(.100)
        self._browser.find_element_by_xpath('//*[@id="grouptabs"]/tbody/tr/td[3]/a').click()
        sleep(.100)

        self._Room = self._browser.find_element(By.XPATH,\
                                                '//*[@id="dayviewTable"]/tbody/tr[{1}]/td[{0}]/img'.\
                                                format(str(para_1),str(para_2))).click()









