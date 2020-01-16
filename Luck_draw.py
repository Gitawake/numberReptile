"""
//
//  numberReptile -> ssssfvvv
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
    window = tk.Tk()

    window.title('多功能抽奖系统')

    window.geometry('800x550')

    prize = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    pname = 1

    def one(self):
        # Ui.prize.clear()
        Ui.pname = 1
        first_page1 = tk.Frame(self.window)
        first_page1.pack()

        tk.Label(first_page1, text="请在下方填写参与抽奖的奖品名。").pack()

        first_page2 = tk.Frame(self.window)
        first_page2.pack()

        first_page3 = tk.Frame(self.window)
        first_page3.pack()

        tk.Label(first_page2, text='奖品{}:'.format(Ui.pname)).grid(row=1)

        e1 = tk.Entry(first_page2)
        e1.grid(row=1, column=1, padx=10, pady=5)

        def show():
            app_prize = e1.get()
            if app_prize != '':
                e1.delete(0, "end")
                Ui.prize.append(app_prize)
                Ui.pname = Ui.pname + 1
                tk.Label(first_page2, text='奖品{}:'.format(Ui.pname)).grid(row=1)

                tk.Label(first_page3, text="当前已添加的奖品列表：").grid(row=1, column=1, padx=10, pady=5)
                listb = tk.Listbox(first_page3)
                for i in Ui.prize:
                    listb.insert(0, i)
                listb.grid(row=2, column=1, padx=10, pady=5)
                tk.Button(first_page3, text="开始抽奖", width=10, command=show_1).grid(row=3, column=1, padx=10, pady=5)
            else:
                tk.messagebox.showerror('提示', '奖品不能为空哦~')

        tk.Button(first_page2, text="添加", width=5, command=show).grid(row=1, column=2)

        def show_1():
            if len(Ui.prize) > 1:
                first_page1.destroy()
                first_page2.destroy()
                first_page3.destroy()
                Ui.show1(self)
            else:
                tk.messagebox.showerror('提示', '参与抽奖的奖品不能少于2个哦~')

    def show1(self):
        second_pages = tk.Frame(self.window)
        second_pages.pack()

        second_pages1 = tk.Frame(self.window)
        second_pages1.pack()

        def ss():
            second_pages.destroy()
            second_pages1.destroy()
            ui.show1()

        def sss():
            second_pages.destroy()
            second_pages1.destroy()
            Ui.one(self)

        tk.Button(second_pages, text="重新抽奖", width=10, command=ss).pack()
        tk.Button(second_pages, text="重新设置奖品", width=10, command=sss).pack()

        vv = len(Ui.prize) / 4
        vv = math.ceil(vv) + 1

        t = -1
        for i in range(1, vv):
            for w in range(1, 5):
                t = t + 1
                if t < len(Ui.prize):
                    tk.Button(second_pages1, text=Ui.prize[t], width=10).grid(row=i, column=w, padx=10, pady=5)

        def round():
            extract = random.randint(1, len(Ui.prize))
            result = Ui.prize[extract - 1]

            kg = 8
            while kg != 0:
                kg = kg - 1
                vv1 = len(Ui.prize) / 4
                vv1 = math.ceil(vv1) + 1
                end = 0
                t1 = -1
                for i1 in range(1, vv1):
                    if end == 1:
                        break
                    for w1 in range(1, 5):
                        t1 = t1 + 1
                        if t1 < len(Ui.prize):
                            tk.Button(second_pages1, text=Ui.prize[t1], width=10, bg='red').grid(row=i1, column=w1, padx=10,
                                                                                          pady=5)
                            time.sleep(0.1)
                            if result == Ui.prize[t1] and kg == 0:
                                end = 1
                                break
                            tk.Button(second_pages1, text=Ui.prize[t1], width=10).grid(row=i1, column=w1, padx=10,
                                                                                       pady=5)

        t = threading.Thread(target=round)
        # 开启线程运行
        t.start()
        # 设置循环开始标志


if __name__ == '__main__':
    ui = Ui()
    ui.one()
    ui.window.mainloop()
