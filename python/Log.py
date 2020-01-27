from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from time import sleep,time
import os

class Loger:
    username_dic = {
        'q.rong','y.bai1','T.yang4','w.niu'
    }
    URL = 'https://www.baruch.cuny.edu/library/reservaroom/'

    def __init__(self):

        ## PWD = "C:\Users\QIZHAOR\Desktop\PROGRAM\WebDevelop\StudyRoom\python\chromedriver.exe"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_driver = os.getcwd()+'\\chromedriver.exe'

        self._browser = webdriver.Chrome('{}/chromedriver.exe'.format(os.getcwd()))
##        self._browser = webdriver.Chrome(options = chrome_options , executable_path=chrome_driver)
##        self._browser = webdriver.Chrome(executable_path=chrome_driver)
        
        self._wait = WebDriverWait(self._browser, 100)
        self._browser.get(Loger.URL)


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
        if room < 2:
            return
        para_1 = room + 2
        para_2 = (int(timeS.split(':')[0])-8+1)*2
        para_2 += 1 if (int(timeS.split(':')[1]) > 0) else 0

        
        Room_str = '//*[@id="dayviewTable"]/tbody/tr[{1}]/td[{0}]/img'.format(str(para_1),str(para_2))
        _Room = self._wait.until(ec.element_to_be_clickable((By.XPATH,Room_str)))

        _Room.click()

        _PopWin = self._wait.until(
            ec.visibility_of_element_located((By.ID,'popup')))
##        self._browser.find_elements_by_link_text('Yes').click()
        self._browser.get_screenshot_as_file("room{}From{}.png".format(str(para_1),str(para_2)))
        self._browser.find_element(By.XPATH,'//*[@id="popup"]/form/center/a[1]').click()
        

    def TwoHour(self,room,secOne,secTwo):
        try:
            self.ReserseRoom(room,secOne)
            self.ReserseRoom(room,secTwo)
        except:
            self.TwoHour(room-1,secOne,secTwo)
        finally:
            sleep(1.5)
            self._browser.get_screenshot_as_file("Result1.png")
            self._browser.quit()
            


def Double_log(_username,_password,_Type,_room,sec1,sec2,targetTime):
    loger = Loger()
    loger.EnterIn(_username,_password) ## First enter the username and passwors
    PostSleepTime(targetTime)    ## Sleep unit 00:00:00
    loger.login(_Type)       ## Login the page
    loger.TwoHour(_room,sec1,sec2) ## for resering the room

def PostSleepTime(targetTime):
    timeToSleep = targetTime - time()
    sleep(timeToSleep)

    
        

