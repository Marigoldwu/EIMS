# from model.ConnDB import ConnDB
# from model.user import User
# # 数据库参数配置
# server = "127.0.0.1"
# port = "1433"
# user = "sa"
# password = "123456"
# charset = "utf-8"
# database = "EIMS"
# ms = ConnDB(server=server, port=port, user=user, password=password, database=database, autocommit=True, as_dict=True)
#
# # 查
# sql = "select * from myUser"
# # 增
# sql2 = "insert into myUser values (%s, %s, %s, %s)"
# # 改
# sql3 = "update myUser set password=%s where user_id=%s"
# result = ms.ExecQuery(sql, ())
# # nums = len(result)
# item = result[0]
# user = User(item['user_id'], item['username'], item['password'], item['is_deleted'])
# print(user.username)
# # ms.ExecNonQuery(sql2, (nums+1, "lisa", "123456", 0))
# ms.ExecNonQuery(sql3, ("1234567", 3))
# ms.close()

# -*- coding: utf-8 -*-
import tkinter
from view.login import *
root = tkinter.Tk()
style = ttk.Style("cosmo")
root.title("疫情医疗信息管理系统")
LoginPage(root)
root.mainloop()
