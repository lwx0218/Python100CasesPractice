# coding: utf-8

'''
实例035：设置输出颜色
**题目：**文本颜色设置。
'''

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(colors.WARNING + "警告的颜色字体?" + colors.ENDC)
print(colors.FAIL + "警告的颜色字体?" + colors.ENDC)