# coding: utf-8

'''
实例024：斐波那契数列II
**题目：**有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

**程序分析：**就是斐波那契数列的后一项除以前一项。
'''

def sumFib(n):
    a,b =1,1
    s = 0
    for i in range(n):
        s+=b/a
        a,b=b,a+b
    return s

print(sumFib(2))

def fib(n):
    return 1 if n<=2 else fib(n-1)+fib(n-2)

def sumFib2(n):
    t = 0
    for i in range(n):
        t += fib(n+1)/fib(n)
    return t
print(sumFib2(2))
