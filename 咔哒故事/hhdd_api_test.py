# coding:utf-8

import requests
import json
import pymysql

def Connect_Mysql(name, priority, status, maxVersion, minVersion, id):
    db = pymysql.connect(host='10.0.10.61', user='root', passwd='HZhhddR1209', db='configuring', port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM config_splash WHERE `status` = 1")    # 查询已经上线的闪屏信息
    data = cursor.fetchall()
    # print(data)
    # print(type(data))


    for i in data:
        id.append(i[0])  # id
        name.append(i[1])   # 查询结果的name
        priority.append(i[2])   # 查询结果优先级
        status.append(i[7])     # 查询结果 状态
        minVersion.append(i[8])     # 查询结果 最低版本号
        maxVersion.append(i[9])     # 查询结果 最大版本号

    db.close()


def Splash(htt, hhdd_dict):
    """闪屏配置接口"""

    http = htt + "/conf/splash.json"
    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""

    headers = {
        'Cookie': cookie_hhdd,
        'RDI': 'DT=MI 6;SV=8.0.0;AV=3.8.0;CH=debugpackage',
        'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; MI 6 MIUI/V10.0.1.0.OCACNFH)',
        'Date': 'Thu 1 Nov 2018 07:36:11 GMT'
    }
    # e = requests.
    response = requests.get(url=http, headers=headers)
    response_json = response.json()
    # print(response_json)
    a_dic = response_json['data']
    # print(a_dic)
    for i in range(len(a_dic)):
        print(a_dic[i])


if __name__ == '__main__':
    hhdd_dict = {
                 'userId': '60006991',
                 'token': "1539956bc1d00b3f39dbe5a5ad33577d",
                 'extTime': '1572574301381'
    }
    # import time
    # print(time.)
    name = []
    priority = []
    status = []
    maxVersion = []
    minVersion = []
    id = []
    Connect_Mysql(name, priority, status, maxVersion, minVersion, id)

    htt = 'http://10.0.10.61'

    # htt = "http://pre2.service.hhdd.com"  # 预发环境

    Splash(htt=htt, hhdd_dict=hhdd_dict)
    for i in range(len(name)):
        print(str(id[i]) + '----' + str(name[i]) + '----' + str(priority[i]) + '----' + str(status[i]) + '----' + str(maxVersion[i]) + '----' + str(minVersion[i]))

