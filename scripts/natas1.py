import natas, natas0
import requests

URL = "http://natas1.natas.labs.overthewire.org/"
USER = 'natas1'
PASS = natas0.flag
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
flag = natas.get_flag(URL,auth_basic)

if __name__ == "__main__":
    print(natas.msg, flag)