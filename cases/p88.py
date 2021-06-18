# coding: utf-8

'''
实例088：打印星号
**题目：**读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
'''

import random as rd

def printStar(n):

    lt = sorted(rd.sample([i for i in range(1,51)],n))

    for i in lt:
        print('*'*i)

printStar(7)