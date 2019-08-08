# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2019/7/10  11:23
# @abstract    :创建单个表，单个表

import pandas as pd


for j in range(80, 100):
	try:
		df = pd.read_excel("D:/d/xingyun/福建企业数据字典更新.xlsx",sheetname= j)
		table_name =df.ix[0,0]
		table_name = table_name.replace("wiseweb","wb").upper()
		# 当包含空白列时自动停止,故不知终止索引值可空
		field = df.ix[:,["对应字段", "数据类型"]].fillna(0).values  #无values 则是dataf格式，有则是嵌套数组

		if len(table_name) > 30:
			# print(table_name)
			table_name = table_name + "*******{0}".format(len(table_name) - 30)
		new_data = []
		for i in range(0, len(field)):
			if field[i][1]: #分出无字段类型的
				field_type = field[i][1].split(' ')[0].lower() # 切出字段类型,忽视大小写，统一先按小写处理
				if '(' not in field_type: #单字段类型无字符数限制

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
							item = [field[i][0].upper(), '{0}({1})'.format("VARCHAR2", num)]
						else:
							item = [field[i][0].upper(),'{0}({1})'.format("VARCHAR2",4000) ]
					except:
							item = [field[i][0].upper(),'{0}({1})'.format("VARCHAR2",4000) ]
			else:
				try:
					item = [field[i][0].upper(), "VARCHAR(4000)"]
				except:
					print("error: {0}--{1}".format(table_name, field[i]))
			new_data.append(item)
		with open("D:/d/xingyun/excelToSql_new.txt", "a+", encoding="utf-8") as f:
			f.write("CREATE TABLE {0}".format(table_name))
			f.write("\n(\n")
			for i in range(0, len(new_data) - 1):
				f.write("{0} {1},\n".format(new_data[i][0], new_data[i][1].upper()))
			f.write("{0} {1}".format(new_data[len(new_data) - 1][0], new_data[len(new_data) - 1][1].upper()))
			f.write("\n);\n")
			f.write("\n\n")
		print("the {0} of {1} is out over!".format(j,table_name))
	except:
		print(j)