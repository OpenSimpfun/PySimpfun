import requests

def get_ins_list(token: str):
    headers = {
        "Authorization": token
        }
    req = requests.get("https://api.simpfun.cn/api/ins/list", headers=headers)
    data = req.json()
    return data["list"] if data["code"] == 200 else None