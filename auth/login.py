import requests

def get_token(username, password):
    url = "https://api.simpfun.cn/api/auth/login"
    data = {
        "username": username,
        "passwd": password
    }
    response = requests.post(url, data=data)
    if response.status_code != 200: return None
    if response.json()["code"] != 200: return None
    token = response.json()["token"]
    return token
