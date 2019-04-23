#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : bayuefen
# @File : test.py
# @Time : 2019-04-16 17:51
# @Desc : 基于requests lib的HTTP请求基本应用

import requests
import logging
import json
from requests.auth import AuthBase

domain = 'http://httpbin.org'

# GET
res = requests.get(domain + '/get', params={'aa': 1, 'bb': 2})
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
# # 可配置allow_redirects = False 禁用重定向
# res = requests.get(domain + '/redirect-to', params={'url':'https://www.baidu.com', 'status_code':302})
# print(res.url, res.status_code)
# print(res.history)

# # timeout
# # 超时的异常触发仅仅针对连接过程，与相应体的下载无关，即请求发起至服务器相应的最大时间，超过则以异常处理
# res = requests.get(domain + '/get', timeout=0.001)
# print(res.raise_for_status())


# # file upload
# # 超大文件的传输使用multipart/form-data，默认情况下requests是不支持的，需要使用requests-toolbelt
# file = {'txtFile': open('./test.txt', 'rb')}
# upload_data = {"parentId": "", "fileCategory": "personal", "fileSize": 179, "fileName": "test.txt", "uoType": 1}
# res = requests.post(domain + '/post', upload_data, files=file)
# print(res.url, res.status_code)
# print(res.json())

# # file download
# # notice: 下载原始相应内容（images/xlsx/pdf等），通过设置stream获取raw
# res = requests.get(domain + '/image/jpeg', stream=True)
# print(res.raw, res.raw.read(10))
# with open('./test.jpeg', 'wb') as f:
#     f.write(res.content)

# # Session (⭐️⭐️⭐️)
# # Notice: 1.Session对象能够跨请求保持某些特定参数，并且同一个Session实例发出的所有请求之间保持cookie
# # 2.对于同一个服务器发送多个请求，底层TCP连接可被重用，有显著的性能提升
# rs = requests.Session()
# rs.get(domain + '/cookies/set/username/bayuefen')
# res = rs.get(domain + '/cookies')
# print(res.text)

# # Cookie  (⭐️⭐️⭐️)
# cookies = dict(admin_token='xxxxxxxxx')
# res = requests.get(domain + '/cookies/set', cookies=cookies)
# print(res.text)
#
# # Cookie的返回对象是RequestsCookieJar，这种模式适用于跨域名跨路径使用
# jar = requests.cookies.RequestsCookieJar()
# jar.set('bayuefen_cookies', '123456', domain='httpbin.org', path='/cookies')
# jar.set('bayuefen_values', 'my_values', domain='httpbin.org', path='/elsewhere')
# res1 = requests.get(domain + '/cookies', cookies=jar)
# print(res1.text)

# # JSON解码器
# res = requests.post(domain + '/post', data={'aa': 11, 'bb': 2})
# print(res.raise_for_status(), res.status_code)
# # notice: JSON被解码返回成功，不一定代表HTTP相应成功；检查请求响应是否成功，需通过`response.raise_for_status()` or `response.status_code`去判别
# try:
#     res.json()
# except ValueError:
#     logging.error('No JSON object could be decoded')

# # 定制 headers
# # 定制headers低于特定场景的信息源
# # 1. 如果在 .netrc 中设置了用户认证信息，使用 headers= 设置的授权就不会生效。而如果设置了 auth= 参数，``.netrc`` 的设置就无效了。
# # 2. 如果被重定向到别的主机，授权 header 就会被删除。
# # 3. 代理授权 header 会被 URL 中提供的代理身份覆盖掉。
# # 4. 在我们能判断内容长度的情况下，header 的 Content-Length 会被改写。
# headers = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
# }
# res = requests.get(domain + '/get', headers=headers)
# print(res.json())
# # 相应头
# print(res.headers.get('content-type'))

# # SSL
# requests.get('https://github.com', verify=True)

# # 流式请求
# res = requests.get(domain + '/stream/20', stream=True)
# print(res.raw)
# if res.encoding is None:
#     res.encoding = 'utf-8'
# for line in res.iter_lines():
#     if line:
#         decoded_line = line.decode('utf-8')
#         print(json.loads(decoded_line))

# # Auth HTTP基本身份认证
# auth = requests.auth.HTTPBasicAuth('user', 'passwd')
# res = requests.get(domain + '/hidden-basic-auth/user/passwd', auth=auth)
# print(res.json())
