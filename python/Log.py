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
        'q.rong','y.bai1','T.yang4'
    }
    URL = 'https://www.baruch.cuny.edu/library/reservaroom/'

    def __init__(self):

        ## PWD = "C:\Users\QIZHAOR\Desktop\PROGRAM\WebDevelop\StudyRoom\python\chromedriver.exe"
        self._browser = webdriver.Chrome('{}/chromedriver.exe'.format(os.getcwd()))
        self._browser.get(Loger.URL)
        self._wait = WebDriverWait(self._browser,30)

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

    def login(self,Type):
        try:
            self._log_in_btn.click()
            sleep(0.5)
            self.toTomorRoom(Type)
        except Exception as e:
            pass
        finally:
            #self.browserKiller()
            pass

    def browserKiller(self):
        self._browser.quit()

    def toTomorRoom(self,Type):
        Tomorrow = self._wait.until(
        ec.element_to_be_clickable((By.XPATH,'//*[@id="calendarModule"]/input[2]'))
        )
        ## just see how today work?! COMMAN LINE BELOW.
        Tomorrow.click()
        ##self._browser.find_element_by_xpath('//*[@id="calendarModule"]/input[2]').click()
        
        RoomType = self._wait.until(
            ec.element_to_be_clickable((By.XPATH,'//*[@id="grouptabs"]/tbody/tr/td[{0}]/a'.format(str(Type+1))))
            )
        ##self._browser.find_element_by_xpath('//*[@id="grouptabs"]/tbody/tr/td[3]/a').click()
        ## //*[@id="grouptabs"]/tbody/tr/td[3]/a
        RoomType.click()
        


    def ReserseRoom(self,room,timeS):
        para_1 = room + 2
        para_2 = (int(timeS.split(':')[0])-8+1)*2
        para_2 += 1 if (int(timeS.split(':')[1]) > 0) else 0

        
        Room_str = '//*[@id="dayviewTable"]/tbody/tr[{1}]/td[{0}]/img'.format(str(para_1),str(para_2))
        _Room = self._wait.until(ec.element_to_be_clickable((By.XPATH,Room_str)))

        _Room.click()

        _PopWin = self._wait.until(
            ec.visibility_of_element_located((By.ID,'popup')))
##        self._browser.find_elements_by_link_text('Yes').click()
        self._browser.find_element(By.XPATH,'//*[@id="popup"]/form/center/a[1]').click()

    def TwoHour(self,room,secOne,secTwo):
        self.ReserseRoom(room,secOne)
        self.ReserseRoom(room,secTwo)
        
                                                                              
def thread_run_func(_username,_password,Type,room,timeS,T_t_sleep):
    pass

    


def Double_log(_username,_password,_Type,_room,sec1,sec2,timeToSleep):
    loger = Loger()
    loger.EnterIn(_username,_password) ## First enter the username and passwors
    sleep(timeToSleep)    ## Sleep unit 00:00:00
    loger.login(_Type)       ## Login the page
    loger.TwoHour(_room,sec1,sec2) ## for resering the room
    
    
        

