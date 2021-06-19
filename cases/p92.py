# coding: utf-8

'''
实例092：time模块II
**题目：**时间函数举例2。
'''
import time

start = time.time()
for i in range(3000):
    print(i)
end = time.time()

print(end - start)