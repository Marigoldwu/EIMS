# -*- coding: utf-8 -*-
"""
@Time: 2022/4/28 9:28 
@Author: Marigold
@Version: 0.0.0
@Description：
@WeChat Account: Marigold
"""
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from model.ConnDB import *
from view.dataEntryForm import DataEntryForm


class AddPatientFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.patient_id = StringVar()
        self.patient_name = StringVar()
        self.patient_tel = StringVar()
        self.patient_birth = StringVar()
        self.patient_place = StringVar()
        self.is_enter = IntVar()
        self.diagnosis = StringVar()
        self.level = StringVar()
        self.admission_time = StringVar()
        self.confirmed_time = StringVar()
        self.hospital_id = IntVar()
        self.worker_id = IntVar()
        self.medical_supplies_id = IntVar()
        self.createPage()

    def createPage(self):
        ttk.Label(self, text='添加病例信息', font='SimSum -16 bold').grid(row=0, column=0, pady=10)
        ttk.Label(self, text='姓    名:', font='SimSun -14').grid(row=1, column=0, pady=10)
        ttk.Label(self, text='联系方式:', font='SimSun -14').grid(row=2, column=0, pady=10)
        ttk.Label(self, text='出生日期:', font='SimSun -14').grid(row=3, column=0, pady=10)
        ttk.Label(self, text='籍    贯:', font='SimSun -14').grid(row=4, column=0, pady=10)
        ttk.Label(self, text='是否境外输入:', font='SimSun -14').grid(row=5, column=0, pady=10)
        ttk.Label(self, text='诊断结果:', font='SimSun -14').grid(row=6, column=0, pady=10)
        ttk.Label(self, text='症状等级:', font='SimSun -14').grid(row=1, column=3, pady=10)
        ttk.Label(self, text='就诊时间:', font='SimSun -14').grid(row=2, column=3, pady=10)
        ttk.Label(self, text='确诊时间:', font='SimSun -14').grid(row=3, column=3, pady=10)
        ttk.Label(self, text='医院代号:', font='SimSun -14').grid(row=4, column=3, pady=10)
        ttk.Label(self, text='负责人编号:', font='SimSun -14').grid(row=5, column=3, pady=10)
        ttk.Label(self, text='物资编号:', font='SimSun -14').grid(row=6, column=3, pady=10)
        ttk.Entry(self, textvariable=self.patient_name).grid(row=1, column=1, columnspan=2, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.patient_tel).grid(row=2, column=1, columnspan=2, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.patient_birth).grid(row=3, column=1, columnspan=2, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.patient_place).grid(row=4, column=1, columnspan=2, pady=10, sticky=W + E)
        ttk.Radiobutton(self, text="否", value=0, variable=self.is_enter).grid(
            row=5, column=1, padx=5, pady=10)
        ttk.Radiobutton(self, text="是", value=1, variable=self.is_enter).grid(
            row=5, column=2, padx=5, pady=10)
        self.is_enter.set(0)
        ttk.Entry(self, textvariable=self.diagnosis).grid(row=6, column=1, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.level).grid(row=1, column=4, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.admission_time).grid(row=2, column=4, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.confirmed_time).grid(row=3, column=4, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.hospital_id).grid(row=4, column=4, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.worker_id).grid(row=5, column=4, pady=10, sticky=W + E)
        ttk.Entry(self, textvariable=self.medical_supplies_id).grid(row=6, column=4, pady=10, sticky=W + E)
        ttk.Button(self, text='提交', command=self.datacommit, width=10, bootstyle="Primary").grid(row=7, column=1,
                                                                                                 pady=10)
        ttk.Button(self, text='清除', command=self.clear, width=10, bootstyle="Danger").grid(row=7, column=3, pady=10)

    def datacommit(self):
        global patient_name, patient_tel, patient_birth, diagnosis, patient_place, level, confirmed_time, admission_time, hospital_id, medical_supplies_id, worker_id
        ms = ConnDB()
        if self.patient_name.get():
            patient_name = self.patient_name.get()
        else:
            showinfo(title='提示', message='姓名不能为空！')
        if self.patient_tel.get():
            patient_tel = self.patient_tel.get()
        else:
            showinfo(title='提示', message='联系方式不能为空！')
        if self.patient_birth.get():
            patient_birth = self.patient_birth.get()
        else:
            showinfo(title='提示', message='出生日期不能为空！')
        if self.patient_place.get():
            patient_place = self.patient_place.get()
        else:
            showinfo(title='提示', message='籍贯不能为空！')
        if self.diagnosis.get():
            diagnosis = self.diagnosis.get()
        else:
            showinfo(title='提示', message='诊断结果不能为空！')
        if self.level.get():
            level = self.level.get()
        else:
            showinfo(title='提示', message='症状等级不能为空！')
        if self.admission_time.get():
            admission_time = self.admission_time.get()
        else:
            showinfo(title='提示', message='就诊时间不能为空！')
        if self.confirmed_time.get():
            confirmed_time = self.confirmed_time.get()
        else:
            showinfo(title='提示', message='确诊时间不能为空！')
        if self.hospital_id.get():
            hospital_id = self.hospital_id.get()
        else:
            showinfo(title='提示', message='医院代号不能为空！')
        if self.worker_id.get():
            worker_id = self.worker_id.get()
        else:
            showinfo(title='提示', message='负责人编号不能为空！')
        if self.medical_supplies_id.get():
            medical_supplies_id = self.medical_supplies_id.get()
        else:
            showinfo(title='提示', message='医疗用品编号不能为空！')
        number = len(ms.ExecQuery("select patient_id from patient"))
        sql = "insert into patient values({},N'{}',{},N'{}',N'{}',{},N'{}',N'{}',N'{}',N'{}',{},{},{},{},0)".format(
            number + 1, patient_name,
            patient_tel, patient_birth,
            patient_place, self.is_enter.get(),
            diagnosis,
            level,
            admission_time,
            confirmed_time, 0,
            hospital_id,
            worker_id,
            medical_supplies_id)
        try:
            # print(sql)
            ms.ExecNonQuery(sql, ())
            showinfo(title='提示', message='添加成功！')
            self.clear()

        except Exception as e:
            showinfo(title='提示', message='出错了！请重试！')
            print(str(e))
        ms.close()

    def clear(self):
        self.patient_name.set('')
        self.patient_tel.set('')
        self.patient_birth.set('')
        self.patient_place.set('')
        self.is_enter.set(0)
        self.diagnosis.set('')
        self.level.set('')
        self.admission_time.set('')
        self.confirmed_time.set('')
        self.hospital_id.set(1)
        self.worker_id.set(1)
        self.medical_supplies_id.set(1)


class SearchFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.number = StringVar()
        self.userName = StringVar()
        self.sex = StringVar()
        self.age = StringVar()
        self.birth = StringVar()
        self.tel = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.major = StringVar()
        self.r = IntVar()
        self.index = StringVar()
        self.way = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='查询病例信息', font='SimSum -16 bold').grid(row=0, column=0, pady=10)
        Button(self, text="显示全部病例", command=self.displayall, font='SimSun -14').grid(row=1, column=4, padx=5, pady=10,
                                                                                     sticky=W + E + N + S)
        Label(self, text='查询方式:', font='SimSun -14').grid(row=1, column=0, padx=5, pady=10, sticky=W)
        combobox = ttk.Combobox(self, textvariable=self.way, font='SimSun -14')
        combobox.grid(row=1, column=1, padx=5, pady=10, sticky=W + E + N + S)
        # 设置下拉菜单中的值
        combobox['value'] = ("编号", "姓名")
        combobox['state'] = "readonly"  # 设定下拉框状态，readonly表示只读，不可更改内容
        combobox.current(0)
        Entry(self, text=self.index).grid(row=1, column=2, padx=5, pady=10, sticky=W + E + N + S)
        Button(self, text='查询', command=lambda: self.search(self.way.get(), self.index.get()), font='SimSun -14') \
            .grid(row=1, column=3, padx=5, pady=10, sticky=W + E + N + S)
        Label(self, text='上一次查询记录:', font='SimSun -14').grid(row=4, column=0, padx=5, pady=10, sticky=N)

    def displayall(self):
        ms = ConnDB(as_dict=False)
        sql = "select patient_id,patient_name,patient_place,patient_tel,is_enter,diagnosis,hospital_name,worker_name " \
              "from patient left join hospital on patient.hospital_id = hospital.hospital_id LEFT JOIN worker ON " \
              "patient.worker_id=worker.worker_id LEFT JOIN medical_supplies on patient.medical_supplies_id = " \
              "medical_supplies.medical_supplies_id where is_deleted=0 "
        result = ms.ExecQuery(sql, ())
        ms.close()
        # 定义列
        columns = ("编号", "姓名", "籍贯", "联系方式", "是否境外输入", "诊断结果", "医院", "负责人")
        tree = ttk.Treeview(self, show='headings', columns=columns)
        tree.grid(row=4, column=1, columnspan=1000, sticky=W + E + N + S)
        # 设置列，不显示
        tree.column("编号", width=80, anchor="center")
        tree.column("姓名", width=80, anchor="center")
        tree.column("籍贯", width=80, anchor="center")
        tree.column("联系方式", width=100, anchor="center")
        tree.column("是否境外输入", width=100, anchor="center")
        tree.column("诊断结果", width=80, anchor="center")
        tree.column("医院", width=200, anchor="center")
        tree.column("负责人", width=80, anchor="center")
        # 显示表头
        tree.heading("编号", text="编号")
        tree.heading("姓名", text="姓名")
        tree.heading("籍贯", text="籍贯")
        tree.heading("联系方式", text="联系方式")
        tree.heading("是否境外输入", text="是否境外输入")
        tree.heading("诊断结果", text="诊断结果")
        tree.heading("医院", text="医院")
        tree.heading("负责人", text="负责人")
        # 添加数据
        i = 0
        for data in result:
            # for j in range(0, len(data)):
            #     if type(result[i][j]) == int:
            #         continue
            #     # print(chardet.detect(data[j]))
            #     data[j].encode('utf-8')
            tree.insert("", i, text=str(i), values=data)
            i += 1

        def all(event):
            item = tree.selection()  # 'I001'、'I002'
            if item:
                txt = tree.item(item[0], 'values')
                ms = ConnDB(as_dict=False)
                sql = "select * from patient where patient_id={} and is_deleted=0".format(int(txt[0]))
                result = ms.ExecQuery(sql, ())[0]
                ms.close()
                f = open('info.txt', 'w', encoding='utf-8')
                f.truncate()
                for item in result:
                    f.writelines(str(item)+'@')
                f.close()
                top = Toplevel()
                DataEntryForm(top)

        def deleteItem(event):

            item = tree.selection()  # 'I001'、'I002'
            if item:
                txt = tree.item(item[0], 'values')
                if askyesno('确认操作', '确定删除该条记录？'):
                    ms = ConnDB(as_dict=False)
                    sql = "update patient set is_deleted=1 where patient_id={}".format(int(txt[0]))
                    ms.ExecNonQuery(sql, ())
                    ms.close()
                    showinfo("提示", "删除成功！")
        tree.bind('<Double-1>', all)
        tree.bind('<3>', deleteItem)

    def search(self, way, index):
        ms = ConnDB(as_dict=False)
        if way == '编号':

            sql = "select patient_id,patient_name,patient_place,patient_tel,is_enter,diagnosis,hospital_name," \
                  "worker_name " \
                  "from patient left join hospital on patient.hospital_id = hospital.hospital_id LEFT JOIN worker ON " \
                  "patient.worker_id=worker.worker_id LEFT JOIN medical_supplies on patient.medical_supplies_id = " \
                  "medical_supplies.medical_supplies_id where patient_id=%s "
            if index.isdigit():
                result = ms.ExecQuery(sql, (index,))
                ms.close()
                if len(result):
                    # 定义列
                    columns = ("编号", "姓名", "籍贯", "联系方式", "是否境外输入", "诊断结果", "医院", "负责人")
                    tree = ttk.Treeview(self, show='headings', columns=columns)
                    tree.grid(row=4, column=1, columnspan=10)
                    # 设置列，不显示
                    tree.column("编号", width=80, anchor="center")
                    tree.column("姓名", width=80, anchor="center")
                    tree.column("籍贯", width=80, anchor="center")
                    tree.column("联系方式", width=100, anchor="center")
                    tree.column("是否境外输入", width=100, anchor="center")
                    tree.column("诊断结果", width=80, anchor="center")
                    tree.column("医院", width=200, anchor="center")
                    tree.column("负责人", width=80, anchor="center")
                    # 显示表头
                    tree.heading("编号", text="编号")
                    tree.heading("姓名", text="姓名")
                    tree.heading("籍贯", text="籍贯")
                    tree.heading("联系方式", text="联系方式")
                    tree.heading("是否境外输入", text="是否境外输入")
                    tree.heading("诊断结果", text="诊断结果")
                    tree.heading("医院", text="医院")
                    tree.heading("负责人", text="负责人")
                    # 添加数据
                    for i in range(0, len(result)):
                        # for j in range(0, len(result[i])):
                        #     if type(result[i][j]) == int:
                        #         continue
                        #     # print(chardet.detect(result[i][j]))
                        #     result[i][j].encode('utf-8')
                        tree.insert("", i, text=str(i), values=result[i])

                else:
                    showinfo('提示', '该编号的病例不存在！')
            else:
                showinfo(title='提示', message='请输入正确编号！')
        elif way == '姓名':
            sql = "select patient_id,patient_name,patient_place,patient_tel,is_enter,diagnosis,hospital_name," \
                  "worker_name " \
                  "from patient left join hospital on patient.hospital_id = hospital.hospital_id LEFT JOIN worker ON " \
                  "patient.worker_id=worker.worker_id LEFT JOIN medical_supplies on patient.medical_supplies_id = " \
                  "medical_supplies.medical_supplies_id where patient_name=N'%s' " % index
            result = ms.ExecQuery(sql, ())
            ms.close()
            if len(result):
                # 定义列
                columns = ("编号", "姓名", "籍贯", "联系方式", "是否境外输入", "诊断结果", "医院", "负责人")
                tree = ttk.Treeview(self, show='headings', columns=columns)
                tree.grid(row=4, column=1, columnspan=10)
                # 设置列，不显示
                tree.column("编号", width=80, anchor="center")
                tree.column("姓名", width=80, anchor="center")
                tree.column("籍贯", width=80, anchor="center")
                tree.column("联系方式", width=100, anchor="center")
                tree.column("是否境外输入", width=100, anchor="center")
                tree.column("诊断结果", width=80, anchor="center")
                tree.column("医院", width=200, anchor="center")
                tree.column("负责人", width=80, anchor="center")
                # 显示表头
                tree.heading("编号", text="编号")
                tree.heading("姓名", text="姓名")
                tree.heading("籍贯", text="籍贯")
                tree.heading("联系方式", text="联系方式")
                tree.heading("是否境外输入", text="是否境外输入")
                tree.heading("诊断结果", text="诊断结果")
                tree.heading("医院", text="医院")
                tree.heading("负责人", text="负责人")
                # 添加数据
                for i in range(0, len(result)):
                    # for j in range(0, len(result[i])):
                    #     if type(result[i][j]) == int:
                    #         continue
                    #     # print(chardet.detect(result[i][j]))
                    #     result[i][j].encode('utf-8')
                    tree.insert("", i, text=str(i), values=result[i])
            else:
                showinfo('提示', '该姓名的病例不存在！')

