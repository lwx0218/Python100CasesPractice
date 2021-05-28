# coding: utf-8

'''
实例030：回文数
**题目：**一个5位数，判断它是不是回文数。
即12321是回文数，个位与万位相同，十位与千位相同。

**程序分析：**用字符串比较方便,就算输入的不是数字都ok。
'''

def palindrome(n):
    n = str(n)
    head, tail = 0,len(n)-1

    flag = True

    while head < tail:
        if n[head] != n[tail]:
            return "Not a palindrome"
            flag = False
            break
        head,tail = head+1,tail-1
    if flag:
        return "It's a palindrome"

print(palindrome(12321))