# coding: utf-8

'''
实例042：变量作用域
**题目：**学习使用auto定义变量的用法。

**程序分析：**python中的变量作用域。
'''

i = 0
n = 0

def dummy():
    i = 0
    print(i)
    i+=1

def dummy2():
    global n
    print(n)
    n+=1

# for j in range(20):
#     print(i)
#     dummy()
#     i+=1

for k in range(2):
    print(n)
    dummy2()
    n+=10
