"""
//
//  numberReptile -> Luck_draw
//
//  Created by 苏相荣 on 2020/1/8 17:27.
//  Copyright © 2020 SuXiangRong. All rights reserved.
//
"""

import random
import threading
import tkinter as tk
import tkinter.messagebox
import time
import math


class Ui(object):
    """
    简单的抽奖系统
    """

    # 实例化Gui库
    window = tk.Tk()
    # 定义ui窗口标题
    window.title('多功能抽奖系统')
    # 定义ui窗口大小
    window.geometry('800x550')
    # 创建一个参与抽奖的列表
    prize = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # 定义变量用于显示当前添加的是第几个奖品
    current = 1

    def prize_setting(self):
        """
        添加奖品列表页面
        :return:
        """
        # 开始之前先重置奖品列表为空
        Ui.prize.clear()
        # 重置当前添加的奖品是第几个为1
        Ui.current = 1
        # 创建一个frame用于放置按钮
        first_pagenter_prizes = tk.Frame(self.window)
        # 定义frame排列方式
        first_pagenter_prizes.pack()
        # 定义一个label用于显示顶部标题
        tk.Label(first_pagenter_prizes, text="请在下方填写参与抽奖的奖品名。").pack()
        # 创建一个frame用于放置按钮
        first_page2 = tk.Frame(self.window)
        # 定义frame排列方式
        first_page2.pack()
        # 创建一个frame用于放置按钮
        first_page3 = tk.Frame(self.window)
        # 定义frame排列方式
        first_page3.pack()
        # 定义一个label用于显示输入栏名字
        tk.Label(first_page2, text='奖品{}:'.format(Ui.current)).grid(row=1)
        # 定义一个entry用于输入奖品
        enter_prizes = tk.Entry(first_page2)
        # 定义entry排列方式
        enter_prizes.grid(row=1, column=1, padx=10, pady=5)

        def show():
            """
            定义奖品添加函数
            :return:
            """
            # 获取输入框的值用于储存到列表
            app_prize = enter_prizes.get()
            # 判断输入框内是否不为空
            if app_prize != '':
                # 清空输入框
                enter_prizes.delete(0, "end")
                # 把获取到的内容储存到奖品列表
                Ui.prize.append(app_prize)
                # 当前添加的奖品是第几个加1
                Ui.current = Ui.current + 1
                # 重新渲染奖品名字得到最新当前是第几个
                tk.Label(first_page2, text='奖品{}:'.format(Ui.current)).grid(row=1)
                # 渲染当前已添加到列表的奖品列表标题
                tk.Label(first_page3, text="当前已添加的奖品列表：").grid(row=1, column=1, padx=10, pady=5)
                # 开始渲染当前已添加的奖品列表
                listb = tk.Listbox(first_page3)
                # 循环取出奖品列表
                for i in Ui.prize:
                    # 从第一个开始取，取完内所有值
                    listb.insert(0, i)
                # 定义listb样式
                listb.grid(row=2, column=1, padx=10, pady=5)
                # 定义开始抽奖按钮
                tk.Button(first_page3, text="开始抽奖", width=10, command=get_set).grid(row=3, column=1, padx=10, pady=5)
            # 输入框为空时
            else:
                # 弹窗提示
                tk.messagebox.showerror('提示', '奖品不能为空哦~')
        # 定义添加按钮触发show函数
        tk.Button(first_page2, text="添加", width=5, command=show).grid(row=1, column=2)

        def get_set():
            """
            准备开始抽奖
            :return:
            """
            # 判断奖品列表不少于两个奖项
            if len(Ui.prize) > 1:
                # 先销毁界面布局
                first_pagenter_prizes.destroy()
                first_page2.destroy()
                first_page3.destroy()
                # 调用抽奖页面函数
                Ui.start_raffle(self)
            # 如果奖品少于两个
            else:
                # 提示奖品不能少于两个
                tk.messagebox.showerror('提示', '参与抽奖的奖品不能少于2个哦~')

    def start_raffle(self):
        """
        定义抽奖页面
        :return:
        """
        # 创建一个frame用于放置顶部按钮
        second_pages = tk.Frame(self.window)
        # 定义frame排列方式
        second_pages.pack()
        # 创建一个frame用于放置转盘
        second_pages1 = tk.Frame(self.window)
        # 定义frame排列方式
        second_pages1.pack()

        def restart():
            """
            定义重新抽奖函数
            :return:
            """
            # 先销毁界面布局
            second_pages.destroy()
            second_pages1.destroy()
            # 调用抽奖函数
            ui.start_raffle()

        def reset():
            """
            定义重新设置奖品函数
            :return:
            """
            # 先销毁界面布局
            second_pages.destroy()
            second_pages1.destroy()
            # 调用奖品设置函数
            Ui.prize_setting(self)
        # 创建重新开始抽奖按钮
        tk.Button(second_pages, text="重新抽奖", width=10, command=restart).pack()
        # 创建重新设置奖品按钮
        tk.Button(second_pages, text="重新设置奖品", width=10, command=reset).pack()
        # 定义变量结算出转盘有多少列
        column_number = len(Ui.prize) / 4
        # 把得到的列向上取整
        column_number = math.ceil(column_number)
        # 定义一个变量用于获取奖品列表的奖项名
        get_prizes = -1
        # 循环放置转盘的列
        for row in range(1, column_number + 1):
            # 循环放置转盘的行
            for column in range(1, 5):
                # 定义自增用于获取整个列表的奖项名
                get_prizes = get_prizes + 1
                # 判断获取的自增函数小于奖品列表的总数
                if get_prizes < len(Ui.prize):
                    # 循环放置奖品
                    tk.Button(second_pages1, text=Ui.prize[get_prizes], width=10).grid(row=row, column=column, padx=10, pady=5)

        def turntable():
            """
            定义转动效果函数
            :return:
            """
            # 定义返回一个随机1-奖品列表总数的整数
            extract = random.randint(1, len(Ui.prize))
            # 按照随机数获取对应的奖品
            result = Ui.prize[extract - 1]
            # 定义抽奖转动的轮数
            turn_around = 8
            # 循环轮数当轮数不等于0的时候一直循环
            while turn_around != 0:
                # 每轮减少轮数1
                turn_around = turn_around - 1
                # 定义一个结束标记变量
                end = False
                # 定义一个变量用于获取奖品列表的奖项名
                get_prizes1 = -1
                # 循环转盘的列
                for row1 in range(1, column_number + 1):
                    # 判断结束标记是否True
                    if end:
                        # 结束循环
                        break
                    # 循环转盘的行
                    for column1 in range(1, 5):
                        # 定义自增用于获取整个列表的奖项名
                        get_prizes1 = get_prizes1 + 1
                        # 判断获取的自增函数小于奖品列表的总数
                        if get_prizes1 < len(Ui.prize):
                            # 循环改变转盘奖品颜色
                            red_button = tk.Button(second_pages1, text=Ui.prize[get_prizes1], width=10, bg='red')
                            # 定义变颜色按钮的位置
                            red_button.grid(row=row1, column=column1, padx=10, pady=5)
                            # 暂停0.1秒
                            time.sleep(0.1)
                            # 判断如果轮数等于0并且当前变色的按钮和随机数对应
                            if turn_around == 0 and result == Ui.prize[get_prizes1]:
                                # 重置结束标志变量
                                end = True
                                # 结束循环
                                break
                            # 上面条件不满足
                            else:
                                # 重置按钮颜色
                                white_button = tk.Button(second_pages1, text=Ui.prize[get_prizes1], width=10)
                                white_button.grid(row=row1, column=column1, padx=10, pady=5)
        # 定义一个线程用于变成效果
        discoloration = threading.Thread(target=turntable)
        # 运行线程
        discoloration.start()


# 定义程序入口
if __name__ == '__main__':
    # 实例化类
    ui = Ui()
    # 运行函数
    ui.prize_setting()
    # 循环窗口消息
    ui.window.mainloop()
