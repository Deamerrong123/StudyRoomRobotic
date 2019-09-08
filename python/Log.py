#https://www.baruch.cuny.edu/library/reservaroom/
from urllib import request,parse
from http.cookiejar import CookieJar

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

    def __int__(self,URL,username,password):
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
                self.data).endcode('utf-8'),headers=Loger.headers)
            self.opener.open(req)





if __name__ == '__main__':
    URL = 'https://www.baruch.cuny.edu/library/reservaroom/'
    # respond = requests.get(URL).headers
    # print(respond)


