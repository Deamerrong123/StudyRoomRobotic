from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

        ## automatically enter the username and passward
        self._browser.find_element_by_id('usernamefield').send_keys(self._username)
        self._browser.find_element_by_id('passwordfield').send_keys(self._password)

        ## get the log_in button
        self._log_in_btn = self._browser.find_element_by_id('loginsubmitbutton')

    def log(self):
        if (self._username in Loger.username_dic):
            self._log_in_btn.click()
        else:
            raise ValueError
    def logged(self):
        try:
            pass

        except:
            pass

    def ReserseRoom(self):
        self._browser.find_element_by_xpath('//*[@id="calendarModule"]/input[2]').click()
        self._browser.find_element_by_xpath('//*[@id="grouptabs"]/tbody/tr/td[3]/a').click()
        ## //*[@id="dayviewTable"]/tbody/tr[19]/td[6]/img
        self._browser.find_element_by_xpath('//*[@id="dayviewTable"]/tbody/tr[19]/td[6]/img').click()
        self.popup = self._browser.find_element_by_id('popup')
        # if popup.is_displayed():
        #     self._browser.find_element_by_link_text('Yes').click()



# if __name__ == '__main__':
#     URL = 'https://www.baruch.cuny.edu/library/reservaroom/'
#     loger = Loger(URL,'','')



