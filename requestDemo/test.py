#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : bayuefen
# @File : test.py
# @Time : 2019-04-16 17:51
# @Desc : 基于requests lib的HTTP请求基本应用

import requests

domain = 'http://httpbin.org'

# GET
res = requests.get(domain+'/get', params={'aa':1,'bb':2})
print(res.status_code, res.text)
print(res.url, res.json())

# # POST
# res = requests.post(domain + '/post', params={'aa': 11, 'bb': 22}, data={'username': 'bayuefen', 'password': '123456'})
# print(res.status_code, res.text)
# print(res.url, res.json())

# # PATCH
# res = requests.patch(domain + '/patch', data={'username':'bayuefen','password':'123456','visibility':'private'})
# print(res.status_code, res.text)
# print(res.headers)

# # DELETE
# res = requests.delete(domain + '/delete')
# print(res.status_code, res.text)
# print(res.headers)

# # redirect
# res = requests.get(domain + '/redirect-to', params={'url':'https://www.baidu.com', 'status_code':302})
# print(res.url, res.status_code)
# print(res.history)

# # file upload
# file = {'txtFile': open('./test.txt', 'rb')}
# upload_data = {"parentId": "", "fileCategory": "personal", "fileSize": 179, "fileName": "test.txt", "uoType": 1}
# res = requests.post(domain + '/post', upload_data, files=file)
# print(res.url, res.status_code)
# print(res.json())

# # file download
# res = requests.get(domain + '/image/jpeg', stream=True)
# with open('./test.jpeg', 'wb') as f:
#     f.write(res.content)

# # Session
# session = requests.Session()
# session.auth = ('username', 'password')
# res1 = requests.get(domain + '/get')
# print(res1.status_code)
# print(res1.text)

# # Cookie
# cookies = dict(admin_token='xxxxxxxxx')
# res = requests.get(domain + '/cookies/set', cookies=cookies)
# print(res.text)
#
# jar = requests.cookies.RequestsCookieJar()
# jar.set('bayuefen_cookies', '123456', domain='httpbin.org', path='/cookies')
# jar.set('bayuefen_values', 'my_values', domain='httpbin.org', path='/elsewhere')
# res1 = requests.get(domain + '/cookies', cookies=jar)
# print(res1.text)
