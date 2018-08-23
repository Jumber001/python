#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zhang time:2018/7/19
import requests


response = requests.get('http://www.baidu.com')
# print(response.text)
print(response.headers)
# print(response.status_code)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
response = requests.get('https://passport.baidu.com/static/passpc-account/img/reg/upreg.png', headers=headers)
print(response.status_code)

print(response.content)
with open('.png', 'wb') as f:
    f.write(response.content)
    f.close()
