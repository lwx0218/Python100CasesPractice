# Python3 100 Cases
> Original website
>
> http://www.runoob.com/python/python-100-examples.html
>
> https://github.com/RichardFu123/Python100Cases/blob/master/Python100.md
>
> I rewrote 7 cases


#### Case 69
**题目：**有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

```
def countOff(n):
    num = [i for i in range(1, n + 1)]

    indicator = 1
    iloc = 0

    while len(num) >= 1:

        if iloc >= len(num):
            iloc = 0

        if indicator == 3:
            if len(num) == 1: break
            num.pop(iloc)
            indicator = 0
            iloc -= 1

        iloc += 1
        indicator += 1

    return num[0]
print(countOff(100))
```

#### Case 74
**题目：**列表排序及连接。
```
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
```

#### Case 76
**题目：**编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
```
def fun(n):

    res = 0

    if n%2 == 0:
        for i in range(2,n+1,2):
           res+=1/i
        return res
    else:
        for i in range(1, n+1, 2):
            res+=1/i
        return res

if __name__=='__main__':
    print(fun(50))
```



#### Case 78
**题目：**找到年龄最大的人，并输出。请找出程序中有什么问题。
```
person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}

print(
    list(person.keys())
    [list(person.values()).index(max(person.values()))]
)
```
#### Case 85
**题目：**输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
```
def divisibility(n):

    keep = True

    res = 1
    key = '9'
    while keep:
        if int(key) % n ==0:
            keep = False
        else:
            key+='9'
            res+=1
    return res, int(key), int(int(key)/n)

print(divisibility(13))
```
#### Case 88
**题目：**读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
```
import random as rd

def printStar(n):

    lt = sorted(rd.sample([i for i in range(1,51)],n))

    for i in lt:
        print('*'*i)

printStar(7)
```
#### Case 93
**题目：**时间函数举例3。
**Python 3.8 has abandoned the time.clock(), used the time.perf_counter() instead

```
import time

start = time.perf_counter()
for i in range(100):
    print(i)
end = time.perf_counter()
print('different is %6.3f' % (end - start))
```