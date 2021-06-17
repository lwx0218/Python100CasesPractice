# coding: utf-8

'''
实例083：制作奇数
**题目：**求0—7所能组成的奇数个数。

程序分析：

组成1位数是4个。1,3,5,7结尾

组成2位数是7*4个。第一位不能为0

组成3位数是784个。中间随意

组成4位数是788*4个。
'''

def makeOdd():
    sum = 4
    s = 4
    for i in range(2,9):
        print(sum)
        if i<=2:
             s*=7
        else:
            s*=8
        sum+=s
    print('sum = %d' % sum)

makeOdd()
