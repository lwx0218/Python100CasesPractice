# coding: utf-8

'''
实例074：列表排序、连接
**题目：**列表排序及连接。

**程序分析：**排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。
'''
import random as rd
def listMod():
    rd.seed(1)
    lt1 = rd.sample([i for i in range(10,50)],4)
    lt2 = [i for i in range(4)]

    # link:
    lt1.extend(lt2)

    # sort:
    lt1.sort()
    return lt1

if __name__ == '__main__':
    print(listMod())