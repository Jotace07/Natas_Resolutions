import requests, re, natas, natas5

URL = 'http://natas6.natas.labs.overthewire.org'
USER = 'natas6'
PASS = natas5.flag
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)

secret = 'FOEIUWGHFEEUHOFUOIU'
body = f'secret={secret}&submit=Submit'
flag = natas.get_flag_post(URL, auth_basic, body, headers={"Content-Type": "application/x-www-form-urlencoded"})

if __name__ == '__main__':
    print(natas.msg, flag)