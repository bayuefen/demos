#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : bayuefen
# @File : test.py
# @Time : 2019-04-17 16:22
# @Desc : test files

import configparser

config = configparser.ConfigParser()
config.read('./config.ini')
url = config.get('domain', 'url')
print(url)

