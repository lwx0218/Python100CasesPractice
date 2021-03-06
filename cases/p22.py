# coding: utf-8

'''
实例022：比赛对手
**题目：**两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

**程序分析：**找到条件下不重复的三个对手即可。
'''

def rival():

    a = set(['x','y','z'])
    b = set(['x','y','z'])
    c = set(['x','y','z'])

    a-=set(('x'))
    c-=set(('x','z'))

    for i in a:
        for j in b:
            for k in c:
                if len(set((i,j,k))) == 3:
                    print("a vs {}\nb vs {}\nc vs {}".format(i,j,k))

rival()