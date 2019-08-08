# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2019/7/3  21:44
# @abstract    :

import pandas as pd


for j in range(1, 90): # 表索引超过上限会报错
	# j = 1
	df = pd.read_excel("D:/d/xingyun/福建企业数据字典.xlsx",sheetname= j)
	# data = df.head()
	# print(data)
	table_name =df.ix[0,0]
	table_name = table_name.replace("wiseweb","wb").upper()
	# 当包含空白列时自动停止,故不知终止索引值可空
	field = df.ix[:,["对应字段", "数据类型"]].fillna(0).values  #无values 则是dataf格式，有则是嵌套数组
	# print(table_name,"\n",field)
	# print(type(field))
	# for item in field:
	# 	print(item,type(item),len(field))
	# 	for i in item:
	# 		print(i)
	# 	break
	if len(table_name) >= 30:
		print(table_name)
		table_name = table_name + "*******"
	new_data = []
	for i in range(0, len(field)):
		# print(field[i])
		# print(field[i][1],field,len(field))
		if field[i][1]: #分出无字段类型的
			field_type = field[i][1].split(' ')[0].lower() # 切出字段类型,忽视大小写，统一先按小写处理
			if '(' not in field_type: #单字段类型无字符数限制

				if field_type  in("text", "clob", "longtext") :
					item =[field[i][0].upper(), "CLOB"]
					# print("1")
				if field_type == "double" or field_type =="number":
					item =[field[i][0].upper(), "NUMBER"]
					# print("2")
				if field_type == "datetime":
					item =[field[i][0].upper(), "date"]
					# print("3")
				if field_type in ["bigint" , "smallint" , "int"]:
					if field_type == "bigint":
						item = [field[i][0].upper(),'NUMBER' ]
						# print("4")
					else:
						item = [field[i][0].upper(),'INT' ]
						# print(5)
				if field_type == "timestamp" or field_type == "date":
						item = [field[i][0].upper(), field_type]
						# print(6)
				if field_type == "varchar" or field_type =="varchar2":
					# print(7)
					item = [field[i][0].upper(),'{0}({1})'.format(field_type,20) ]
			else:
				# print(field_type)
				num = field_type.split('(')[1].strip(')')  # 切出字段类型的数值
				field_type= field_type.split('(')[0].lower()
				# print(num,field_type)
				if field_type in ["bigint" , "smallint","int"]:
					item = [field[i][0].upper(),'NUMBER({0})'.format(num) ]
					# print("66")

				if  field_type == "varchar" or field_type =="varchar2":
					# print(field_type)
					if int(num) <= 4000:
						item = [field[i][0].upper(), '{0}({1})'.format(field_type, num)]
						# print(8)
					else:
						# print(9)
						item = [field[i][0].upper(),'{0}({1})'.format(field_type,4000) ]
		else:
			try:
				item = [field[i][0].upper(), "INT"]
			except:
				print("error: {0}--{1}".format(table_name, field[i]))
			# print(10)
		# print(item)
		new_data.append(item)
	# print(new_data)
	with open("D:/d/xingyun/excelToSql.txt", "a+", encoding="utf-8") as f:
		f.write("CREATE TABLE {0}".format(table_name))
		f.write("\n(\n")
		for i in range(0, len(new_data) - 1):
			f.write("{0} {1},\n".format(new_data[i][0], new_data[i][1].upper()))
		f.write("{0} {1}".format(new_data[len(new_data) - 1][0], new_data[len(new_data) - 1][1].upper()))
		f.write("\n)\n")
		f.write("\n\n")
	print("the {0} of {1} is out over!".format(j,table_name))
	# break
