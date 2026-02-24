import requests
import toml

def get_info():
    url = "https://api.simpfun.cn/api/auth/info"
    headers = {
        "Authorization": toml.load("config.toml")["token"]
        }
    response = requests.get(url, headers=headers)
    return response.json()