# class EditFrame(Frame):  # 继承Frame类
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.root = master  # 定义内部变量root
#         self.number = StringVar()
#         self.userName = StringVar()
#         self.sex = StringVar()
#         self.age = StringVar()
#         self.birth = StringVar()
#         self.tel = StringVar()
#         self.email = StringVar()
#         self.address = StringVar()
#         self.major = StringVar()
#         self.r = IntVar()
#         self.index = StringVar()
#         self.way = StringVar()
#         self.oldusername = StringVar()
#         self.oldsex = StringVar()
#         self.oldage = StringVar()
#         self.oldbirth = StringVar()
#         self.oldtel = StringVar()
#         self.oldemail = StringVar()
#         self.oldaddress = StringVar()
#         self.oldmajor = StringVar()
#         self.createPage()
#
#     def createPage(self):
#         Label(self, text='更新病例信息', font='SimSun -16 bold').grid(row=0, column=0, pady=10)
#         Label(self, text='编号').grid(row=1, column=0, padx=5, pady=10)
#         Entry(self, textvariable=self.number).grid(row=1, column=1, padx=5, pady=10)
#         Button(self, text='查询', command=lambda: self.search(self.number.get()), font='SimSun -14', width=10).grid(row=1,
#                                                                                                                   column=2,
#                                                                                                                   padx=5,
#                                                                                                                   pady=10)
#         Label(self, text='姓   名:', font='SimSun -14').grid(row=2, column=0, pady=10)
#         Label(self, text='性   别:', font='SimSun -14').grid(row=3, column=0, pady=10)
#         Label(self, text='年   龄:', font='SimSun -14').grid(row=4, column=0, pady=10)
#         Label(self, text='出生日期:', font='SimSun -14').grid(row=5, column=0, pady=10)
#         Label(self, text='联系方式:', font='SimSun -14').grid(row=2, column=2, pady=10)
#         Label(self, text='邮   箱:', font='SimSun -14').grid(row=3, column=2, pady=10)
#         Label(self, text='地   址:', font='SimSun -14').grid(row=4, column=2, pady=10)
#         Label(self, text='专   业:', font='SimSun -14').grid(row=5, column=2, pady=10)
#         Entry(self, textvariable=self.userName).grid(row=2, column=1, pady=10)
#         Entry(self, textvariable=self.sex).grid(row=3, column=1, pady=10)
#         Entry(self, textvariable=self.age).grid(row=4, column=1, pady=10)
#         Entry(self, textvariable=self.birth).grid(row=5, column=1, pady=10)
#         Entry(self, textvariable=self.tel).grid(row=2, column=3, pady=10)
#         Entry(self, textvariable=self.email).grid(row=3, column=3, pady=10)
#         Entry(self, textvariable=self.address).grid(row=4, column=3, pady=10)
#         Entry(self, textvariable=self.major).grid(row=5, column=3, pady=10)
#         Button(self, text='更新', command=lambda: self.updateinfo(self.number.get()), font='SimSun -14', width=10).grid(
#             row=6, column=1, pady=10)
#         Button(self, text='撤销', command=lambda: self.repeal(self.number.get()), font='SimSun -14', width=10).grid(row=6,
#                                                                                                                   column=2,
#                                                                                                                   pady=10)
#
#     def search(self, number):
#         if number:
#             db = MySQLdb.connect(host='localhost', user='root', password='woyangni0109', db='new_schema',
#                                  charset='utf8')
#             cur = db.cursor()
#             numberexists = 0
#             sql = "select number from {}"
#             sql = sql.format(self.tablename)
#             cur.execute(sql)
#             numberdata = cur.fetchall()
#             for i in range(0, len(numberdata)):
#                 if numberdata[i][0] == number:
#                     numberexists = 1
#                     break
#                 else:
#                     i += 1
#             if numberexists:
#                 sql = "select * from {} where number = '{}'"
#                 sql = sql.format(self.tablename, number)
#                 cur.execute(sql)
#                 contactsdata = cur.fetchall()
#                 db.close()
#                 self.oldusername = contactsdata[0][1]
#                 self.oldsex = contactsdata[0][2]
#                 self.oldage = contactsdata[0][3]
#                 self.oldbirth = contactsdata[0][4]
#                 self.oldtel = contactsdata[0][5]
#                 self.oldemail = contactsdata[0][6]
#                 self.oldaddress = contactsdata[0][7]
#                 self.oldmajor = contactsdata[0][8]
#
#                 self.userName.set(contactsdata[0][1])
#                 self.sex.set(contactsdata[0][2])
#                 self.age.set(contactsdata[0][3])
#                 self.birth.set(contactsdata[0][4])
#                 self.tel.set(contactsdata[0][5])
#                 self.email.set(contactsdata[0][6])
#                 self.address.set(contactsdata[0][7])
#                 self.major.set(contactsdata[0][8])
#             else:
#                 showinfo('提示', '该学号的学生不存在！')
#                 self.number.set('')
#         else:
#             showinfo('提示', '学号不能为空！')
#
#     def updateinfo(self, number):
#         newusername = self.userName.get()
#         newsex = self.sex.get()
#         newage = self.age.get()
#         newbirth = self.birth.get()
#         newtel = self.tel.get()
#         newemail = self.email.get()
#         newaddress = self.address.get()
#         newmajor = self.major.get()
#         # 提交到数据库
#         db = MySQLdb.connect(host='localhost', user='root', password='woyangni0109', db='new_schema', charset='utf8')
#         cur = db.cursor()
#         sql = "update {} set userName = '{}',sex = '{}'," \
#               "age = '{}',birth = '{}',tel='{}',email = '{}',address = '{}',major = '{}' where number = '{}'"
#         sql = sql.format(self.tablename, newusername, newsex, newage, newbirth, newtel, newemail, newaddress, newmajor,
#                          number)
#         try:
#             cur.execute(sql)
#             db.commit()
#             db.close()
#             showinfo('提示', '数据更新成功!')
#         except:
#             showinfo('提示', '数据更新失败！')
#
#     def repeal(self, number):
#         db = MySQLdb.connect(host='localhost', user='root', password='woyangni0109', db='new_schema', charset='utf8')
#         cur = db.cursor()
#         sql = "update {} set userName = '{}',sex = '{}'," \
#               "age = '{}',birth = '{}',tel='{}',email = '{}',address = '{}',major = '{}' where number = '{}'"
#         sql = sql.format(self.tablename, self.oldusername, self.oldsex, self.oldage, self.oldbirth,
#                          self.oldtel, self.oldemail, self.oldaddress, self.oldmajor, number)
#         try:
#             cur.execute(sql)
#             db.commit()
#             db.close()
#             showinfo('提示', '撤销成功!')
#         except:
#             showinfo('提示', '撤销失败！')
#
#
# class DeleteFrame(Frame):  # 继承Frame类
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.root = master  # 定义内部变量root
#         self.number = StringVar()
#         self.userName = StringVar()
#         self.sex = StringVar()
#         self.age = StringVar()
#         self.birth = StringVar()
#         self.tel = StringVar()
#         self.email = StringVar()
#         self.address = StringVar()
#         self.major = StringVar()
#         self.r = IntVar()
#         self.index = StringVar()
#         self.way = StringVar()
#         f = open('user.txt', 'r', encoding='utf-8')
#         self.tablename = f.read()
#         f.close()
#         self.oldusername = StringVar()
#         self.oldsex = StringVar()
#         self.oldage = StringVar()
#         self.oldbirth = StringVar()
#         self.oldtel = StringVar()
#         self.oldemail = StringVar()
#         self.oldaddress = StringVar()
#         self.oldmajor = StringVar()
#         self.createPage()
#
#     def createPage(self):
#         Label(self, text='删除学生信息', font='SimSun -16 bold').grid(row=0, column=0, pady=10)
#         Label(self, text='学号').grid(row=1, column=0, padx=5, pady=10)
#         Entry(self, textvariable=self.number).grid(row=1, column=1, padx=5, pady=10)
#         Button(self, text='查询', command=lambda: self.search(self.number.get()), font='SimSun -14', width=10).grid(row=1,
#                                                                                                                   column=2,
#                                                                                                                   padx=5,
#                                                                                                                   pady=10)
#         Label(self, text='姓   名:', font='SimSun -14').grid(row=2, column=0, pady=10)
#         Label(self, text='性   别:', font='SimSun -14').grid(row=3, column=0, pady=10)
#         Label(self, text='年   龄:', font='SimSun -14').grid(row=4, column=0, pady=10)
#         Label(self, text='出生日期:', font='SimSun -14').grid(row=5, column=0, pady=10)
#         Label(self, text='联系方式:', font='SimSun -14').grid(row=2, column=2, pady=10)
#         Label(self, text='邮   箱:', font='SimSun -14').grid(row=3, column=2, pady=10)
#         Label(self, text='地   址:', font='SimSun -14').grid(row=4, column=2, pady=10)
#         Label(self, text='专   业:', font='SimSun -14').grid(row=5, column=2, pady=10)
#         Entry(self, textvariable=self.userName).grid(row=2, column=1, pady=10)
#         Entry(self, textvariable=self.sex).grid(row=3, column=1, pady=10)
#         Entry(self, textvariable=self.age).grid(row=4, column=1, pady=10)
#         Entry(self, textvariable=self.birth).grid(row=5, column=1, pady=10)
#         Entry(self, textvariable=self.tel).grid(row=2, column=3, pady=10)
#         Entry(self, textvariable=self.email).grid(row=3, column=3, pady=10)
#         Entry(self, textvariable=self.address).grid(row=4, column=3, pady=10)
#         Entry(self, textvariable=self.major).grid(row=5, column=3, pady=10)
#         Button(self, text='删除', command=lambda: self.delete(self.number.get()), font='SimSun -14', width=10).grid(row=6,
#                                                                                                                   column=1,
#                                                                                                                   pady=10)
#         Button(self, text='撤销', command=lambda: self.repeal(self.number.get()), font='SimSun -14', width=10).grid(row=6,
#                                                                                                                   column=2,
#                                                                                                                   pady=10)
#
#     def search(self, number):
#         if number:
#             db = MySQLdb.connect(host='localhost', user='root', password='woyangni0109', db='new_schema',
#                                  charset='utf8')
#             cur = db.cursor()
#             numberexists = 0
#             sql = "select number from {}"
#             sql = sql.format(self.tablename)
#             cur.execute(sql)
#             numberdata = cur.fetchall()
#             for i in range(0, len(numberdata)):
#                 if numberdata[i][0] == number:
#                     numberexists = 1
#                     break
#                 else:
#                     i += 1
#             if numberexists:
#                 sql = "select * from {} where number = '{}'"
#                 sql = sql.format(self.tablename, number)
#                 cur.execute(sql)
#                 contactsdata = cur.fetchall()
#                 db.close()
#                 self.oldusername = contactsdata[0][1]
#                 self.oldsex = contactsdata[0][2]
#                 self.oldage = contactsdata[0][3]
#                 self.oldbirth = contactsdata[0][4]
#                 self.oldtel = contactsdata[0][5]
#                 self.oldemail = contactsdata[0][6]
#                 self.oldaddress = contactsdata[0][7]
#                 self.oldmajor = contactsdata[0][8]
#
#                 self.userName.set(contactsdata[0][1])
#                 self.sex.set(contactsdata[0][2])
#                 self.age.set(contactsdata[0][3])
#                 self.birth.set(contactsdata[0][4])
#                 self.tel.set(contactsdata[0][5])
#                 self.email.set(contactsdata[0][6])
#                 self.address.set(contactsdata[0][7])
#                 self.major.set(contactsdata[0][8])
#             else:
#                 showinfo('提示', '该学号的学生不存在！')
#                 self.number.set('')
#         else:
#             showinfo('提示', '学号不能为空！')
#
#     def delete(self, number):
#         db = MySQLdb.connect(host='localhost', user='root', password='woyangni0109', db='new_schema', charset='utf8')
#         cur = db.cursor()
#         sql = "delete from {} where number = '{}'"
#         sql = sql.format(self.tablename, number)
#         try:
#             cur.execute(sql)
#             db.commit()
#             db.close()
#             showinfo('提示', '删除成功！')
#             self.number.set('')
#             self.userName.set('')
#             self.sex.set('')
#             self.age.set('')
#             self.birth.set('')
#             self.tel.set('')
#             self.email.set('')
#             self.address.set('')
#             self.major.set('')
#         except:
#             showinfo('提示', '删除失败！')
#
#     def repeal(self, number):
#         db = MySQLdb.connect(host='localhost', user='root', password='woyangni0109', db='new_schema', charset='utf8')
#         cur = db.cursor()
#         sql = "update {} set userName = '{}',sex = '{}'," \
#               "age = '{}',birth = '{}',tel='{}',email = '{}',address = '{}',major = '{}' where number = '{}'"
#         sql = sql.format(self.tablename, self.oldusername, self.oldsex, self.oldage, self.oldbirth,
#                          self.oldtel, self.oldemail, self.oldaddress, self.oldmajor, number)
#         try:
#             cur.execute(sql)
#             db.commit()
#             db.close()
#             showinfo('提示', '撤销成功!')
#         except:
#             showinfo('提示', '撤销失败！')


