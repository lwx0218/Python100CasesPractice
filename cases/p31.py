# coding: utf-8

'''
实例031：字母识词
**题目：**请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

**程序分析：**这里用字典的形式直接将对照关系存好。
'''


weekT = {'u':'Tuesday','t':'Thursday'}
weekS = {'a':'Saturday', 'u':'Sunday'}

week = {'m':'Monday','w':'Wednesday','f':'Friday','t':weekT,'s':weekS}

n = week[str(input("please enter the first letter: ")).lower()]

if n == weekT or n ==weekS:
    print(n[str(input("please enter the second the letter: ")).lower()])
else:
    print(n)

