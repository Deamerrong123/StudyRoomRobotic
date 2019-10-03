from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

import threading
import os

class Loger:
    username_dic = {
        'q.rong','y.bai1'
    }
    URL = 'https://www.baruch.cuny.edu/library/reservaroom/'

    def __init__(self):

        ## PWD = "C:\Users\QIZHAOR\Desktop\PROGRAM\WebDevelop\StudyRoom\python\chromedriver.exe"
        self._browser = webdriver.Chrome('{}/chromedriver.exe'.format(os.getcwd()))
        self._browser.get(Loger.URL)
        self._wait = WebDriverWait(self._browser,2.5)

        self._usernameField = self._browser.find_element_by_id('usernamefield')
        self._passwordField = self._browser.find_element_by_id('passwordfield')

        ## get the log_in button
        self._log_in_btn = self._browser.find_element_by_id('loginsubmitbutton')

    def EnterIn(self,username,password):
        self._usernameField.send_keys(username)
        self._passwordField.find_element_by_id('passwordfield').send_keys(password)
        if username not in username_dic:
            self.browserKiller()
            raise ValueError
        ## automatically enter the username and password

    def login(self):
        try:
            self._log_in_btn.click()
        except Exception as e:
            pass
        finally:
            self.browserKiller()

    def browserKiller(self):
        self._browser.quit()


    def ReserseRoom(self,room,timeS):
        para_1 = int(room.split()[1])+1
        para_2 = (int(timeS.split(':')[0])-8+1)*2
        para_2 += 1 if (int(timeS.split(':')[1]) > 0) else 0

        
        Tomorrow = self._wait.until(
            ec.element_to_be_clickable(By.XPATH,'//*[@id="calendarModule"]/input[2]')
            )
        Tomorrow.click()
        ##self._browser.find_element_by_xpath('//*[@id="calendarModule"]/input[2]').click()
        
        TechRoom = self._wait.until(
            ec.element_to_be_clickable(By.XPATH,'//*[@id="grouptabs"]/tbody/tr/td[3]/a')
            )
        TechRoom.click()
        ##self._browser.find_element_by_xpath('//*[@id="grouptabs"]/tbody/tr/td[3]/a').click()

        Room_str = '//*[@id="dayviewTable"]/tbody/tr[{1}]/td[{0}]/img'.format(str(para_1),str(para_2))
        _Room = self._wait.until(ec.element_to_be_clickable(By.XPATH,Room_str))

        _Room.click()

        _PopWin = self._wait.until(
            ec.visibility_of_element_located(By.ID,'popup'))
        self._browser.find_elements_by_link_text('Yes').click()
                                                                              
                                                                              



def thread_run_func(_username,_password,room,timeS):
    loger = Loger()
    try:
        loger.EnterIn(_username,_password)
        loger.login()
        loger.ReserseRoom(room,timeS)
    except Exception as e:
        pass
    finally:
        loger.browserKiller()

def Double_log(URL,_username,_password):
    t1 = threading.Thread(target = thread_run_func,args =(_username,_password,))
    t2 = threading.Thread(target = thread_run_func,args =(URL,_username,_password,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
        

