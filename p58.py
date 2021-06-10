# coding: utf-8

'''
实例058：画矩形
**题目：**画图，学用rectangle画方形。
'''
import tkinter as tk

root = tk.Tk()
root.title('Canvas')
canvas = tk.Canvas(width=800, height=600, bg='green')
canvas.pack(expand='yes', fill='both')

x0 = 263
y0 = 263
y1 = 275
x1 = 275
for i in range(19):
    canvas.create_rectangle(x0, y0, x1, y1)
    x0 -= 5
    y0 -= 5
    x1 += 5
    y1 += 5

canvas.pack()
root.mainloop()