# conding:utff-8
import requests
import time
s = requests.session()
import json

global cookieDict


cookieDict = {}

def getTimeStamp():

    t = time.time()
    nowTime = int(round(t * 1000))
    timeStamp = str(nowTime)
    return timeStamp

def refreshToken():

    headers = {'user-agent': 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)', 'rdi': "DT=iPhone7,1;SV=11.3;AV=3.6.0.1",
               'Cookie': "Hm_lvt_e78ff38557cf56b9dd1487bbc60d06d5=1526526790; UM_distinctid=1636c15beb528f-0e260b9eeec5ee-704c175a-4a640-1636c15beb614b"}
    url = "http:///kada.ngrok.kittygo.cn/refreshToken.json?clientSecretText=1ebd198a3d7af6c64f3ba4bc6ae9cdd%3B3ac9c3e206f4a298d9049f9c42dbeaa0&deviceId=3ac9c3e206f4a298d9049f9c42dbeaa0"


    r = requests.get(url=url, verify=False, headers=headers)

    return r.cookies

def cookie_change_dict(_hhdd_):

    hhdd_dict = _hhdd_.strip('""').strip('{}')

    hhdd = hhdd_dict.split(",")

    print(hhdd)


    hhdd_dict = {}

    for i in range(len(hhdd)):
        str1 = hhdd[i]
        str_num = str1.split(":")
        key = str_num[0]
        # if key != 'token':
        #     valuse = str_num[1]
        #     if valuse == 'null':
        #         valuse = None
        #     elif valuse == 'true':
        #         valuse = True
        #     elif valuse == 'false':
        #         valuse = False
        #     else:
        #         valuse = int(valuse)
        # else:
        valuse = str_num[1]


        hhdd_dict[key] = valuse

    hhdd = str(hhdd_dict)
    print("hhdd-------", hhdd)
    # hhdd = hhdd.strip('{}')
    hhdd = hhdd.replace(' ', '')
    print("hhdd-------", hhdd)
    hhdd = hhdd.replace("'", '"')
    # hhdd = hhdd.replace('"', '\"')
    hhdd = '\"' + hhdd + '\"'

    print("hhdd-------", hhdd)
    return hhdd



def getCookie(_hhdd_):

    hhdd_dict = _hhdd_.strip('""').strip('{}')

    hhdd = hhdd_dict.split(",")

    print(hhdd)


    hhdd_dict = {}

    for i in range(len(hhdd)):
        str1 = hhdd[i]
        str_num = str1.split(":")
        key = str_num[0]
        valuse = str_num[1]
        hhdd_dict[key] = valuse

    return hhdd_dict


#短信验证码登陆
def Code_Login_AndReg(htt, code, phone, userSequence, deviceId):

    payload = {'code': code, 'phone': phone,
               'userSequence': userSequence, 'deviceId': deviceId}
    headers = {'user-agent': 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)', 'rdi': "DT=iPhone7,1;SV=11.3;AV=3.6.0.1"}
    url = htt + "/user/codeLoginAndReg.json"
    r = requests.get(url=url, headers=headers, params=payload)
    print('Code_Login_AndReg-------------------------------------------')
    print(r.text)
    print(r.url)
    print(r.status_code)
    print(r.cookies)
    print(r.cookies['_HHDD_'])
    print(r.status_code)
    print(r.text)
    print('--------------------------------------------')
    return r.cookies['_HHDD_']


def login(loginName, htt):

    # htt = "http://10.0.10.61"
    htt1 = "http://kada.ngrok.kittygo.cn"

    payload = {'deviceId': '6c8c01b8-766c-33e9-b2a5-915bccebe8ae', 'loginName': loginName, 'password': 'KKgsp3f3bKeXY8KiAWckTw=='}
    headers = {'user-agent': 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)', 'rdi': "DT=iPhone7,1;SV=11.3;AV=3.6.0.1"}
    url = htt1 + "/user/login.json"
    r = requests.post(url=url, headers=headers, data=payload)
    print('login-------------------------------------------')
    print(r.cookies)
    print(r.cookies['_HHDD_'])
    print(r.status_code)
    print(r.text)
    print('--------------------------------------------')

    return r.cookies['_HHDD_']

# 手机绑定前置接口
def validatePhone(hhdd_dict, phone, deviceId, code, htt):

    # htt = "http://10.0.10.61"
    htt1 = "http://kada.ngrok.kittygo.cn"

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']
    JSESSIONID = hhdd_dict['JSESSIONID']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + \
                  token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\";" + "JSESSIONID=" + JSESSIONID

    url = htt + "/user/validatePhone.json"

    payload = {'phone': phone, 'deviceId': deviceId, 'code': code, 'password': 'KKgsp3f3bKeXY8KiAWckTw=='}


    headers = {
        'user-agent': 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)',
        'rdi': "DT=iPhone7,1;SV=11.3;AV=3.6.0.1",
        'Cookie': cookie_hhdd
    }

    r = requests.get(url=url, headers=headers, params=payload)
    print("validatePhone------------------------------------")
    print(r.url)
    print(r.cookies)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)
    print("-------------------------------------------------")

# 绑定接口 输入主userid
def doUnify(userid, htt):

    # htt = "http://10.0.10.61"
    htt1 = "http://kada.ngrok.kittygo.cn"

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']
    JSESSIONID = hhdd_dict['JSESSIONID']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + \
                  token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\";" + "JSESSIONID=" + JSESSIONID

    # cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + \
    #               token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""

    url = htt + "/user/doUnify.json"

    payload = {'userId': userid}

    headers = {
        'user-agent': 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)',
        'rdi': "DT=iPhone7,1;SV=11.3;AV=3.6.0.1",
        'Cookie': cookie_hhdd
    }

    r = requests.get(url=url, headers=headers, params=payload)
    print("doUnify------------------------------------")
    print(r.url)
    print(r.cookies)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)
    print("-------------------------------------------------")



