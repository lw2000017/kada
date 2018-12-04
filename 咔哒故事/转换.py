# f = open('11.txt', 'r')
# coding:utf-8
# 读取文件
with open('11.txt') as f1:
    list = f1.readlines()
for i in range(0, len(list)):
    list[i] = list[i].rstrip('\n')  # 去掉换行符

list1 = []

for i in list:
    list1.append(int(i))  # 把列表中的str转换为int
print(list1)

# with open('story2_getStoryList1.json', encoding='utf-8') as f:
#     string = f.read()
#     # print(string)
# import re
# storyId = re.findall(r'"storyId":(/d)', string)
# print(storyId)

# import hashlib
# import base64
#
# md5 = hashlib.md5()
#
# md5.update('get'.encode(encoding='utf-8'))  # method
# md5.update('\n'.encode(encoding='utf-8'))
# md5.update('*/*'.encode(encoding='utf-8'))  # accept
# md5.update('\n'.encode(encoding='utf-8'))
# # md5.update(''.encode(encoding='utf-8'))  # bodyMd5
# # md5.update('\n'.encode(encoding='utf-8'))
# # md5.update(''.encode(encoding='utf-8'))  # content_type
# # md5.update('\n'.encode(encoding='utf-8'))
# md5.update('Fri 2 Nov 2018 08:44:54 GMT'.encode(encoding='utf-8'))  # date
# md5.update('\n'.encode(encoding='utf-8'))
# md5.update('DT=MI 6;SV=8.0.0;AV=3.8.0;CH=debugpackage'.encode(encoding='utf-8'))  # rdi
# md5.update('\n'.encode(encoding='utf-8'))
# md5.update('GET /book2/otherCollectList.json?pagingSize=60&pagingNumber=1'.encode(encoding='utf-8'))  # pathurl
# # md5.update(b'1')
# md5_md5 = md5.hexdigest()
# # print(md5_md5)
# h1 = base64.b64encode(md5_md5.encode(encoding='utf-8'))
# h1_str = str(h1, 'utf-8')
# print(h1_str)