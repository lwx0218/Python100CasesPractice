# coding: utf-8

'''
实例016：输出日期
**题目：**输出指定格式的日期。

**程序分析：**使用 datetime 模块。
'''

import datetime

def date():
    print(datetime.date.today())
    print(datetime.date(2333,3,3))
    print(datetime.date.today().strftime('%Y_%m_%d'))
    print(datetime.date(2021,2,3).replace(year=datetime.date(2021,2,3).year+22))

date()