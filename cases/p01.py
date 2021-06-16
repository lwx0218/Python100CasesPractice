# coding: utf-8

'''
实例001：数字组合
**题目：**有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

**程序分析：**遍历全部可能，把有重复的剃掉。
'''

import itertools

class combination():

    # tt as total

    def __init__(self,tt = 0):
        self.tt = tt

    def reg(self):
        for i in range(1,5):
            for j in range(1,5):
                for k in range(1,5):
                    if (i!=j) and (j!=k) and (k!=i):
                        print(i,j,k)
                        self.tt+=1
        return self.tt

    def simple(self):

        lt = [1,2,3,4]
        for i in itertools.permutations(lt,3):
            print(i)
            self.tt+=1
        return self.tt

if __name__ == "__main__":
    com = combination()
    # print(com.reg())
    print(com.simple())