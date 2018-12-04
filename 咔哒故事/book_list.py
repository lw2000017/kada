# coding:utf-8
import requests
import json


def book_list(htt):
    # 瀑布流，随便看看
    url_book_n = htt + "/book2/otherCollectList.json"

    # url_story_n = htt + ""

    # hhdd_dict = {
    #         'userId': '60007413',  # 7日内新用户
    #         'token': '67ab406a0c52a1fd0f4cf14253250b4f',
    #         'extTime': '1572484393971'
    #     }

    hhdd_dict = {
        'userId': '60006991',  # 7日外老用户
        'token': '1539956bc1d00b3f39dbe5a5ad33577d',
        'extTime': '1572574301381'
    }

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""

    headers = {
        # 'user-agent': 'Dalvik/2.1.0(Linux; U; Android 5.1;OPPO A37m Build/LMY47I)',
        # 'rdi': "DT=OPPO A37m;SV=5.1;AV=3.7.3;CH=debugpackage",  # 回来问一下，这个rdi是什么鬼？
        'rdi': 'DT=MI 6;SV=8.0.0;AV=3.8.0;CH=debugpackage',
        'Cookie': cookie_hhdd,
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; MI 6 MIUI/V10.0.1.0.OCACNFH)',  # Android 设备标识
        'Authorization': 'ESQNF2o4CAsLZGF/Cj4rMnhaJGRhbj4AD1VFVxgrN001EmV8cUsxJwI9YkMMXUNhFCw=',
        'Connection': 'keep-alive',
        'Date': "Wed 31 Oct 2018 05:47:11 GMT",
        'Accept': '*/*',
        'Host': '10.0.10.61',
        'Content-Length': '0'

    }
    book_list_sourceid_list = [61787, 60182, 53425, 53481, 60076, 60107, 54873, 55200, 54040]

    pagingSize = 60

    for pagingNumber in range(1, 10):

        payload = {'pagingSize': pagingSize, 'pagingNumber': pagingNumber}
        response = requests.get(url=url_book_n, headers=headers, params=payload)
        data_sourceId = []
        r_json = response.json()
        # print(r_json)
        data_len = len(r_json['data'])

        # 将绘本id 加入data_sourceID
        for i in r_json['data']:
            # if i['type'] == 1:
            data_sourceId.append(i['sourceId'])

        print("第{0}页共有--------{1}绘本".format(pagingNumber, data_len))


        for data in data_sourceId:
            num = 0
            num = data_sourceId.count(data)
            # print(num)
            if num > 1:
                print(pagingNumber, data, num)
                print('---------------一条切割器---------------')
    # print(len(data_sourceId))



        json_name = 'book2_otherCollectList' + str(pagingNumber) + '.json'
        with open(json_name , 'w',encoding='utf-8') as json_file:
            json.dump(r_json, json_file, ensure_ascii=False, indent=4)




if __name__ == '__main__':

    htt = "http://10.0.10.61"   # 测试环境

    # htt = "http://pre2.service.hhdd.com"  # 预发环境

    book_list(htt)






















    """
    import hashlib
    import base64

    md5 = hashlib.md5()
    
    md5.update(b'get')  # method
    md5.update(b'\n')
    md5.update(b'*/*')  # accept
    md5.update(b'\n')
    md5.update(b'')     # bodyMd5
    md5.update(b'\n')
    md5.update(b'')    # content_type
    md5.update(b'\n')
    md5.update(b'Wed 31 Oct 2018 02:11:03 GMT')   # date
    md5.update(b'\n')
    md5.update(b'DT=MI 6;SV=8.0.0;AV=3.8.0;CH=debugpackage')    # rdi
    md5.update(b'\n')
    md5.update('/book2/otherCollectList.json?pagingSize=60&pagingNumber='.encode(encoding='utf-8'))     # pathurl
    md5.update(str(pagingNumber).encode(encoding='utf-8'))
    md5_md5 = md5.hexdigest()
    print(md5_md5)
    h1 = base64.b64encode(md5_md5.encode(encoding='utf-8'))
    h1_str = str(h1, 'utf-8')
    print(h1_str)
    """