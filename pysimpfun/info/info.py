import requests

def get_info(token: str):
    url = "https://api.simpfun.cn/api/auth/info"
    headers = {
        "Authorization": token
        }
    response = requests.get(url, headers=headers)
    return response.json()