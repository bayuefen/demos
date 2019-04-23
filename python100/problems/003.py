#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : bayuefen
# @File : 003.py
# @Time : 2019-04-02 23:15
# @Desc : 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

n = 0
while (n + 1)**2 - n * n <= 168:
    n += 1
for i in range((n + 1)**2):
    if i**0.5 == int(i**0.5)and (i + 168)**0.5 == int((i + 168)**0.5):
        print(i - 100)