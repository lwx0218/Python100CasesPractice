# coding: utf-8

'''
实例068：旋转数列
**题目：**有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
'''

from collections import *

lt = [i for i in range(1,10)]

deq = deque(lt,maxlen=len(lt))
print(deq)
deq.rotate(int(3))
print(list(deq))