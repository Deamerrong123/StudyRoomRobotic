from urllib import request,parse
import requests
from http.cookiejar import CookieJar
from bs4 import BeautifulSoup

class Loger:

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
        self._headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'cookie' : 'redirected=false; _ga=GA1.2.1132941602.1568047287; _gid=GA1.2.1576673836.1568047287; PHPSESSID=2qa157seip2l2v9qsva54seu34'
        }


    def log(self):
        respond = None
        if self._username not in Loger.username_dic:
            respond = False
            raise ValueError

        if self._username in Loger.username_dic:
            req = request.Request(self.URL,data = parse.urlencode(
                self._data).encode('utf-8'),headers=Loger.headers)
            respond = self.opener.open(req)
        return respond

    def loaded(self):
        ## determined if we're redirected into a the personal page,
        ## with the unsername on the span, class = 'username'

        ##page = self.log()
        pages = requests.get(self.URL,headers = self._headers)
        with open('loggedPage.html','w',encoding = 'utf-8') as f:
            f.write(pages.content.decode('utf-8'))

if __name__ == '__main__':
    URL = 'https://www.baruch.cuny.edu/library/reservaroom/'
    loger = Loger(URL,'','')
    loger.loaded()



