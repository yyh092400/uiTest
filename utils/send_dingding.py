import requests
def send_dingding_mesg(msg=None,phone=None):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": "通知",
            "text": msg
        },
        "at": {
                    'atMobiles':[phone],
                    "isAtAll":False  #是否@所有人
                }
    }
    try:
        response = requests.post(
            'https://oapi.dingtalk.com/robot/send?access_token=3527f06650491e8b246118d203e6d0490045010b7b41c04dd709f6a1e6f26415',
            json=data, headers=headers)
        if response.status_code == 200:
            print("消息发送成功")
        else:
            print(f"消息发送失败，状态码：{response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"发送消息过程中发生错误：{e}")

