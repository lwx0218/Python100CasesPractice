# coding: utf-8

'''
实例045：求和
**题目：**统计 1 到 100 之和。

**程序分析：**无
'''

def sum100(n):
    res = 0
    for i in range(1,n+1):
        res+=i
    return res

print(sum100(100))