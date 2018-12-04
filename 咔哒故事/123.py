# coding:utf-8
import requests
import json


def xianmian(htt):
    # http = htt + "/book2/getCollectItems.json"
    http = htt + "/story2/getCollectItems.json"
    hhdd_dict = {
        'userId': '60007413',  # 7日内新用户
        'token': '47f782fe83219ac62a0aedfbabfa2a4f',
        'extTime': '1572418286223'
    }
    # hhdd_dict = {
    #     'userId': '60006991',  # 7日外老用户
    #     'token': '165a178a4ffcc8b6d2102fcb6dc73dfc',
    #     'extTime': '1572416758924'
    # }

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"false\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""

    headers = {
        'Cookie': cookie_hhdd,
        'RDI': 'DT=OPPO A37m;SV=5.1;AV=3.7.3;CH=debugpackage',
        # 'rdi': 'DT=CLT-AL01;SV=8.1.0;AV=3.8.0;CH=debugpackage',
        'user-agent': 'Dalvik/2.1.0(Linux; U; Android 5.1;OPPO A37m Build/LMY47I)'
    }
    payload = {'collectId': "22798"}
    response = requests.get(url=http, headers=headers, params=payload)
    response_json = response.json()

    extFlag = response_json['data']['extFlag']  # 限免标志
    remainingTime = response_json['data']['remainingTime']  # 限免剩余时间

    print(extFlag, remainingTime)






if __name__ == '__main__':
    # htt = "http://10.0.10.61"
    htt = ''
    xianmian(htt)
