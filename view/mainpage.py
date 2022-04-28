# -*- coding: utf-8 -*-
"""
@Time: 2022/4/28 9:24 
@Author: Marigold
@Version: 0.0.0
@Description：
@WeChat Account: Marigold
"""
# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from view.view import *  # 菜单栏对应的各个子页面
import view.login as login


class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry("1200x600")
        f = open('user.txt', 'r', encoding='utf-8')
        self.tablename = f.read()
        f.close()
        self.root.title('疫情医疗信息管理系统   ' + '欢迎您：' + self.tablename)
        # self.root.resizable(0, 0)
        self.createPage()

    def createPage(self):
        self.AddPatient = AddPatientFrame(self.root)  # 创建不同Frame
        self.Search = SearchFrame(self.root)
        # self.Editinfo = EditFrame(self.root)
        # self.Delete = DeleteFrame(self.root)
        self.Search.grid()  # 默认显示查询界面
        menubar = Menu(self.root)
        menubar.add_command(label='添加病例', command=self.add, font='SimSun -14')
        menubar.add_command(label='查询病例', command=self.search, font='SimSun -14')
        # menubar.add_command(label='更新', command=self.edit, font='SimSun -14')
        # menubar.add_command(label='删除', command=self.delete, font='SimSun -14')
        # menubar.add_command(label='备份与恢复', command=self.copy, font='SimSun -14')
        menubar.add_command(label='切换账户', command=self.change, font='SimSun -14')
        self.root['menu'] = menubar  # 设置菜单栏

    def add(self):
        self.AddPatient.grid()
        self.Search.grid_forget()

    def search(self):
        self.AddPatient.grid_forget()
        self.Search.grid()

    def change(self):
        if askokcancel('提示', '确定要切换账户？'):
            self.root.destroy()
            root = tkinter.Tk()
            root.title("疫情医疗信息管理系统")
            login.LoginPage(root)
            root.mainloop()
