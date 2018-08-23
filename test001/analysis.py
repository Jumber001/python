#!/usr/bin/env python
# -*- coding:utf-8 -*-
# uthor:zhang time:2018/7/18
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
print(driver.page_source)
