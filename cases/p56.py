# coding: utf-8

'''
实例056：画圈
**题目：**画图，学用circle画圆形。　　　

**程序分析：**无。
'''

import tkinter as tk

canvas = tk.Canvas(width = 800,height = 600, bg = 'green')
canvas.pack(expand="YES",fill="both")
k=1
j=1
for i in range(26):
    canvas.create_oval(310-k,250-k,310+k,250+k,width=1)
    k+=j
    j+=0.3
tk.mainloop()