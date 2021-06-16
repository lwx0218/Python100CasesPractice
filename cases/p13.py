# coding: utf-8

'''
实例013：所有水仙花数
**题目：**打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

**程序分析：**利用for循环控制100-999个数，每个数分解出个位，十位，百位。
'''


def narcissus():
    lt = []

    for i in range(100, 1000):
        temp = str(i)
        one = eval(temp[-1])
        ten = eval(temp[-2])
        hun = eval(temp[-3])
        if one ** 3 + ten ** 3 + hun ** 3 == i:
            lt.append(i)
    return lt


print(narcissus())
