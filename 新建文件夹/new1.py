# coding:utf-8
import requests
from bs4 import BeautifulSoup
import os


def one(url, href_index):
    # 获取首页的所有详情页的连接
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    channel = soup.find_all('a', attrs={'target': '_blank'})
    for i in channel:
        href = i.get('href')
        if '.html' in href:
            href_index.append(href)


def two(url, title, img_url, img_title):
    # 打开详情页，获取每个详情页的标题和图片的连接、标题
    # 留作文件夹名称用
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    channel = soup.select('#l > div.title > h1')
    channel1 = soup.select('#l > div.content-a > p > img')
    for a in channel:
        i_title = a.string
        title.append(str(i_title))
    for b in channel1:
        imgurl = b.get('src')
        imgtitle = b.get('title')
        img_url.append(imgurl)
        img_title.append(imgtitle)



def three(title, url, img_title):
    # 创建文件夹
    # 保存图片
    path = title
    if not os.path.exists(path):
        os.mkdir(path)
        print("'%s'" % title + ' 文件夹创建成功')

    else:
        print('"%s"' % title + " 文件夹已存在")

    img_path = os.getcwd() + '\\' + path + '\\' + img_title
    # print(img_path)
    if not os.path.exists(img_path):
        with open(img_path, 'wb')as f:
            f.write(requests.get(url).content)
            print("'%s'" % img_title + ' 图片写入成功')
    else:
        print("'%s'" % img_title + " 图片已存在")




if __name__ == '__main__':
    url = 'http://www.lanrentuku.com'  # 主链接
    href_index = []  # 详情页的连接
    one(url=url, href_index=href_index)
    # print(href_index)
    new_href_12 = href_index[0:12]  # 取详情页连接前12条
    # print(new_href_12)
    title = []
    img_url = []
    img_title = []
    for i in range(len(new_href_12)):
        two(url=url + str(new_href_12[i]), title=title, img_title=img_title, img_url=img_url)
        # print(title)

        three(title=str(title[i]), url=img_url[i], img_title=img_title[i])
        print('')