# 微信绑定前置接口
# String appid
# String code
# String deviceId 设备唯一标识

def validateWechat(hhdd_dict, htt,  appid, code, deviceId):

    # htt = "http://10.0.10.61"r.cookies['_HHDD_']
    htt1 = "http://kada.ngrok.kittygo.cn"

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""

    url = htt + "/user/validateWechat.json"

    payload = {'appid': appid, 'code': code, 'deviceId': deviceId}

    headers = {
        'user-agent': 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)',
        'rdi': "DT=iPhone7,1;SV=11.3;AV=3.6.0.1",
        'Cookie': cookie_hhdd
    }

    r = requests.get(url=url, headers=headers, params=payload)
    print("validateWechat------------------------------------")
    print(r.url)
    print(r.cookies)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)
    print("-------------------------------------------------")
    return r.cookies['JSESSIONID']

# 获取短信验证码接口
def SMSCode(phoneNumber, intent, htt):

    # htt = "http://10.0.10.61"
    htt1 = "http://kada.ngrok.kittygo.cn"

    # userId = hhdd_dict['userId']
    # token = hhdd_dict['token']
    # extTime = hhdd_dict['extTime']

    # cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" +\
    #               token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""


    url = htt + "/verifyCode/SMSCode.json"

    payload = {'phoneNumber': phoneNumber, 'intent': intent}

    headers = {
        'user-agent': 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)',
        'rdi': "DT=iPhone7,1;SV=11.3;AV=3.6.0.1",
        # 'Cookie': cookie_hhdd
    }

    r = requests.get(url=url, headers=headers, params=payload)
    print("SMScode------------------------------------")
    print(r.url)
    print(r.cookies)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)
    print(r.cookies['JSESSIONID'])
    print("-------------------------------------------------")
    return r.cookies['JSESSIONID']


def getBook2List(hhdd_dict, htt):

    # htt = "http://10.0.10.61"
    htt1 = "http://pre2.service.hhdd.com"
    # htt1 = "http://kada.ngrok.kittygo.cn"

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""

    url = htt + "/subscribe/getBook2List.json"

    payload = {'pagingNumber': '1', 'pagingSize': '20000'}

    headers = {
        'user-agent': 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)',
        'rdi': "DT=iPhone7,1;SV=11.3;AV=3.7.0.1",
    'Cookie': cookie_hhdd
    }

    r = requests.get(url=url, headers=headers, params=payload)
    print("getBook2List------------------------------------")
    print(r.url)
    print(r.cookies)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)
    print("-------------------------------------------------")


def popup(isNew, hhdd_dict, htt):
    # 预发布环境
    # htt = "http://pre2.service.hhdd.com"
    # 测试环境
    # htt = "http://10.0.10.63:28080"
    url = htt + "/conf/popup.json"
    payload = {'isNew': isNew}

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""

    headers = {
        'user-agent': 'Dalvik/2.1.0(Linux; U; Android 5.1;OPPO A37m Build/LMY47I)',
        'rdi': "DT=OPPO A37m;SV=5.1;AV=3.7.3;CH=debugpackage",
        'Cookie': cookie_hhdd
    }
    r = requests.get(url=url, headers=headers, params=payload)
    print("popup------------------------------------")
    print(r.url)
    print(r.cookies)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)
    print("-------------------------------------------------")

# ios 打分开关
# 获取是否打开开关接口
def Get_Client_Config(hhdd_dict, htt):
    # 测试环境
    # htt = "http://10.0.10.63:28080"
    # 预发布环境
    # htt = "http://pre2.service.hhdd.com"
    url = htt + "/config/getClientConfig.json"

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""
    # 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)',
    headers = {
        'user-agent': 'Dalvik/2.1.0(Linux; U; Android 5.1;OPPO A37m Build/LMY47I)',
        'rdi': "DT=OPPO A37m;SV=5.1;AV=3.7.1;CH=debugpackage",
        'Cookie': cookie_hhdd
    }
    r = requests.get(url=url, headers=headers)
    print("Get_Client_Config------------------------------------")
    print(r.url)
    print(r.cookies)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)
    print("-------------------------------------------------")


# 获取用户创建时间
def Get_User_Detail(hhdd_dict, htt):

    # htt = "http://10.0.10.63:28080"
    # htt = "http://pre2.service.hhdd.com"
    url = htt + "/user/getUserDetail.json"

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""
    # 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)',
    headers = {
        'user-agent': 'Dalvik/2.1.0(Linux; U; Android 5.1;OPPO A37m Build/LMY47I)',
        'rdi': "DT=OPPO A37m;SV=5.1;AV=3.7.1;CH=debugpackage",
        'Cookie': cookie_hhdd
    }
    r = requests.get(url=url, headers=headers)
    print("Get_User_Detail------------------------------------")
    print(r.url)
    print(r.cookies)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)
    print("-------------------------------------------------")