# class CopyFrame(Frame):  # 继承Frame类
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.root = master  # 定义内部变量root
#         f = open('user.txt', 'r', encoding='utf-8')
#         self.tablename = f.read()
#         f.close()
#         self.createPage()
#
#     def createPage(self):
#         Label(self, text='数据备份与恢复', font='SimSun -16 bold').grid(row=0, column=0, padx=5, pady=10, sticky=W)
#         Button(self, text='备份数据', command=self.backups, font='SimSun -14').grid(
#             row=1, column=0, padx=5, pady=10, sticky=W)
#         Button(self, text='恢复数据', command=self.renew, font='SimSun -14').grid(
#             row=1, column=1, padx=5, pady=10, sticky=W)
#
#     def backups(self):
#         # 追加mysql的bin目录到环境变量
#         # sys.path.append('C:\Users\HP\AppData\Bin')
#         # 如果不存在backup文件，新建一个
#         if not os.path.exists('backup'):
#             os.mkdir('backup')
#         # 切换到新建的文件夹中
#         os.chdir('backup')
#         # def tuplesql(command,server,user,passwd,db,table,filename):
#         #   return (mysqlcomm,dbserver,dbuser,dbpasswd,dbname,dbtable,exportfile)
#         # 定义一系列参数
#         mysqlcomm = 'mysqldump'
#         dbserver = 'locolhost'
#         dbuser = 'root'
#         dbpasswd = 'woyangni0109'
#         dbname = 'new_schema'
#         dbtable = str(self.tablename)
#         exportfile = 'backups.sql'
#         # 定义sql的格式
#         sqlfromat = "%s -h%s -u%s -p%s %s %s >%s"
#         # 生成相应的sql语句
#         sql = (sqlfromat % (mysqlcomm, dbserver, dbuser, dbpasswd, dbname, dbtable, exportfile))
#
#         # 判断是否已经有相应的sql文件生成；如果有，就按时间重命名该文件
#         if os.path.exists(r'backups.sql'):
#             os.rename('backups.sql', 'backups' + str(time.time()) + '.sql')
#         # 执行sql并获取语句，os.system和subprocess.Popen执行该sql无效果，不知道是怎么回事，后续会继续关注
#         result = os.popen(sql)
#         # 对sql执行进行判断
#         if result:
#             showinfo(title='提示', message='数据备份成功！')
#         else:
#             showinfo(title='提示', message='数据备份失败！')
#
#     def renew(self):
#         # 简单的恢复关键代码其实就下面这一行mysqldump换为mysql 用户名 密码 你要恢复到的数据库名 < sql文件
#         try:
#             os.system("mysql -uroot -pwoyangni0109 new_schema < /backup/backups.sql")
#             showinfo(title='提示', message='数据恢复成功！')
#         except Exception as e:
#             showinfo(title='提示', message='数据恢复失败！\n' + str(e))
