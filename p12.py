# coding: utf-8

'''
实例012:100到200的素数
**题目：**判断101-200之间有多少个素数，并输出所有素数。

**程序分析：**判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
'''

def listPrime():

    count=0
    list =[]

    for i in range(101,200):
        for j in range(2,round(i**0.5)+1):
            if i%j==0:
                break
        else:
            count+=1
            list.append(i)

    return count,list

print(listPrime())
