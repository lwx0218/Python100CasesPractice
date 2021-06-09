# coding: utf-8

'''
实例033：列表转字符串
**题目：**按逗号分隔列表。
'''

def list2Str(n):
    return ','.join(str(i) for i in n)

n = list(range(10))

print(list2Str(n))