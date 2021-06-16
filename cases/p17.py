# coding: utf-8

'''
实例017：字符串构成
**题目：**输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

**程序分析：**利用 while 或 for 语句,条件为输入的字符不为 '\n'。
'''

def strFac(n):
    alp, spc, dig, oth = 0,0,0,0

    for i in n:
        if i.isspace():
            spc+=1
        elif i.isdigit():
            dig+=1
        elif i.isalpha():
            alp+=1
        else:
            oth+=1

    return alp,spc,dig,oth

print(strFac("meet your makers 123 *^$%^&*"))