# coding:utf-8

import requests
from bs4 import BeautifulSoup
import os


def Get_index_url(url):
    """找到当前页所有可用地址"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    channel = soup.find_all('a')  # 找到对应地址
    for i in channel:
        index_url = i.get()


def Get_page_num(url, page_url):
    """找到有多少页"""
    """或者自己规定多少页"""
    response = requests.get(url)  # 先进入首页
    soup = BeautifulSoup(response.text, 'html.parser')
    channel = soup.find('a')  # 找到页码的标签
    for i in channel:
        page = i.get()
        page_url.append(page)


def Get_index_tile(url, page_title):
    """获取标题"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    channel = soup.find('a')    # 找到标题
    for i in channel:
        title = i.get()
        page_title.append(title)

