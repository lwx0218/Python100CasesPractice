# coding: utf-8

'''
实例085：整除
**题目：**输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
'''

def divisibility(n):

    keep = True

    res = 1
    key = '9'
    while keep:
        if int(key) % n ==0:
            keep = False
        else:
            key+='9'
            res+=1
    return res, int(key), int(int(key)/n)

print(divisibility(13))
