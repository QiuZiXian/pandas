# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2019/7/9  17:41
# @abstract    : 1/2/3处理后的更新

import pandas as pd

key_list = []
for j in range(2, 100):
	try:
		df = pd.read_excel("D:/d/xingyun/福建企业数据字典更新.xlsx",sheetname= j)
	# try:
		old_table_name =df.ix[0,1]
		if not old_table_name:
			old_table_name = df.ix[1,1]
		print(old_table_name)
		old_table_name = old_table_name.replace("wiseweb","wb").upper()
		if len(old_table_name) > 30:
			old_table_name =  "{0}*****{1}".format(old_table_name, len(old_table_name ) - 30)
		new_table_name = df.ix[0,0]
		if not new_table_name:
			new_table_name = df.ix[1,0]
		new_table_name = new_table_name.replace("wiseweb","wb").replace("company", "cy").upper()
		# 当包含空白列时自动停止,故不知终止索引值可空
		primary_key = df.ix[0,"对应字段"]  #无values 则是dataf格式，有则是嵌套数组

		# print(old_table_name, new_table_name, primary_key)
		if primary_key:
			if len(new_table_name) > 27:
				pk_name = "PK_{0}****{1}".format(new_table_name, len(new_table_name) - 27 )
			else:
				pk_name = "PK_{0}".format(new_table_name )
			key_list.append((old_table_name,new_table_name, primary_key, pk_name))
		else:
			print(old_table_name)
	except:
		print(j)
# print(len(key_list), key_list)

# alter table table_name add constraint key_name primary key(key_field)
# alter table old_table_name rename to new_table_name
with open("D:/d/xingyun/update_rename_1.txt", 'w', encoding="utf-8") as f:
	for item in key_list:
		f.write("ALTER TABLE {0} RENAME TO {1};\n\n".format(item[0], item[1]))
print("rename over!!")

with open( "D:/d/xingyun/update_set_PK_1.txt", 'w', encoding= "utf-8") as f:
	for item in key_list:
		f.write("ALTER TABLE {0} ADD CONSTRAINT {1} PRIMARY KEY({2});\n\n ".format(item[1], item[3].upper(), item[2].upper()))

print("set PK over!!")