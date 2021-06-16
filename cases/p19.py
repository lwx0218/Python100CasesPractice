# coding: utf-8

'''
实例019：完数
**题目：**一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

**程序分析：**将每一对因子加进集合，在这个过程中已经自动去重。最后的结果要求不计算其本身。
'''

def fac(n):
    res = set()
    for i in range(1,n):
        if n%i==0:
            res.add(i)
            res.add(n/i)
    return res

def sumFac():
    for i in range(2,1001):
        if i ==sum(fac(i))-i:
            print(i)

sumFac()

