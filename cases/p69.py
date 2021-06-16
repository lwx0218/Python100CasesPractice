# coding: utf-8

'''
实例069：报数
**题目：**有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
'''


def countOff(n):
    num = [i for i in range(1, n + 1)]

    indicator = 1
    iloc = 0

    while len(num) >= 1:

        if iloc >= len(num):
            iloc = 0

        if indicator == 3:
            if len(num) == 1: break
            num.pop(iloc)
            indicator = 0
            iloc -= 1

        iloc += 1
        indicator += 1

    return num[0]


print(countOff(100))
