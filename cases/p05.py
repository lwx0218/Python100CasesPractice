# coding: utf-8

'''
实例005：三数排序
**题目：**输入三个整数x,y,z，请把这三个数由小到大输出。

**程序分析：**练练手就随便找个排序算法实现一下，偷懒就直接调函数。
'''

lt = []

for i in range(3):
    lt.append(eval(input("please enter the number")))

for i in range(len(i)):
    for j in range(i, len(i)):
        if lt[i] > lt[j]:
            lt[i], lt[j] = lt[j], lt[i]


lt.sort()
sorted(lt)
