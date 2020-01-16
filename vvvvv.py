"""
//
//  numberReptile -> vvvvv
//
//  Created by 苏相荣 on 2020/1/14 15:54.
//  Copyright © 2020 SuXiangRong. All rights reserved.
//
"""
import tkinter
# 导入线程模块
import threading
import time

root = tkinter.Tk()
root.title('转盘抽奖')
root.minsize(290,370)


# 摆放按钮
btn1 = tkinter.Button(root, text = '蓝牙耳机', bg = 'red')
btn1.place(x = 20, y = 20, width = 70, height = 70)

btn2 = tkinter.Button(root, text = '再来一次', bg = 'white')
btn2.place(x = 110, y = 20, width = 70, height = 70)

btn3 = tkinter.Button(root, text = '抱枕', bg = 'white')
btn3.place(x = 200, y = 20, width = 70, height = 70)

btn4 = tkinter.Button(root, text = '谢谢惠顾', bg = 'white')
btn4.place(x = 20, y = 110, width = 70, height = 70)

btn5 = tkinter.Button(root, text = '保温杯', bg = 'white')
btn5.place(x = 200, y = 110, width = 70, height = 70)

btn6 = tkinter.Button(root, text = '充电宝', bg = 'white')
btn6.place(x = 20, y = 200, width = 70, height = 70)

btn7 = tkinter.Button(root, text = 'iphoneX', bg = 'white')
btn7.place(x = 110, y = 200, width = 70, height = 70)

btn8 = tkinter.Button(root, text = '谢谢惠顾', bg = 'white')
btn8.place(x = 200, y = 200, width = 70, height = 70)

# 将所有选项组成列表
prizelists = [btn1,btn2,btn3,btn5,btn8,btn7,btn6,btn4]

# 是否开启循环的标志
isloop = False
# 是否运行的标志
functions = False

def round():
    # 判断是否开始循环（防止多次按下开始按钮程序开启多次转盘循环）
    if isloop == True:
        return

    # 初始化计数变量
    i = 0
    while True:
        # 延时操作
        time.sleep(0.06)
        # 将所有组件的背景颜色变为白色
        for j in prizelists:
            j['bg'] = 'white'
        # 将当前数值对应的组件变色
        prizelists[i]['bg'] = 'red'

        i += 1
        # 如果i大于最大索引直接归零
        if i >= len(prizelists):
            i = 0
        if functions == True:
            continue
        else:
            break

# 建立一个新线程的函数
def newtask():
    global isloop
    global functions
    # 建立线程
    t = threading.Thread(target = round)
    # 开启线程运行
    t.start()
    # 设置循环开始标志
    isloop = True
    # 是否运行的标志
    functions = True

# 定义停止循环的函数
def stop():
    global isloop
    global functions

    functions = False
    isloop = False

# 开始按钮
btn_start = tkinter.Button(root, text = '开始', command = newtask)
btn_start.place(x = 80, y = 300, width = 50, height = 50)

# 结束按钮

btn_stop = tkinter.Button(root, text = '结束', command = stop)
btn_stop.place(x = 150, y = 300, width = 50, height = 50)

root.mainloop()