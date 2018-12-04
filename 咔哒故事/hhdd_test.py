# coding:utf-8
import requests
import json
import time

# 瀑布流
def get_book_list(htt):
    # 绘本推荐列表
    n = 0
    paging_size = 60
    url_book_n = htt + "/book2/otherCollectList.json"
    # 听书\故事推荐列表
    url_story_n = htt + "/story2/getStoryList.json"

    # 传cookie
    # hhdd_dict = {
    #     'userId': '60007413',  # 7日内新用户
    #     'token': '67ab406a0c52a1fd0f4cf14253250b4f',
    #     'extTime': '1572484393971'
    # }
    hhdd_dict = {
        'userId': '60006991',  # 7日外老用户
        'token': '1539956bc1d00b3f39dbe5a5ad33577d',
        'extTime': '1572574301381'
    }

    dict_souceId = {}
    dict_souceId_number = {}


    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"true\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""

    # rdi = 'DT=OPPO A37m;SV=5.1;AV=3.7.3;CH=debugpackage'
    headers = {
        # 'user-agent': 'Dalvik/2.1.0(Linux; U; Android 5.1;OPPO A37m Build/LMY47I)',
        # 'rdi': "DT=OPPO A37m;SV=5.1;AV=3.7.3;CH=debugpackage",  # 回来问一下，这个rdi是什么鬼？
        'rdi': 'DT=CLT-AL01;SV=8.1.0;AV=3.8.0;CH=debugpackage',
        'Cookie': cookie_hhdd,
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; CLT-AL01 Build/HUAWEICLT-AL01'  # Android 设备标识
    }


    n = 0
    paging_size = 60
    # 抽取的id
    probation_plan_sourceId_list = [60319, 61787, 60182, 53425, 53481, 60076, 60107, 62017, 60806, 60214, 60970, 60072, 60465, 61928, 51112, 51113, 62680, 50049, 61845, 66076, 54012, 54015, 54016, 51380, 62263, 62596, 62763, 54873, 66059, 55200, 54040, 51074, 54928, 50156, 50050, 53528, 54656, 55052, 54769, 54903, 52196, 51233, 53092, 52259, 54927, 50047, 62014, 53351, 60648, 60126, 60162, 53198, 60104, 60647, 54963, 60062, 61208, 60223, 60024, 60803, 61123, 55181, 61302, 54202, 54204, 54702, 53951, 54035, 53981, 54201, 60869, 53987, 54353, 53996, 54208, 61609, 55203, 54139, 55205, 55199, 53999, 62594, 53982, 54206, 54226, 55204, 53992, 54352, 54203, 55202, 53995, 54731, 54205, 54017, 53994, 54872, 54711, 54700, 54699, 53932, 55505, 61611, 54227, 54288, 54371, 53971, 54406, 54900, 60334, 61612, 53990, 54207, 54038, 61366, 54891, 54136, 54654, 54653, 66075, 66058, 66056, 66055, 66014, 65959, 65956, 65954, 65951, 65948, 65945, 62843, 62115, 65901, 65903, 54010, 60192, 60231, 60895, 60032, 52615, 60356, 60898, 60042, 60170, 60357, 52802, 60139, 60118, 52678, 60084, 60027, 52606, 60035, 50078, 53694, 52983, 50073, 51825, 50094, 50850, 51453, 50515, 53512, 50723, 52410, 53334, 50079, 50920, 52121, 53542, 52981, 53669, 53487, 52910, 53401, 53428, 50895, 50045, 52187, 50606, 52027, 52287, 53244, 52028, 55128, 53553, 52251, 50999, 51356, 54167, 62636, 62037, 54046, 53541, 62281, 54390, 54793, 61310, 54045, 54044, 54135, 62063, 54553, 61856, 54250, 54463, 61986, 54732, 61464, 54721, 53896, 61079, 60594, 54251, 54133, 54137, 54766, 54401, 54172, 54416, 62190]
    # new_probation_plan_sourceId_list = [61787, 60182, 53425, 53481, 60076, 60107, 54873, 55200, 54040, 53490, 53651, 52967, 53671, 53030, 52535, 51442, 53532, 52975, 51710, 50081, 53559, 52878, 53601, 53032, 53580, 52471, 52877, 52532, 53558, 53684, 52565, 50078, 53495, 53465, 52982, 53681, 51380, 53577, 50759, 53682, 50104, 53452, 52983, 52455, 53454, 52534, 53462, 52874, 51394, 53603, 53073, 50843, 52873, 50125, 53074, 53450, 50553, 53168, 53575, 51003, 53453, 52909, 53604, 52875, 50118, 53252, 52876, 52328, 50157, 62017, 60806, 60022, 60077, 52895, 60634, 52624, 60126]

    # 去除列表重复数据
    probation_plan_sourceId_list1 = []
    for i in probation_plan_sourceId_list:
        if i not in probation_plan_sourceId_list1:
            probation_plan_sourceId_list1.append(i)
    print(probation_plan_sourceId_list1)



    for paging_number in range (1, 10):
        payload = {'pagingSize': paging_size, 'pagingNumber': paging_number}
        r = requests.get(url=url_book_n, headers=headers, params=payload)   # 请求绘本推荐列表接口
        a_dict = r.json()
        data_len = len(a_dict['data'])
        data_List = a_dict['data']
        list_sourceId = []


        # 单绘本sourceId 加入list中
        for data in data_List:
            # if data['type'] == 1:
            list_sourceId.append(data['sourceId'])
        # print(list_sourceId)
        # 打印单绘本出现次数
        for sourceId in list_sourceId:
            num = 0
            num = list_sourceId.count(sourceId)
            # print(num)
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
        # print(list_sourceId)
        print("第{0}页获取绘本总个数---{1}个".format(paging_number, data_len))
        n = n + data_len

        # print(paging_number, dict_souceId)
        json_name = 'book2_otherCollectList' + str(paging_number) + '.json'
        with open(json_name, 'w', encoding='utf-8') as json_file:
            json.dump(a_dict, json_file, ensure_ascii=False, indent=4)

    print("souceId比较结果：", dict_souceId)
    print("souceId出现次数：", dict_souceId_number)
    print("总数：", n)


