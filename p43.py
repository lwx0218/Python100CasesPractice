# coding: utf-8

'''
实例043：作用域、类的方法与变量
**题目：**模仿静态变量(static)另一案例。

**程序分析：**综合实例041和实例042。
'''

class dummy:
    n = 1
    def num(self):
        print('class dummy: ',self.n)
        print('global dummy:',n)
        self.n+=1

d = dummy()
n = 1
for i in range(5):
    n*=10
    d.num()