import base64,requests, natas, natas7

URL = 'http://natas8.natas.labs.overthewire.org/'
USER = 'natas8'
PASS = natas7.flag
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
url_of_the_code = 'http://natas8.natas.labs.overthewire.org/index-source.html'

encoded_secret = natas.get_flag(url_of_the_code, auth_basic)
decoded_hex = bytes.fromhex(encoded_secret).decode('utf-8')
rev_string = decoded_hex[::-1]
b64_decoded = base64.b64decode(rev_string).decode()
header = {"Content-Type": "application/x-www-form-urlencoded"}
body = f'secret={b64_decoded}&submit=Submit'

flag = natas.get_flag_post(URL, auth_basic, body, header)

if __name__ == '__main__':
    print(natas.msg, flag)