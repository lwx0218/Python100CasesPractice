# coding: utf-8

'''
实例007：copy
**题目：**将一个列表的数据复制到另一个列表中。

**程序分析：**使用列表[:]，拿不准可以调用copy模块。
'''

import copy

a = [1, 2, 3, 4, ['a', 'b', 'c']]

b = a
c = a[:]  # shallow copy
d = copy.copy(a)  # shallow copy
e = copy.deepcopy(a)  # deep copy

a.append(3)
a[4].append('f')

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
print('e = ', e)
