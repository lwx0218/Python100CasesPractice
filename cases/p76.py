# coding: utf-8

'''
实例076：做函数
**题目：**编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
'''

def fun(n):

    res = 0

    if n%2 == 0:
        for i in range(2,n+1,2):
           res+=1/i
        return res
    else:
        for i in range(1, n+1, 2):
            res+=1/i
        return res

if __name__=='__main__':
    print(fun(50))