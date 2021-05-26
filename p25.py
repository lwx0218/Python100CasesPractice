# coding: utf-8

'''
**题目：**求1+2!+3!+...+20!的和。

**程序分析：**1+2!+3!+...+20!=1+2(1+3(1+4(...20(1))))
'''

def factorialSum(n):
    res = 1
    for i in range(n,1,-1):
        res = i *res+1
    return res

print(factorialSum(20))

def factorial(n):
    return n*factorial(n-1) if n>1 else 1

def factorialSum2(n):
    res = 0
    for i in range(n):
        res+=factorial(i+1)
    return res
print(factorialSum2(20))