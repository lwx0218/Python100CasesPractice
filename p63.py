# coding: utf-8

'''
实例063：画椭圆
**题目：**画椭圆
'''

import tkinter as tk

x = 360
y = 160
top = y - 30
bottom = y - 30

canvas = tk.Canvas(width=400, height=600, bg='white')
for i in range(10):
    canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
    top -= 5
    bottom += 5
canvas.pack()
tk.mainloop()