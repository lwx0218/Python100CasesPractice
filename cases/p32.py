# coding: utf-8

'''
实例032：反向输出II
**题目：**按相反的顺序输出列表的值。

**程序分析：**无。
'''

def revOut(n):
    return n[::-1]

n = list(range(10))

print(n)
print(revOut(n))