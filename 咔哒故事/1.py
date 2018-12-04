# coding:utf-8

import requests
from bs4 import BeautifulSoup
import os
import urllib.request

"""
url = 'http://www.cnblogs.com/yoyoketang/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# channel = soup.find_all('div', attrs={'class': 'dayTitle'})
# for i in channel:
#     print(i.a.string)   # a是下一级的标签，打印这个标签的string值
# print(soup)

channel = soup.find_all('div', attrs={'class': 'postCon'})  # 找到其父类
for i in channel:
    print(i.div.contents)    # tag的 .contents 属性可以将tag的子节点以列表的方式输出

"""


def Get_Img_Index_Url(url, href_index):
    response = requests.get(url)
    # print(response.content)
    soup = BeautifulSoup(response.text, 'html.parser')
    channel = soup.find_all('a', attrs={"target": "_blank"})
    for i in channel:
        href = i.get('href')
        if 'html' in href:
            href_index.append(href)


def Get_Img_Index_Titile(url, new_title):
    # 获取标题
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.select('#l > div.title > h1')
    # print(title)
    for i in title:
        title_new = i.string
        # print(type(title_new))
        new_title.append(str(title_new))


def three(title):
    # 创建文件夹
    name = title
    if not os.path.exists(name):
        os.mkdir(name)
    else:
        print(name + '目录已存在')

def four(url, img_url, img_title):
    # 找到对应图片的地址和标题
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    channel = soup.select('#l > div.content-a > p > img')
    for i in channel:
        img_url1 = i.get('src')
        img_title1 = i.get('title')
        img_url.append(img_url1)
        img_title.append(img_title1)

def five(url, img_title):
    # img = urllib.request.urlopen(url)
    # path1 = img_title.
    urllib.request.urlretrieve(url, str(img_title))



if __name__ == '__main__':
    url = 'http://www.lanrentuku.com'
    # url_head = 'http://www.lanrentuku.com'
    href_index = []     # 详情页的连接
    title = []  # 文件夹名称
    # new_title = title_new
    Get_Img_Index_Url(url=url, href_index=href_index)
    # print(href_index)
    new_href = []       # 详情页的连接
    img_url = []    # 图片的连接
    img_title = []  # 图片的标题
    for i in range(len(href_index)):
        if i < 12:
            new_href.append(href_index[i])
    for i in range(len(new_href)):
        title_new = 'a'
        Get_Img_Index_Titile(url=url + str(href_index[i]), new_title=title)
        # print(title)
        # print(1)
        three(title=str(title[i]))
        # print(title[i])
        four(url=url + str(href_index[i]), img_url=img_url, img_title=img_title)
        # print(img_title[i], img_url[i])
        five(url=img_url[i], img_title=img_title[i])
