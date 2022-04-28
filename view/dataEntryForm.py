# -*- coding: utf-8 -*-
"""
@Time: 2022/4/28 16:03 
@Author: Marigold
@Version: 0.0.0
@Description：
@WeChat Account: Marigold
"""
from tkinter import *
from tkinter.messagebox import showinfo, askyesno
from model.ConnDB import ConnDB
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class DataEntryForm(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        with open('info.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
            lista = data[0].split('@')
        f.close()
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (800, 600))  # 设置窗口大小
        # self.root.minsize(500, 350)
        # self.root.maxsize(500, 350)

        self.root.title('修改信息')
        self.page = Frame(self.root)  # 创建Frame
        # form variables
        self.patient_id = IntVar()
        self.patient_name = StringVar()
        self.patient_tel = IntVar()
        self.patient_birth = StringVar()
        self.patient_place = StringVar()
        self.is_enter = IntVar()
        self.diagnosis = StringVar()
        self.level = StringVar()
        self.admission_time = StringVar()
        self.confirmed_time = StringVar()
        self.is_recovery = IntVar()
        self.hospital_id = IntVar()
        self.worker_id = IntVar()
        self.medical_supplies_id = IntVar()
        self.patient_id.set(int(lista[0]))
        self.patient_name.set(lista[1])
        self.patient_tel.set(int(lista[2]))
        self.patient_birth.set(lista[3])
        self.patient_place.set(lista[4])
        self.is_enter.set(int(lista[5]))
        self.diagnosis.set(lista[6])
        self.level.set(lista[7])
        self.admission_time.set(lista[8])
        self.confirmed_time.set(lista[9])
        self.is_recovery.set(int(lista[10]))
        self.hospital_id.set(int(lista[11]))
        self.worker_id.set(int(lista[12]))
        self.medical_supplies_id.set(int(lista[13]))
        self.createPage()

    def createPage(self):
        ttk.Label(self.root, text='添加病例信息', font='SimSum -16 bold').grid(row=0, column=0, pady=10)
        ttk.Label(self.root, text='姓    名:', font='SimSun -14').grid(row=1, column=0, pady=10)
        ttk.Label(self.root, text='联系方式:', font='SimSun -14').grid(row=2, column=0, pady=10)
        ttk.Label(self.root, text='出生日期:', font='SimSun -14').grid(row=3, column=0, pady=10)
        ttk.Label(self.root, text='籍    贯:', font='SimSun -14').grid(row=4, column=0, pady=10)
        ttk.Label(self.root, text='是否境外输入:', font='SimSun -14').grid(row=5, column=0, pady=10)
        ttk.Label(self.root, text='诊断结果:', font='SimSun -14').grid(row=6, column=0, pady=10)
        ttk.Label(self.root, text='症状等级:', font='SimSun -14').grid(row=7, column=0, pady=10)
        ttk.Label(self.root, text='就诊时间:', font='SimSun -14').grid(row=1, column=3, pady=10)
        ttk.Label(self.root, text='确诊时间:', font='SimSun -14').grid(row=2, column=3, pady=10)
        ttk.Label(self.root, text='是否治愈:', font='SimSun -14').grid(row=3, column=3, pady=10)
        ttk.Label(self.root, text='医院代号:', font='SimSun -14').grid(row=4, column=3, pady=10)
        ttk.Label(self.root, text='负责人编号:', font='SimSun -14').grid(row=5, column=3, pady=10)
        ttk.Label(self.root, text='物资编号:', font='SimSun -14').grid(row=6, column=3, pady=10)
        ttk.Entry(self.root, text=self.patient_name, textvariable=self.patient_name).grid(row=1, column=1, columnspan=2,
                                                                                          pady=10, sticky=W + E)
        ttk.Entry(self.root, text=self.patient_tel, textvariable=self.patient_tel).grid(row=2, column=1, columnspan=2,
                                                                                        pady=10, sticky=W + E)
        ttk.Entry(self.root, text=self.patient_birth, textvariable=self.patient_birth).grid(row=3, column=1,
                                                                                            columnspan=2, pady=10,
                                                                                            sticky=W + E)
        ttk.Entry(self.root, text=self.patient_place, textvariable=self.patient_place).grid(row=4, column=1,
                                                                                            columnspan=2, pady=10,
                                                                                            sticky=W + E)
        ttk.Radiobutton(self.root, text="否", value=0, variable=self.is_enter).grid(
            row=5, column=1, padx=5, pady=10, sticky=W)
        ttk.Radiobutton(self.root, text="是", value=1, variable=self.is_enter).grid(
            row=5, column=2, padx=5, pady=10, sticky=W)
        ttk.Entry(self.root, text=self.diagnosis, textvariable=self.diagnosis).grid(row=6, column=1, pady=10,
                                                                                    sticky=W + E)
        ttk.Entry(self.root, text=self.level, textvariable=self.level).grid(row=7, column=1, pady=10, sticky=W + E)
        ttk.Entry(self.root, text=self.admission_time, textvariable=self.admission_time).grid(row=1, column=4, pady=10,
                                                                                              sticky=W + E)
        ttk.Entry(self.root, text=self.confirmed_time, textvariable=self.confirmed_time).grid(row=2, column=4, pady=10,
                                                                                              sticky=W + E)
        ttk.Radiobutton(self.root, text="否", value=0, variable=self.is_recovery).grid(
            row=3, column=4, padx=5, pady=10, sticky=W)
        ttk.Radiobutton(self.root, text="是", value=1, variable=self.is_recovery).grid(
            row=3, column=5, padx=5, pady=10, sticky=W)
        ttk.Entry(self.root, text=self.hospital_id, textvariable=self.hospital_id).grid(row=4, column=4, pady=10,
                                                                                        sticky=W + E)
        ttk.Entry(self.root, text=self.worker_id, textvariable=self.worker_id).grid(row=5, column=4, pady=10,
                                                                                    sticky=W + E)
        ttk.Entry(self.root, text=self.medical_supplies_id, textvariable=self.medical_supplies_id).grid(row=6, column=4,
                                                                                                        pady=10,
                                                                                                        sticky=W + E)
        ttk.Button(self.root, text='提交', command=self.datacommit, width=10, bootstyle="Primary").grid(row=8, column=1,
                                                                                                      pady=10)
        ttk.Button(self.root, text='关闭', command=self.closePage, width=10, bootstyle="Danger").grid(row=8, column=3,
                                                                                                pady=10)

    def datacommit(self):
        global patient_name, patient_tel, patient_birth, diagnosis, patient_place, level, confirmed_time, admission_time, hospital_id, medical_supplies_id, worker_id, is_recovery
        ms = ConnDB()
        if self.patient_name.get():
            patient_name = self.patient_name.get()
        else:
            showinfo(title='提示', message='姓名不能为空！')
            return False
        if self.patient_tel.get():
            patient_tel = self.patient_tel.get()
        else:
            showinfo(title='提示', message='联系方式不能为空！')
            return False
        if self.patient_birth.get():
            patient_birth = self.patient_birth.get()
        else:
            showinfo(title='提示', message='出生日期不能为空！')
            return False
        if self.patient_place.get():
            patient_place = self.patient_place.get()
        else:
            showinfo(title='提示', message='籍贯不能为空！')
            return False
        if self.diagnosis.get():
            diagnosis = self.diagnosis.get()
        else:
            showinfo(title='提示', message='诊断结果不能为空！')
            return False
        if self.level.get():
            level = self.level.get()
        else:
            showinfo(title='提示', message='症状等级不能为空！')
            return False
        if self.admission_time.get():
            admission_time = self.admission_time.get()
        else:
            showinfo(title='提示', message='就诊时间不能为空！')
            return False
        if self.confirmed_time.get():
            confirmed_time = self.confirmed_time.get()
        else:
            showinfo(title='提示', message='确诊时间不能为空！')
            return False
        if self.hospital_id.get():
            hospital_id = self.hospital_id.get()
        else:
            showinfo(title='提示', message='医院代号不能为空！')
            return False
        if self.worker_id.get():
            worker_id = self.worker_id.get()
        else:
            showinfo(title='提示', message='负责人编号不能为空！')
            return False
        if self.medical_supplies_id.get():
            medical_supplies_id = self.medical_supplies_id.get()
        else:
            showinfo(title='提示', message='医疗用品编号不能为空！')
            return False
        number = len(ms.ExecQuery("select patient_id from patient"))
        sql = "update patient set patient_name=N'{}',patient_tel={},patient_birth=N'{}',patient_place=N'{}'," \
              "is_enter={},diagnosis=N'{}',level=N'{}',admission_time=N'{}',confirmed_time=N'{}',is_recovery={}," \
              "hospital_id={},worker_id={},medical_supplies_id={} where patient_id={}".format(
            patient_name,
            patient_tel, patient_birth,
            patient_place, self.is_enter.get(),
            diagnosis,
            level,
            admission_time,
            confirmed_time,
            self.is_recovery.get(),
            hospital_id,
            worker_id,
            medical_supplies_id,
            self.patient_id.get())
        print(sql)
        try:
            # print(sql)
            ms.ExecNonQuery(sql, ())
            showinfo(title='提示', message='更改成功！')
            self.clear()
            self.root.destroy()

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

    def closePage(self):
        if askyesno('确认操作', '确定执行？'):
            self.root.destroy()
# if __name__ == "__main__":
#
#     app = ttk.Window("Data Entry", "superhero", resizable=(False, False))
#     DataEntryForm(app)
#     app.mainloop()
