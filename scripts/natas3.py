import requests, re, natas, natas2

URL = 'http://natas3.natas.labs.overthewire.org/'
USER = 'natas3'
PASS = natas2.flag
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
url_of_flag = 'http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt'

flag = natas.get_flag(url_of_flag, auth_basic)

if __name__ == "__main__":
    print(natas.msg, flag)