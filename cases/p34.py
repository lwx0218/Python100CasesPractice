# coding: utf-8

'''
实例034：调用函数
**题目：**练习函数调用。
'''

def hi():
    print("Hi there")

def hiAg():
    for i in range(2):
        hi()

if __name__=="__main__":
    hiAg()