def get_Login_Type(hhdd_dict, htt):

    # htt = "http://10.0.10.63:28080"
    url = htt + "/user/getLoginType.json"

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    deviceId = '03dc153f-e1d1-33df-9d31-587fa85f4d48'

    payload = {'deviceId': deviceId}

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""
    # 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)',
    headers = {
        'user-agent': 'Dalvik/2.1.0(Linux; U; Android 5.1;OPPO A37m Build/LMY47I)',
        'rdi': "DT=OPPO A37m;SV=5.1;AV=3.7.1;CH=debugpackage",
        'Cookie': cookie_hhdd
    }
    r = requests.get(url=url, headers=headers, params=payload)
    print("get_Login_Type------------------------------------")
    print(r.url)
    print(r.cookies)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)
    print("-------------------------------------------------")


def get_Story2_List(hhdd_dict, htt):

    # htt = "http://10.0.10.63:28080"
    # htt = "http://pre2.service.hhdd.com"
    url = htt + "/subscribe/getStory2List.json"

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    pagingNumber = 1
    pagingSize = 10000
    # sourceId = 22328
    # sourceId =

    payload = {'pagingNumber': pagingNumber, 'pagingSize' : pagingSize}

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""
    # 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)',
    headers = {
        'user-agent': 'Dalvik/2.1.0(Linux; U; Android 5.1;OPPO A37m Build/LMY47I)',
        'rdi': "DT=OPPO A37m;SV=5.1;AV=3.7.3;CH=debugpackage",
        'Cookie': cookie_hhdd
    }
    r = requests.get(url=url, headers=headers, params=payload)
    print("get_Login_Type------------------------------------")
    print(r.url)
    print(r.cookies)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)
    print("-------------------------------------------------")
    a_dict = r.json()
    with open('data.json', 'w') as json_file:
        json.dump(a_dict, json_file, ensure_ascii = False, indent=4)




def unsubscribe(hhdd_dict, htt):

    # htt = "http://pre2.service.hhdd.com"
    # htt = ""
    url = htt + "/subscribe/unsubscribe.json"

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    sourceType = 2
    sourceIdStr = '20196, 21901, 26332, 20209, 21678'

    payload = {'sourceType': sourceType, 'sourceIdStr' : sourceIdStr}

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""
    # 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)',
    headers = {
        'user-agent': 'Dalvik/2.1.0(Linux; U; Android 5.1;OPPO A37m Build/LMY47I)',
        'rdi': "DT=OPPO A37m;SV=5.1;AV=3.7.3;CH=debugpackage",
        'Cookie': cookie_hhdd
    }
    r = requests.get(url=url, headers=headers, params=payload)
    print("get_Login_Type------------------------------------")
    print(r.url)
    print(r.cookies)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)
    print("-------------------------------------------------")
    a_dict = r.json()
    with open('data.json', 'w') as json_file:
        json.dump(a_dict, json_file, ensure_ascii = False, indent=4)


def get_Client_Config(hhdd_dict, htt):

    # htt = "http://10.0.10.63:28080"
    url = htt + "/config/getClientConfig.json"

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""
    # 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)',
    headers = {
        'user-agent': 'Dalvik/2.1.0(Linux; U; Android 5.1;OPPO A37m Build/LMY47I)',
        'rdi': "DT=OPPO A37m;SV=5.1;AV=3.7.6;CH=debugpackage",
        'Cookie': cookie_hhdd
    }
    r = requests.get(url=url, headers=headers)
    print("get_Client_Config------------------------------------")
    print(r.url)
    print(r.cookies)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)
    print("-------------------------------------------------")
    a_dict = r.json()
    with open('data.json', 'w') as json_file:
        json.dump(a_dict, json_file, ensure_ascii = False, indent=4)


