# coding: utf-8

'''
实例023：画菱形
**题目：**打印出如下图案（菱形）:

    *    ***   *****  *******   *****    ***     *

**程序分析：**递归调用即可。
'''

def drawRhombus(n):
    a = "*"*(2*(4-n)+1)
    print(a.center(9,' '),end='')
    if n!=1:
        drawRhombus(n-1)
        print(a.center(9,' '),end="")

drawRhombus(4)