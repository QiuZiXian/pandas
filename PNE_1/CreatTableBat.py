# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2019/8/8  16:16
# @abstract    : 1、除了clob数据类型，其它统一先设成varchar2（4000）；2、有字段去重 3、关键字处理待增加 4、可以改用csv数据head建初始空表

import pandas as pd

for j in range(2, 101): # 数值索引不能超出sheet数
	df = pd.read_excel("D:/d/xingyun/fj.xlsx",sheet_name=j)
	new_table_name = df.iloc[0,0]
	if pd.isnull(new_table_name):  # pandas 的nan值需要用自带的isnull或isna函数判断
		new_table_name = df.iloc[1,0]
	try:
		new_table_name = new_table_name.replace("wiseweb","wb").replace("company", "cy").upper()
	except:
		print(j, new_table_name)
		break
	if len(new_table_name) >30:
		new_table_name = "{0}*****{1}".format(new_table_name, len(new_table_name ) - 30)
		print(new_table_name)
	field = df.loc[:,["对应字段", "数据类型"]].fillna(0).values  #无values 则是dataf格式，有则是嵌套数组

	new_data = []
	for i in range(0, len(field)): #这里的细节处理对应数据类型都设置为varchar2（4000）来说没什么意义，
		if field[i][1]: #分出无字段类型的
			field_type = field[i][1].split(' ')[0].lower() # 切出字段类型,忽视大小写，统一先按小写处理
			if '(' not in field_type: #单独只有字段类型无字符数限制

				if field_type  in("text", "clob", "longtext") :
					item =[field[i][0].upper(), "CLOB"]
					# print("1")
				else:
					item = [field[i][0].upper(),'{0}({1})'.format("VARCHAR2",4000) ]
			else:
				# print(field_type)
				num = field_type.split('(')[1].strip(')')  # 切出字段类型的数值
				field_type= field_type.split('(')[0].lower()
				try:
					if int(num) <= 4000:
						item = [field[i][0].upper(), '{0}({1})'.format("VARCHAR2", 4000)]
					else:
						item = [field[i][0].upper(),'{0}({1})'.format("VARCHAR2",4000) ]
				except:
						item = [field[i][0].upper(),'{0}({1})'.format("VARCHAR2",4000) ]
		else:
			try:
				item = [field[i][0].upper(), "VARCHAR(4000)"]
			except:
				print("error: {0}--{1}".format(new_table_name, field[i]))
		if item is not in new_data: # 去重，也可以最后用set去重
			new_data.append(item)
	# 将excel表逐一转写成sql语句保存为txt文件
	with open("D:/d/xingyun/excelToSql20190808.txt", "a+", encoding="utf-8") as f:
		f.write("CREATE TABLE {0}".format(new_table_name))
		f.write("\n(\n")
		for i in range(0, len(new_data) - 1):
			f.write("{0} {1},\n".format(new_data[i][0], new_data[i][1].upper()))
		f.write("{0} {1}".format(new_data[len(new_data) - 1][0], new_data[len(new_data) - 1][1].upper()))
		f.write("\n);\n")
		f.write("\n\n")
	print("the {0} of {1} is out over!".format(j,new_table_name))