def Get_Book_List(hhdd_dict, htt):
    # 绘本列表接口
    url_book_n = htt + "/book2/otherCollectList.json"

    url_story_n = htt + "/story2/getStoryList.json"

    # 随便看看 绘本 第一页数据
    list_sourceId = []

    dict_souceId = {}

    dict_souceId_number = {}


    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"false\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""

    # 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)',
    headers = {
        'user-agent': 'Dalvik/2.1.0(Linux; U; Android 5.1;OPPO A37m Build/LMY47I)',
        # 'rdi': "DT=OPPO A37m;SV=5.1;AV=3.7.3;CH=debugpackage",
        'rdi': "DT=iPhone8,1;SV=12.0;AV=3.8.0.1;CH=debugpackage",
        'Cookie': cookie_hhdd
    }
    # new_probation_plan_sourceId_list = [60214, 52618, 60169, 60126, 60104, 60065]

    probation_plan_sourceId_list = [53159, 50081, 50104, 53157, 50723, 53155, 50625, 51416, 53293, 50067, 53161, 50156, 52120, 53154, 53302, 50125, 50103, 50105, 50070, 51003, 53664, 50834, 53482, 51088, 53156, 53483, 50075, 53303, 50998, 53160, 51269, 50097, 51455, 50146, 51087, 50626, 51276, 53667, 50726, 51564, 51259, 52024, 51997, 50623, 50119, 50074, 55132, 55151, 53162, 53623, 50624, 53485, 51311, 53179, 51239, 53549, 51301, 51029, 50994, 53243, 53332, 53121, 51249, 50789, 53665, 51684, 51477, 50107, 53151, 50501, 51037, 50109, 50043, 51967, 50138, 53133, 54926, 50145, 55152, 50096, 53131, 51032, 50065, 51034, 52249, 51337, 50406, 51844, 51350, 53313, 52805, 50083, 50633, 51812, 50839, 51438, 50995, 53134, 53178, 50100, 52741, 51243, 52832, 50099, 50763, 51849, 50033, 52314, 50853, 53314, 52203, 50776, 50112, 50616, 53661, 50136, 51594, 50795, 52323, 52731, 52733, 54581, 52732, 51030, 51555, 53119, 55199, 53490, 55200, 52591, 51112, 53111, 53092, 51113, 53558, 53112, 51681, 51783, 51974, 50047, 52593, 50128, 50850, 51925, 52923, 52567, 50892, 50073, 53559, 50399, 55205, 50115, 51380, 52536, 51710, 53528, 51920, 52187, 52259, 51825, 51679, 50036, 55128, 50500, 51721, 50689, 50790, 52553, 50147, 51642, 51512, 51971, 50650, 50649, 51731, 50870, 55197, 54927, 50983, 53601, 51323, 54928, 55203, 53428, 50651, 51233, 53244, 50579, 53409, 53152, 55204, 52922, 52586, 52587, 53246, 52114, 51972, 50605, 53407, 50982, 53408, 50615, 50751, 50515, 52287, 50048, 52081, 50420, 50895, 52027, 51242, 55202, 51434, 52544, 50102, 51678, 51921, 54711, 53534, 51986, 52552, 53410, 52585, 52565, 53669, 52028, 53682, 50407, 50843, 54601, 50377, 50359, 50974, 55311, 52083, 51988, 53487, 54640, 50068, 52361, 51258, 50388, 54991, 53553, 51231, 52551, 50416, 52493, 54900, 52413, 52548, 53242, 52410, 53580, 54356, 50606, 55021, 51209, 51916, 52283, 52494, 51667, 52885, 50349, 52097, 53334, 51437, 52549, 52967, 53102, 52235, 50076, 50672, 53684, 52412, 51727, 52642, 53105, 53681, 51774, 55471, 53091, 50038, 53271, 52109, 51118, 50064, 50443, 52722, 52543, 50728, 55120, 50085, 50886, 51074, 50685, 50864, 52800, 50356, 52884, 51865, 51926, 51110, 50051, 52116, 50444, 52814, 52881, 51205, 51442, 51585, 53176, 51561, 50803, 53603, 53551, 51629, 50077, 52352, 53002, 52084, 50999, 52205, 50679, 50984, 51397, 53613, 50357, 53113, 50370, 51791, 53702, 50088, 50044, 50740, 53106, 53252, 52886, 53604, 51449, 51400, 52363, 51830, 50553, 51954, 50375, 50387, 52701, 53488, 52322, 53411, 51142, 51379, 52882, 52371, 53120, 55131, 52541, 53614, 50769, 50855, 51875, 51652, 53818, 53658, 51960, 52742, 51440, 50140, 51588, 55371, 53116, 50683, 50785, 51782, 51725, 51000, 51267, 53219, 53245, 53220, 50762, 50362, 53671, 50671, 52963, 55207, 53174, 50391, 50371, 50883, 50394, 52252, 50953, 55315, 50363, 51156, 55301, 50878, 52961, 51752, 51846, 55402, 53027, 51436, 51107, 50930, 50931, 50675, 53532, 53254, 51724, 51918, 53013, 50673, 52495, 51959, 52909, 50397, 51462, 51150, 50382, 53175, 50707, 51353, 50367, 55342, 51699, 52696, 53218, 52702, 50916, 55079, 50117, 52298, 50378, 50543, 52664, 50662, 50634, 50765, 53611, 50374, 51847, 51001, 53117, 52055, 50353, 53522, 50440, 50899, 52721, 51146, 51683, 52970, 50130, 52540, 54981, 52929, 50052, 50591, 51456, 51234, 50405, 53489, 51644, 50365, 51963, 50423, 50464, 50050, 51985, 52062, 50922, 55431, 50398, 52883, 50668, 51723, 52392, 51889, 51333, 51751, 52969, 50879, 51651, 51696, 55438, 51984, 50670, 52393, 51923, 55346, 50801, 51556, 50881, 50809, 50808, 53114, 51439, 50664, 51955, 51091, 52542, 50389, 51843, 52262, 51700, 55461, 50836, 50424, 51433, 51049, 52186, 50786, 52871, 50667, 53273, 52703, 52385, 51109, 52592, 50547, 52315, 50665, 51861, 51811, 50585, 50686, 51957, 50412, 50806, 50722, 51349, 51108, 51378, 50066, 50718, 53581, 50684, 50361, 52707, 50372, 52695, 50379, 53840, 53058, 53576, 51638, 50046, 50807, 55451, 50636, 51653, 55443, 50380, 50502, 51893, 50976, 50390, 50800, 52962, 50987, 52011, 51414, 51917, 50970, 51391, 55218, 51596, 51732, 52414, 50360, 55209, 51620, 52491, 50427, 53556, 52764, 51951, 51388, 55125, 51664, 51255, 54354, 50813, 51098, 51891, 50154, 52908, 52763, 50744, 50063, 51117, 50439, 50897, 51515, 50681, 50403, 51253, 52246, 52162, 51143, 52198, 53486, 55196, 52365, 50906, 50351, 50385, 50805, 50344, 50842, 53093, 55435, 50680, 52911, 50660, 51322, 51565, 51763, 52817, 50429, 51778, 50658, 50437, 51878, 51458, 52274, 53832, 52182, 51236, 50706, 52986, 53255, 50527, 51945, 51968, 50996, 52199, 50542, 51726, 50346, 50400, 51484, 50721, 50084, 53552, 50393, 52256, 51775, 52827, 51360, 51247, 51781, 53612, 55344, 50548, 52831, 52021, 51444, 50122, 50123, 50417, 51697, 51662, 51877, 51341, 50880, 51254, 53491, 50499, 52487, 51628, 52407, 52212, 52743, 51982, 50384, 50497, 51899, 53662, 50495, 52937, 50838, 51384, 51425, 55404, 52293, 50875, 52907, 50802, 55192, 50663, 50659, 50419, 51562, 53021, 51958, 51351, 50739, 51574, 50366, 51948, 51264, 50514, 51802, 50466, 52866, 51704, 51193, 51953, 50963, 50137, 50489, 53841, 53054, 51691, 52933, 51347, 53495, 55220, 51270, 50546, 52799, 52715, 51017, 52032, 51464, 51848, 50072, 51569, 50657, 52023, 50743, 52333, 50430, 50376, 53842, 50582, 51741, 50496, 51792, 50587, 51658, 50538, 51480, 51395, 51608, 51361, 50494, 51965, 50682, 51261, 51964, 50493, 51601, 50563, 50884, 51348, 50536, 51801, 52282, 51123, 52671, 50108, 51730, 51140, 52951, 52638, 50782, 51381, 52905, 51412, 51761, 53533, 53062, 55341, 54901, 50540, 50418, 51387, 53272, 51692, 52208, 51336, 53547, 50507, 52930, 50474, 52872, 50350, 52091, 50383, 51637, 51262, 51991, 51981, 52250, 52570, 52382, 50560, 50595, 51944, 52251, 53253, 53053, 50592, 52275, 51690, 55381, 51648, 51566, 50904, 51263, 51950, 51096, 55432, 52364, 52762, 51470, 51012, 52142, 50578, 53103, 52771, 51880, 51551, 53833, 50986, 51106, 50661, 52231, 51927, 52865, 50411, 51272, 50702, 55421, 51779, 52206, 51331, 51483, 50373, 51251, 51649, 50594, 51204, 50989, 51277, 53560, 51563, 53571, 50413, 52654, 52852, 51097, 51362, 51467, 51894, 50948, 51962, 52830, 53211, 51443, 50771, 51417, 50905, 52108, 50735, 52319, 52345, 50396, 52258, 50485, 51616, 50545, 51693, 52676, 52074, 52001, 52326, 50583, 51983, 52191, 50637, 51687, 52223, 52273, 53055, 51085, 51611, 53251, 55206, 53574, 50734, 52342, 53170, 50438, 53406, 51929, 52966, 52864, 51851, 51626, 50935, 51665, 51343, 51196, 51047, 52869, 51646, 52201, 52277, 52403, 50604, 52931, 51703, 50492, 55441, 52879, 52853, 51636, 53575, 53115, 52279, 52854, 52172, 53063, 51722, 51966, 50912, 53202, 51532, 52381, 51572, 51473, 50690, 51491, 51435, 50506, 52761, 50577, 52861, 50484, 51002, 51773, 52697, 52325, 50041, 53011, 50121, 51126, 52118, 51623, 51518, 51246, 51016, 50111, 52868, 50442, 53834, 54909, 53082, 51712, 51095, 53685, 50551, 52051, 52880, 50856, 51701, 51603, 52204, 52673, 53250, 50523, 50414, 52926, 52716, 51392, 51148, 52661, 52932, 51659, 51728, 50874, 52411, 53572, 52900, 51159, 51149, 50666, 52391, 50641, 50784, 53703, 52255, 50979, 51931, 50714, 52106, 55433, 52384, 51094, 50080, 52217, 55161, 50368, 51044, 51827, 52936, 51468, 51121, 51780, 51122, 52131, 50386, 51591, 51999, 51643, 52243, 51654, 51911, 52404, 51866, 52554, 51590, 52054, 52179, 51632, 52286, 51474, 51883, 52550, 50745, 55361, 51579, 51052, 52052, 51598, 51471, 50603, 51198, 51842, 50764, 52829, 51420, 53172, 50508, 52031, 53531, 52064, 51411, 50513, 52906, 51705, 50132, 50124, 51354, 51776, 52547, 51573, 51145, 50947, 55322, 52087, 51007, 51418, 51399, 50799, 52095, 51153, 50566, 50760, 52295, 51657, 55219, 52658, 50958, 53052, 51120, 51542, 52974, 50861, 51266, 52719, 51998, 51892, 51777, 53622, 51709, 52486, 52409, 50521, 55314, 51771, 52942, 51245, 52053, 51863, 50564, 52692, 54285, 50525, 52316, 51250, 50761, 54910, 51666, 50840, 50134, 52718, 53657, 51729, 53171, 51424, 51469, 55312, 51924, 50992, 52744, 52324, 50710, 51592, 51823, 51615, 52094, 51935, 52072, 52698, 53274, 50609, 50911, 52965, 54361, 50032, 51826, 52030, 52183, 52700, 50985, 50692, 52096, 51321, 50704, 52068, 50698, 52928, 51647, 52224, 51873, 51607, 50737, 51413, 51163, 52284, 51645, 52652, 51933, 51898, 52207, 50517, 53654, 51014, 53281, 51151, 55321, 50688, 51050, 50602, 51639, 52192, 52651, 52694, 53656, 51656, 50133, 51670, 51176, 50687, 52964, 51359, 51867, 52653, 53846, 52714, 53524, 50598, 55401, 50788, 52821, 51450, 51240, 52098, 50572, 50774, 52819, 52824, 51257, 50408, 50957, 52362, 52823, 50589, 51821, 50581, 53061, 51466, 51238, 51593, 52561, 51663, 53012, 51897, 52987, 52291, 52194, 50891, 50719, 52870, 50568, 52225, 51806, 51463, 50580, 51162, 50510, 50584, 53843, 53173, 50798, 52041, 53655, 51772, 50693, 51445, 52161, 50552, 51489, 51358, 50898, 50415, 51482, 50700, 52851, 51168, 51235, 50775, 52816, 52867, 51824, 50434, 54351, 51155, 50938, 51803, 52189, 50914, 51479, 52180, 51133, 50588, 51465, 55411, 53845, 53023, 54908, 51882, 52171, 51201, 51655, 52102, 51650, 50696, 51192, 52462, 51613, 51129, 50703, 50913, 51989, 52818, 51476, 51995, 52245, 51733, 51053, 50465, 51586, 51045, 52944, 52099, 50954, 53081, 51597, 51568, 52934, 52100, 50901, 52339, 51680, 52940, 51161, 50865, 51018, 52708, 50467, 53835, 52546, 51612, 50900, 53837, 50402, 51913, 51075, 52804, 53573, 50993, 52665, 51457, 52253, 52303, 51332, 52232, 52711, 50950, 50932, 51160, 50071, 50590, 50695, 51695, 50596, 51805, 53523, 53025, 52863, 50944, 55208, 53838, 51922, 50600, 53283, 50511, 51887, 53844, 53660, 52988, 51021, 53024, 51900, 51244, 53026, 53847, 51641, 50952, 51357, 50716, 52299, 50715, 54166, 54637, 61719, 51157, 52985, 53836, 51195, 51554, 51461, 50960, 52188, 50951, 51831, 52943, 50711, 51475, 53064, 50887, 52177, 51130, 52776, 50873, 50554, 50708, 51386, 52104, 52820, 52842, 51022, 53212, 52562, 50699, 50959, 51207, 52973, 50910, 51881, 50908, 53550, 51252, 52538, 50697, 50597, 51385, 50946, 52175, 50961, 50717, 50608, 51005, 52254, 51762, 51698, 50691, 52899, 51019, 52292, 55434, 50617, 55129, 51232, 50709, 52075, 51194, 51158, 52773, 50593, 50964, 51486, 52341, 51919, 52101, 50601, 51606, 53831, 52278, 50962, 51884, 51271, 51890, 52968, 53107, 50347, 50955, 50945, 51256, 51614, 50867, 53839, 51342, 51131, 51371, 50779, 50694, 52302, 52991, 51165, 51605, 51915, 52073, 51202, 52103, 51283, 55347, 50796, 51602, 50780, 52990, 50915, 51822, 52343, 53653, 51127, 51390, 51617, 51885, 53057, 50909, 50949, 52941, 51631, 51134, 52200, 52921, 55201, 51208, 54165, 50939, 52901, 50705, 51023, 50586, 52174, 52276, 50599, 52061, 52066, 51164, 53543, 51125, 52903, 51203, 50712, 50772, 50956, 50395, 51197, 55345, 51191, 52902, 51135, 52190, 52952, 50866, 53548, 50907, 51020, 52132, 51166, 51167, 53544, 51175, 50943, 50701, 51930, 51132, 51128, 51124, 63461, 62904, 50131, 51460]

    n = 0
    paging_size = 60


    for paging_number in range (1, 10):
        payload = {'pagingSize': paging_size, 'pagingNumber': paging_number}
        r = requests.get(url=url_book_n, headers=headers, params=payload)
        a_dict = r.json()
        data_len = len(a_dict['data'])
        data_List = a_dict['data']

        list_sourceId = []

        #单绘本sourceId 加入list中
        for data in data_List:
            if data['type'] == 1:
                list_sourceId.append(data['sourceId'])

        #打印单绘本出现次数
        for sourceId in list_sourceId:
            num = 0
            num = list_sourceId.count(sourceId)
            if num > 1:
                print(paging_number, sourceId, num)
                print("----------------------------分割线------------------------")


        for sourceId in list_sourceId:

            t = (sourceId in probation_plan_sourceId_list)
            dict_souceId[sourceId] = t
        #
        #     if sourceId in probation_plan_sourceId_list:
        #         n = n + 1
        #         print(n)
        #         print(sourceId, paging_number)
            if dict_souceId.get(sourceId):
                if dict_souceId_number.get(sourceId):
                    num = dict_souceId_number[sourceId] + 1
                    dict_souceId_number[sourceId] = num
                else:
                    dict_souceId_number[sourceId] = 1

        print("第{0}页获取绘本总个数{1}个--------".format(paging_number, data_len))
        n = n + data_len

        # print(paging_number, dict_souceId)
        json_name = 'book2_otherCollectList' + str(paging_number) + '.json'
        with open(json_name , 'w',encoding='utf-8') as json_file:
            json.dump(a_dict, json_file, ensure_ascii=False, indent=4)

    print("souceId比较结果：", dict_souceId)
    print("souceId出现次数：", dict_souceId_number)
    print("总数：", n)


    probation_plan_sourceId_list1 = [20818, 20819, 20820, 20821, 20823, 20824, 3715, 3714, 3683, 3684, 3661, 3662, 3644, 3646, 3613, 3577, 3614, 3544, 3576, 3543, 3445, 3446, 3425, 3426, 3393, 3394, 3337, 3336, 3379, 3349, 3378, 3368, 3369, 3315, 3288, 3347, 3277, 3278, 3732, 3316, 3764, 3289, 3765, 3731, 3568, 5811, 5937, 5769, 5768, 5765, 5882, 5812, 5936, 5901, 5881, 5821, 5973, 5971, 4836, 4837, 4864, 4863, 4862, 4861, 5709, 5711, 5710, 3370, 3371, 3382, 3383, 3397, 3421, 3447, 3398, 3448, 3469, 3422, 3467, 3631, 3632, 3630, 3629, 2422, 2425, 2427, 2426, 2428, 2430, 2431, 2432, 3964, 3965, 3966, 3967, 3968, 3969, 4029, 4024, 4025, 4035, 4027, 4033, 5400, 6791, 3225, 1368, 5389]

    n = 0

    # 随便看看 听书 数据

    paging_size = 60
    # paging_number = 1



    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"false\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""
    # 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)',
    headers = {
        'user-agent': 'Dalvik/2.1.0(Linux; U; Android 5.1;OPPO A37m Build/LMY47I)',
        'rdi': "DT=OPPO A37m;SV=5.1;AV=3.7.3;CH=debugpackage",
        'Cookie': cookie_hhdd
    }

    for paging_number in range (1, 11):

        payload = {'pagingSize': paging_size, 'pagingNumber': paging_number}

        r = requests.get(url=url_story_n, headers=headers, params=payload)
        # print("随便听听---" + str(paging_number))
        # print(r.url)
        # print(r.cookies)
        # print(r.request.headers)
        # print(r.status_code)
        # print(r.text)
        # print("-------------------------------------------------")
        a_dict = r.json()
        data_len = len(a_dict['data'])
        # print("获取听书总个数：" + str(data_len))
        data_List = a_dict['data']
        list_sourceId = []

        #听书storyId加入list
        for data in data_List:
            if data['type'] == 2:
                list_sourceId.append(data['data']['storyId'])

        for storyId in list_sourceId:
            if storyId == '13465':
                print("13465 找到了")
                break

        print("没找到")

        #听书storyId出现次数
        for storyId in list_sourceId:
            num = 0
            num = list_sourceId.count(storyId)
            if num > 1:
                print(paging_number, storyId, num)
                print("----------------------------分割线------------------------")

        for storyId in list_sourceId:

            t = (storyId in probation_plan_sourceId_list)
            dict_souceId[storyId] = t

            if storyId in probation_plan_sourceId_list1:
                n = n + 1
                print(n)
                print(storyId, paging_number)

            if dict_souceId.get(storyId):
                if dict_souceId_number.get(storyId):
                    num = dict_souceId_number[storyId] + 1
                    dict_souceId_number[storyId] = num
                else:
                    dict_souceId_number[storyId] = 1


        print("第{0}页获取听书总个数{1}个--------".format(paging_number, data_len))

        json_name = 'story2_getStoryList' + str(paging_number) + '.json'
        with open(json_name, 'w',encoding='utf-8') as json_file:
            json.dump(a_dict, json_file, ensure_ascii=False, indent=4)

    print("souceId出现次数：", dict_souceId_number)


