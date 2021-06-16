# coding: utf-8

'''
实例071：输入和输出
**题目：**编写input()和output()函数输入，输出5个学生的数据记录。
'''



def input_stu(n):
    for i in range(3):
        n[i][0] = input("please enter the student's number: \n")
        n[i][1] = input("please enter the student's name: \n")
        for j in range(3):
            n[i][2].append(eval(input("score: \n")))

def output_stu(n):
    for i in range(3):
        print("%-6s%-10s" % (n[i][0],n[i][1]))
        for j in range(3):
            print("%-8d%" % (n[i][2][j]))

if __name__  == "__main__":
    student = []
    for i in range(5):
        student.append(['', '', []])

    input_stu(student)
    print(student)
    output_stu(student)