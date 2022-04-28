# -*- coding: utf-8 -*-
"""
@Time: 2022/4/27 20:53 
@Author: Marigold
@Version: 0.0.0
@Description：
@WeChat Account: Marigold
"""
from tkinter import *
from tkinter.messagebox import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from model.ConnDB import *
from model.user import *
from view.mainpage import MainPage
from view.dataEntryForm import DataEntryForm

class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (500, 350))  # 设置窗口大小
        # self.root.minsize(500, 350)
        # self.root.maxsize(500, 350)
        self.root.title('登录')
        self.username = StringVar()
        self.password = StringVar()
        self.page = Frame(self.root)  # 创建Frame
        self.createPage()

    def createPage(self):
        self.page.pack()
        ttk.Label(self.page, text="疫情医疗信息管理系统", font='SimSun 25 bold').grid(row=0, stick=W+E, pady=40, columnspan=2)
        ttk.Label(self.page, text='用户名: ', font='SimSun -14').grid(row=1, sticky=E, pady=10)
        ttk.Entry(self.page, textvariable=self.username).grid(row=1, column=1, sticky=W)
        ttk.Label(self.page, text='密  码: ', font='SimSun -14').grid(row=2, sticky=E, pady=10)
        ttk.Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, sticky=W)
        ttk.Button(self.page, text='登录', width=30, command=self.loginCheck, bootstyle="primary-outline").grid(row=3, column=0,
                                                                                                columnspan=2, pady=20)

    def loginCheck(self):
        global user
        name = self.username.get()
        secret = self.password.get()
        if name:
            ms = ConnDB()
            sql = "select * from myUser where is_deleted=0 and username=%s"
            result = ms.ExecQuery(sql, (name,))
            if len(result):
                item = result[0]
                user = User(item['user_id'], item['username'], item['password'], item['is_deleted'])
                if secret:
                    if secret == user.password:
                        f = open('user.txt', 'w', encoding='utf-8')
                        f.truncate()
                        f.write(user.get_username())
                        f.close()
                        self.page.destroy()
                        MainPage(self.root)
                        # DataEntryForm(self.root)
                    else:
                        showinfo(title='提示', message='账号或密码错误！')
                else:
                    showinfo(title='提示', message='请输入密码！')
            else:
                showinfo(title="提示", message="用户不存在！")
            ms.close()

        else:
            showinfo(title='提示', message='请输入用户名！')
