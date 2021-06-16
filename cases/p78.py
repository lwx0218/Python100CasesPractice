# coding: utf-8

'''
实例078：字典
**题目：**找到年龄最大的人，并输出。请找出程序中有什么问题。
'''

person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}

print(
    list(person.keys())
    [list(person.values()).index(max(person.values()))]
)
