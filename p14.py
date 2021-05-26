# coding: utf-8

'''
实例014：分解质因数
**题目：**将一个整数分解质因数。例如：输入90,打印出90=233*5。

**程序分析：**根本不需要判断是否是质数，从2开始向数本身遍历，能整除的肯定是最小的质数。
'''

def factories(n):

    print(n,'= ',end='')

    if n <=0:
        n = abs(n)
        print('-1x',end='')

    ind = 0
    if n<=1:
        print(n)
        ind = 1

    while True:
        if ind:
            break
        for i in range(2,round(n+1)):
            if n%i==0:
                print("{}".format(i),end='')
                if n == i:
                    ind = 1;
                    break
                print('x',end = '')
                n/=i
                break

factories(6)
