# coding: utf-8

'''
实例040：逆序列表
**题目：**将一个数组逆序输出。

**程序分析：**依次交换位置，或者直接调用reverse方法。
'''

def revLt():
    lt = [10**i for i in range(5)]
    lt.reverse()
    return lt

print(revLt())