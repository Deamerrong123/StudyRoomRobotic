#https://www.baruch.cuny.edu/library/reservaroom/
from urllib import request,parse
from http.cookiejar import CookieJar
from bs4 import BeautifulSoup

class Loger:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    cookiejar = CookieJar()
    handler =  request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(handler)
    username_dic = {
        'q.rong','y.bai1'
    }

    def __init__(self,URL,username,password):
        self.URL = URL
        self._username = username
        self._password = password
        self._data = {
            'Username':username,
            'Password':password
        }


    def log(self):
        if self._username not in Loger.username_dic:
            raise ValueError

        if self._username in Loger.username_dic:
            req = request.Request(self.URL,data = parse.urlencode(
                self._data).encode('utf-8'),headers=Loger.headers)
            respond = self.opener.open(req)
        return respond

    def loged(self):
        page = self.log().read
        soup = BeautifulSoup(page,'html.parser')
        logname = soup.find_all('span',class_=  'username')

        print(logname.contents)








if __name__ == '__main__':
    URL = 'https://www.baruch.cuny.edu/library/reservaroom/'
    loger = Loger(URL,'q.rong','97Dec023781')
    loger.log()
    loger.loged()



