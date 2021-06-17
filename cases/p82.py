# coding: utf-8

'''
实例082：八进制转十进制
**题目：**八进制转换为十进制
'''

print(int(input("please enter your number: "),8))

n=eval('0o'+str(int(input('八进制输入：'))))
print(n)