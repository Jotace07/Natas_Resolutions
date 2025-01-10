import natas, re, requests, base64, json
USER = 'natas11'
PASS = 'UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk'
URL = f'http://{USER}.natas.labs.overthewire.org/'
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
burp = {"http":"http://127.0.0.1:8080"}

def xor_encrypt(in_text):
    key = 'eDWo'
    text = in_text
    out_text = ''
    for i in range(len(text)):
        out_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return out_text

data = {"showpassword": "yes", "bgcolor": "#ffff99"}
payload = base64.b64encode(xor_encrypt(json.dumps(data)).encode()).decode()
cookie = {"data": f"{payload}"}

def get_flag():
    request = requests.get(url=URL, cookies=cookie, auth=auth_basic, proxies=burp)
    response_http = request.text
    flag_regex = re.findall('([0-9a-zA-Z]{32})', response_http)
    return flag_regex[0 if len(flag_regex) == 1 else 1]

print("The pass for the next level is:", get_flag())