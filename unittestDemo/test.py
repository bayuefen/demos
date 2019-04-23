#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : bayuefen
# @File : test.py
# @Time : 2019-04-17 17:14
# @Desc :

import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        '''测试大写转换是否正确？'''
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        '''测试布尔断言？'''
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        '''测试异常抛出？'''
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
