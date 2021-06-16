# coding: utf-8

'''
实例061：杨辉三角
**题目：**打印出杨辉三角形前十行。
'''


def yangsTri(n):
    r = [[1]]
    for i in range(1, n):
        r.append(list(map(lambda x, y: x + y, [0] + r[-1], r[-1] + [0])))
    return r


for i in yangsTri(10):
    print(i)
