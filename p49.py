# coding: utf-8

'''
实例049：lambda
**题目：**使用lambda来创建匿名函数。
'''

Max = lambda x,y : x*(x>=y) + y*(y>=x)
Min = lambda x,y : x*(x<=y)+y*(y<=x)


print(Max(1,2))
print(Min(1,2))