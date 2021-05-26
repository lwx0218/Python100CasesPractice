# coding: utf-8

'''
实例004：这天第几天
**题目：**输入某年某月某日，判断这一天是这一年的第几天？

**程序分析：**特殊情况，闰年时需考虑二月多加一天：
'''


def isLeapYear(year):
    return (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))


month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

out = 0
y = eval(input("year: "))
m = eval(input("month: "))
d = eval(input("day: "))

if isLeapYear(y):
    month[2]+1

for i in range(m):
    out+=month[i]

print(out+d)
