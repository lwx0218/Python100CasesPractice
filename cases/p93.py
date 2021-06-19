# coding: utf-8

'''
实例093：time模块III
**题目：**时间函数举例3。
'''
import time

start = time.perf_counter()
for i in range(100):
    print(i)
end = time.perf_counter()
print('different is %6.3f' % (end - start))