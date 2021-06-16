# coding: utf-8

'''
实例066：三数排序
**题目：**输入3个数a,b,c，按大小顺序输出。　　　

**程序分析：**同实例005。
'''
import random as rd
def selectSort(n):
    for i in range(len(n)):
        for j in range(i,len(n)):
            if n[i]>=n[j]:
                n[i],n[j]=n[j],n[i]

    return n

if __name__=='__main__':
    rd.seed(1)
    n = rd.sample([i for i in range(10)],10)
    print("original list: ",n)
    print("sorted list: {}".format(selectSort(n)))