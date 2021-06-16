# coding: utf-8

'''
实例037：排序
**题目：**对10个数进行排序。

**程序分析：**同实例005
'''

import random as rd

def qSort(n):
    if len(n)<2:
        return n
    else:
        pivot = n[0]
        less = [i for i in n[1:] if i <= pivot]
        greater = [i for i in n[1:] if i>pivot]
        return qSort(less) + [pivot] + qSort(greater)

if __name__ == '__main__':
    n = 10
    lt = rd.sample([i for i in range(n)], n)
    print(lt)
    print(qSort(lt))