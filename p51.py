# coding: utf-8

'''
实例051：按位与
**题目：**学习使用按位与 & 。

**程序分析：**0&0=0; 0&1=0; 1&0=0; 1&1=1。
'''

# the Nor gate

a=0o77
print(a)
b=a&5
print(b)
b=b&7
print(b)