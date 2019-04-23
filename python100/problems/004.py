#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : bayuefen
# @File : 004.py
# @Time : 2019-04-23 15:18
# @Desc : 输入某年某月某日，判断这一天是这一年的第几天？
# 不使用三方库的情况下
import sys

year = int(input('请输入年份：\n'))
month = int(input('请输入月份：\n'))
day = int(input('请输入日期：\n'))
monthDays = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
leap = 0

if year < 0:
    print('年份需为正整数!')
    sys.exit()
if month < 1 or month > 12:
    print('月份需为1-12的正整数!')
    sys.exit()
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if day < 1 or day > 28 + leap:
    print('日期需为1-%d的正整数!' %(28+leap))
    sys.exit()
result = 0
if month > 2:
    result += leap
sumMonthTuple = monthDays[0: month - 1]
for days in sumMonthTuple:
    result += days
result += day
print(result)



