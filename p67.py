# coding: utf-8

'''
实例067：交换位置
**题目：**输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
'''

import random as rd


def exchange(n):
    n[-1], n[n.index(min(n))] = n[n.index(min(n))], n[-1]
    ini = n[0]
    ma = n.index(max(n))
    n[0] = n[ma]
    n[ma]= ini
    return n


rd.seed(1)
n = rd.sample([i for i in range(10)], 10)
print(n)
print(exchange(n))