def story_list(htt):
    http = htt + "/story2/getStoryList.json"

    hhdd_dict = {
        'userId': '60007413',  # 7日内新用户
        'token': '67ab406a0c52a1fd0f4cf14253250b4f',
        'extTime': '1572484393971'
    }
    # hhdd_dict = {
    #     'userId': '60006991',  # 7日外老用户
    #     'token': '165a178a4ffcc8b6d2102fcb6dc73dfc',
    #     'extTime': '1572416758924'
    # }

    dict_souceId = {}
    dict_souceId_number = {}

    userId = hhdd_dict['userId']
    token = hhdd_dict['token']
    extTime = hhdd_dict['extTime']

    cookie_hhdd = "_HHDD_=\"{\\\"userId\\\":\\\"" + userId + "\\\",\\\"nick\\\":\\\"\\\",\\\"token\\\":\\\"" + token + "\\\",\\\"login\\\":\\\"false\\\",\\\"extTime\\\":\\\"" + extTime + "\\\"}\""

    # rdi = 'DT=OPPO A37m;SV=5.1;AV=3.7.3;CH=debugpackage'
    headers = {
        # 'user-agent': 'Dalvik/2.1.0(Linux; U; Android 5.1;OPPO A37m Build/LMY47I)',
        # 'rdi': "DT=OPPO A37m;SV=5.1;AV=3.7.3;CH=debugpackage",  # 回来问一下，这个rdi是什么鬼？
        'rdi': 'DT=CLT-AL01;SV=8.1.0;AV=3.8.0;CH=debugpackage',
        'Cookie': cookie_hhdd,
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; CLT-AL01 Build/HUAWEICLT-AL01'  # Android 设备标识
    }

    n = 0
    paging_size = 60

    probation_plan_sourceId_list = []

    for paging_number in range(1, 8):

        payload = {'pagingSize': paging_size, 'pagingNumber': paging_number}

        r = requests.get(url=http, headers=headers, params=payload)
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

        probation_plan_sourceId_list1 = [21001, 13673, 21374, 22328, 23141, 23444]

        # 听书storyId加入list
        for data in data_List:
            if data['type'] == 2:
                list_sourceId.append(data['data']['storyId'])

        for storyId in list_sourceId:
            if storyId == '13465':
                print("13465 找到了")
                break

        print("没找到")

        # 听书storyId出现次数
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
        with open(json_name, 'w', encoding='utf-8') as json_file:
            json.dump(a_dict, json_file, ensure_ascii=False, indent=4)

    print("souceId出现次数：", dict_souceId_number)

if __name__ == '__main__':

    http = "http://10.0.10.61"

    # htt = "http://pre2.service.hhdd.com"  # 预发环境

    get_book_list(htt=http)

    # story_list(htt=http)