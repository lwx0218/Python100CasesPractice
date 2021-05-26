# coding: utf-8

'''
实例018：复读机相加
**题目：**求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

**程序分析：**用字符串解决。
'''

def repeater(n=2,factor=5):
    n = str(n)
    res = 0
    for i in range(factor):
        print("{}".format(n), end='')
        res+=int(n)
        n+=n[0]

        if i+1 == factor:
            break
        print("+",end='')

    print("={}".format(res))

repeater()

