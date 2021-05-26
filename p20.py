# coding: utf-8

'''
实例020：高空抛物
**题目：**一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

**程序分析：**无
'''

def fallDown(n=100,c=10):

    res = n
    for i in range(c):
        n/=2
        res+=n

        if i + 1==c:
            print(n)
    print(res)

fallDown()