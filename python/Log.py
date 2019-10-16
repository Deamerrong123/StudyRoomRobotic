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
        'q.rong','y.bai1',
    }
    URL = 'https://www.baruch.cuny.edu/library/reservaroom/'

    def __init__(self):

        ## PWD = "C:\Users\QIZHAOR\Desktop\PROGRAM\WebDevelop\StudyRoom\python\chromedriver.exe"
        self._browser = webdriver.Chrome('{}/chromedriver.exe'.format(os.getcwd()))
        self._browser.get(Loger.URL)
        self._wait = WebDriverWait(self._browser,2.5)

        self._usernameField = self._browser.find_element_by_id('usernamefield')
        sleep(.5)
        self._passwordField = self._browser.find_element_by_id('passwordfield')
        ##self._passwordField = self._browser.find_element_by_xpath('//*[@id="passwordfield"]')

        ## get the log_in button
        self._log_in_btn = self._browser.find_element_by_id('loginsubmitbutton')

    def EnterIn(self,username,password):
        if username not in Loger.username_dic:
            self.browserKiller()
            raise ValueError
        self._usernameField.send_keys(username)
        self._passwordField.send_keys(password)

        ## automatically enter the username and password

    def login(self):
        try:
            self._log_in_btn.click()
        except Exception as e:
            pass
        finally:
            #self.browserKiller()
            pass

    def browserKiller(self):
        self._browser.quit()


    def ReserseRoom(self,Type,room,timeS):
        para_1 = room + 2
        para_2 = (int(timeS.split(':')[0])-8+1)*2
        para_2 += 1 if (int(timeS.split(':')[1]) > 0) else 0

        
        Tomorrow = self._wait.until(
            ec.element_to_be_clickable((By.XPATH,'//*[@id="calendarModule"]/input[2]'))
            )
        Tomorrow.click()
        ##self._browser.find_element_by_xpath('//*[@id="calendarModule"]/input[2]').click()
        
        RoomType = self._wait.until(
            ec.element_to_be_clickable((By.XPATH,'//*[@id="grouptabs"]/tbody/tr/td[{}]/a'.format(str(Type+1))))
            )
        RoomType.click()
        ##self._browser.find_element_by_xpath('//*[@id="grouptabs"]/tbody/tr/td[3]/a').click()

        Room_str = '//*[@id="dayviewTable"]/tbody/tr[{1}]/td[{0}]/img'.format(str(para_1),str(para_2))
        _Room = self._wait.until(ec.element_to_be_clickable((By.XPATH,Room_str)))

        _Room.click()

        _PopWin = self._wait.until(
            ec.visibility_of_element_located((By.ID,'popup')))
##        self._browser.find_elements_by_link_text('Yes').click()
        self._browser.find_element(By.XPATH,'//*[@id="popup"]/form/center/a[1]').click()
                                                                              
                                                                              
def thread_run_func(_username,_password,Type,room,timeS,T_t_sleep):
    loger = Loger()
    sleep(T_t_sleep)
    loger.EnterIn(_username,_password)
    loger.login()
    loger.ReserseRoom(Type,room,timeS)
    


def Double_log(_username,_password,_Type,_room,sec1,sec2,timeToSleep):
    t1 = threading.Thread(target = thread_run_func,args =(_username,_password,_Type,_room,sec1,timeToSleep,))
    t2 = threading.Thread(target = thread_run_func,args =(_username,_password,_Type,_room,sec2,timeToSleep))
    t1.start()
    t2.start()
    
        

