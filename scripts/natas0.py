import natas
import requests

URL = "http://natas0.natas.labs.overthewire.org/"
USER = "natas0"
PASS = "natas0"
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
flag = natas.get_flag(URL,auth_basic)

if __name__ == "__main__":
    print(natas.msg, flag)