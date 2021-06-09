# coding: utf-8

'''
实例038：矩阵对角线之和
**题目：**求一个3*3矩阵主对角线元素之和。
'''

import numpy as np

def matSum():
    n = np.mat(np.arange(1,10).reshape(3,3))
    res = 0
    for i in range(len(n)):
        res += n[i,i]
    return res

print(matSum())