def Get_Week_Report(htt, key, timestamp):

    # htt = "http://10.0.10.52:8081/report/weekReport.json"
    url = htt + "/report/weekReport.json"
    # key = "0000b282b7070b4dd31c05210f82453b"             #userid的md5值
    # timestamp = "1535817600000"       #阅读报告周期时间戳（指定周期的中周日的时间）
    payload = {'key': key, 'timestamp': timestamp}

    r = requests.get(url=url, params=payload)
    print(r.url, r.status_code)
    print(r.text)
    a_dict = r.json()
    json_name = 'weekReport.json'
    with open(json_name, 'w') as json_file:
        json.dump(a_dict, json_file, ensure_ascii=False, indent=4)


def Get_Day_Report(htt, key, timestamp):

    url = htt + "/report/dayReport.json"
    # key = "0000b282b7070b4dd31c05210f82453b"             #userid的md5值
    # timestamp = "1536336000000"       #阅读报告周期时间戳（指定某日时间戳）
    payload = {'key': key, 'timestamp': timestamp}

    r = requests.get(url=url, params=payload)
    print(r.url, r.status_code)
    print(r.text)
    a_dict = r.json()
    json_name = 'dayReport.json'
    with open(json_name, 'w') as json_file:
        json.dump(a_dict, json_file, ensure_ascii=False, indent=4)

