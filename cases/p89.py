# coding: utf-8

'''
实例089：解码
**题目：**某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
'''


def encode(n):
    n = str(n)
    temp = []
    for i in n:
        temp.append((int(i) + 5) % 10)

    temp[0], temp[1], temp[2], temp[3] = temp[3], temp[2], temp[1], temp[0]

    return "".join('%s' %s for s in temp)

print(encode(1234))