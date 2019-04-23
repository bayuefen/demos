#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : bayuefen
# @File : 003.py
# @Time : 2019-04-02 23:15

# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# x + 100 = m^2 , x + 268 = n^2
# => n^2 - m^2 = 168
# => (m+n)(m-n) = 168
# => 设i = m+n, j = m -n, 则i*j=168
# => m=(i+j)/2, n =(i-j)/2 得i,j均偶数