def Get_Daily_ShortMsg(htt, key, timestamp):

    url = htt + "/report/dailyShortMsg.json"
    # key = "00be179a05105d5ab4061bae380fbaf1"  # userid的md5值
    # timestamp = "1516377600000"  # 阅读报告周期时间戳（指定某日时间戳）
    payload = {'key': key}

    r = requests.get(url=url, params=payload)
    print(r.url, r.status_code)
    print(r.text)
    a_dict = r.json()
    json_name = 'dailyShortMsg.json'
    with open(json_name, 'w') as json_file:
        json.dump(a_dict, json_file, ensure_ascii=False, indent=4)

def Get_Medal_CategoryList(hhdd_dict, htt):

    url = htt + "/medal/getMedalCategoryList.json"

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""

    # 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)',
    headers = {
        'user-agent': 'Dalvik/2.1.0(Linux; U; Android 5.1;OPPO A37m Build/LMY47I)',
        'rdi': "DT=OPPO A37m;SV=5.1;AV=3.6.6;CH=debugpackage",
        'Cookie': cookie_hhdd,
        'Authorization': "IlcSEkcZJjMIend9CTJdLQBpBR8BSR5wdB1GaDpmbUI+aWQcf0s/RwNGaUxWEGFbYx8="
    }
    r = requests.get(url=url, headers=headers)
    print("Get_Medal_CategoryList------------------------------------")
    print(r.url)
    print(r.cookies)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)
    print("-------------------------------------------------")
    a_dict = r.json()
    # return a_dict
    with open('getMedalCategoryList.json', 'w') as json_file:
        json.dump(a_dict, json_file, ensure_ascii=False, indent=4)


