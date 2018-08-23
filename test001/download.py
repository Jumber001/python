#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zhang time:2018/7/18

# Python内置的HTTP请求库request、error、parse、robotparser
import urllib.request
import urllib.parse
# Python第三方请求库
import requests
import json
import pymongo


# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read())
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# response = requests.get("http://www.baidu.com")
# print(type(response.text), type(response.content))
# print(response.text)
# print(response.content)
# print(response.cookies)


# 获取链接
connect = pymongo.MongoClient("127.0.0.1", 27017)
# 获取数据库
db_Malcolm = connect.malcolm
# 获取表
collection = db_Malcolm.malcolm
collection.inventory.insert_one(
    {"item": "canvas",
     "qty": 100,
     "tags": ["cotton"],
     "size": {"h": 28, "w": 35.5, "uom": "cm"}})
