# coding: utf-8

'''
实例015：分数归档
**题目：**利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

**程序分析：**用条件判断即可。
'''

def grade(n):
    if n>=90:
        return 'A'
    elif 89>=n>=60:
        return 'B'
    else:
        return 'C'

print(grade(3))