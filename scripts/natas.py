import requests, re
msg = 'The pass for the next level is:'

def get_flag(url, auth, headers={}):
    get = requests.get(url, auth=auth, headers=headers)
    response_http = get.text
    flag_regex = re.findall('([0-9a-zA-Z]{32})', response_http)
    return flag_regex[0 if len(flag_regex) == 1 else 1]

def get_flag_post(url, auth, body, headers={}):
    get = requests.post(url, auth=auth, data=body, headers=headers)
    response_http = get.text
    flag_regex = re.findall('([0-9a-zA-Z]{32})', response_http)
    return flag_regex[0 if len(flag_regex) == 1 else 1]