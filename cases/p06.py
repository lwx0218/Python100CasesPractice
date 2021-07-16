# coding: utf-8

'''
实例006：斐波那契数列
**题目：**斐波那契数列。

**程序分析：**斐波那契数列（Fibonacci sequence），从1,1开始，后面每一项等于前面两项之和。图方便就递归实现，图性能就用循环。
'''
from functools import lru_cache

@lru_cache()
def fib(n):
    return 1 if n <= 2 else fib(n - 1) + fib(n - 2)

@lru_cache()
def fib2(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a

print(fib(100),fib2(100))
