import requests, natas0, natas, natas1

URL = 'http://natas2.natas.labs.overthewire.org'
USER = 'natas2'
PASS = natas1.flag
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
url_of_flag = 'http://natas2.natas.labs.overthewire.org/files/users.txt'

flag = natas.get_flag(url_of_flag, auth_basic)

if __name__ == "__main__":
    print(natas.msg, flag)