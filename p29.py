# coding: utf-8

'''
实例029：反向输出
**题目：**给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

**程序分析：**学会分解出每一位数,用字符串的方法总是比较省事。
'''

def revO(n):
    n = str(n)
    print(len(n))
    print(n[::-1])

revO(12345)