def Get_MedListByCateList(hhdd_dict, htt):

    url = htt + "/medal/getMedalListByCategoryIdList.json"

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    payload = {'categoryIds': "[1,2,3,4,5,6,7]"}
    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""

    # 'KaDa/3.6.0 (iPhone; iOS 11.3; Scale/3.00)',
    headers = {
        'user-agent': 'Dalvik/2.1.0(Linux; U; Android 5.1;OPPO A37m Build/LMY47I)',
        'rdi': "DT=OPPO A37m;SV=5.1;AV=3.6.6;CH=debugpackage",
        'Cookie': cookie_hhdd,
        'Authorization': "MisdUHpcMFJOA3xcLkIpYBhbNmIaCVMqUitgKjhAVWdtN1BjLktuODcYOmluNmMvZg8="
    }

    r = requests.get(url=url, headers=headers, params=payload)
    print("Get_MedListByCateList------------------------------------")
    print(r.url)
    print(r.cookies)
    print(r.request.headers)
    print(r.status_code)
    print(r.text)
    print("-------------------------------------------------")
    a_dict = r.json()
    # return a_dict
    with open('Get_MedListByCateList.json', 'w') as json_file:
        json.dump(a_dict, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':


    # hhdd_dict = {'userId':'60006701', 'token':"2c5fa10326ac1423fbddcc7226cfa716", 'extTime':'1570792940257'}  # 7日外老用户
    hhdd_dict = {
        'userId': '60007436',  # 7日内新用户
        'token': 'bdb73fbdec2fc393e3611de3b0c90af2',
        'extTime': '1572314356732'
    }
    # hhdd_dict = {'userId': '60007174', 'token': '7419c57392131a0dcb79beef6a82f6bc', 'extTime': '1572055214499'}  # 我自己的

    # htt = "http://mom1.hhdd.com"

#6721145
    key = "c44393f2095d9415331d2328fefeb78b"
    timestamp = "1539446400000"
    # Get_Week_Report(htt, key, timestamp)


#8879721
    key = "d42e9b41cedc2916f6d84636d778c229"
    timestamp = "1538928000000"
    # Get_Day_Report(htt, key, timestamp)


    # key = "88da48291edf094b5972625ccc9e83de"  # userid的md5值
    key = "c44393f2095d9415331d2328fefeb78b"
    timestamp = '1539273600000'
    # timestamp = "1516377600000"  # 阅读报告周期时间戳（指定某日时间戳）
    # Get_Daily_ShortMsg(htt, key, timestamp)

    # htt = "http://10.0.10.62:14080"

    # Get_Medal_CategoryList(hhdd_dict, htt)
    # Get_MedListByCateList(hhdd_dict, htt)







    # 测试环境地址
    htt = "http://10.0.10.61"
    # intent = "loginPhone"
    # phoneNumber = "18505819201"
    # userSequence = "2a6ccfd3-b699-31c8-96ec-7e0cfe3f493a"
    # deviceId = "2a6ccfd3-b699-31c8-96ec-7e0cfe3f493a"
    #
    # hhdd_js = SMSCode(htt=htt, phoneNumber=phoneNumber, intent=intent)
    #
    # cookie = Code_Login_AndReg(htt=htt, code='123456', phone=phoneNumber, userSequence=userSequence, deviceId=deviceId)

    # 预发布环境地址
    # htt = "http://pre2.service.hhdd.com"

    #正式环境地址

    # htt = "https://service.hhdd.com"
    #
    # popup('0', hhdd_dict, htt)
    #
    # Get_User_Detail(hhdd_dict, htt)
    # #
    # Get_Client_Config(hhdd_dict, htt)
    #
    # # get_Login_Type(hhdd_dict)
    #
    # get_Story2_List(hhdd_dict, htt)
    # getBook2List(hhdd_dict, htt)
    #
    # unsubscribe(hhdd_dict, htt)

    # get_Client_Config(hhdd_dict)

    # old_cookie = refreshToken()
    #
    # hhdd = "{userId:60002810,nick:null,token:35ffe4d5277412d5dc45fa5da391572b,extTime:1531277997571,login:true}"
    # hhdd_dict = getCookie(hhdd)
    #
    # #绑定微信
    # # 微信绑定前置接口
    #
    # # hhdd_dict['JSESSIONID'] = validateWechat(hhdd_dict, appid='wx8aa3c576a7fb1f13',
    # #                                          deviceId='6c8c01b8-766c-33e9-b2a5-915bccebe8ae',
    # #                                          code='001lEt2M06xOA42wkfZL0cut2M0lEt2I')
    # # doUnify('60002404')
    #
    # #绑定手机号码
    # hhdd_js = SMSCode('18505819201', 'unifyPhone')
    # hhdd_dict['JSESSIONID'] = hhdd_js
    # # 短信绑定前置接口
    # validatePhone(hhdd_dict, phone='18505819201', deviceId='d7beeee9-ca6b-3e71-9bf9-53fd5f017cc8', code='123456')
    # doUnify('60002810')

    # for index in range(1):
    #     url = "http://pre2.service.hhdd.com" + "/conf/getServiceIPList.json"
    #     r = requests.get(url)
    #     print(r.json())

    Get_Book_List(hhdd_dict, htt)

