# coding: utf-8

'''
实例046：打破循环
**题目：**求输入数字的平方，如果平方运算后小于 50 则退出。
'''


check = True
while check:
    n = input("please enter your number: ")
    if eval(n) ** 2<50:
        print("less than 50")
        check=False
