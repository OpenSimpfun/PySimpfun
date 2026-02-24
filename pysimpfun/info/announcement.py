import requests

def get_announcement_list():
    req = requests.get("https://api.simpfun.cn/api/announcement")
    data = req.json()
    return data["list"]
