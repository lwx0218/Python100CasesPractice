# coding: utf-8

'''
实例036：算素数
**题目：**求100之内的素数。
'''

def prime(n):

    primelt = []

    for i in range(n):
        if i > 1:
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                primelt.append(i)
    return primelt

print(prime(100))