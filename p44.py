# coding: utf-8

'''
实例044：矩阵相加
**题目：**计算两个矩阵相加。

**程序分析：**创建一个新的矩阵，使用 for 迭代并取出 X 和 Y 矩阵中对应位置的值，相加后放到新矩阵的对应位置中。
'''

import numpy as np

x = np.mat(np.arange(1,10).reshape(3,3))
y = np.mat(np.arange(11,20).reshape(3,3))
res = np.zeros((3,3),int)

for i in range(len(x)):
    for j in range(x.shape[1]):
        res[i,j] = x[i,j]+y[i,j]

print(res)
