# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2019/7/4  11:07
# @abstract    :

import pandas as pd

def getDATA( sheet_num, filename= "D:/d/xingyun/福建企业数据字典.xlsx"):
	df = pd.read_excel(filename ,sheetname=16)
	table_name =df.ix[0,0]
	table_name = table_name.replace("wiseweb","wb").upper()
	# 当包含空白列时自动停止,故不知终止索引值可空
	field = df.ix[:,["对应字段", "数据类型"]].fillna(0).values  #无values 则是dataf格式，有则是嵌套数组
	return  table_name, field

def handle(field):
		new_data = []
		for i in range(0, len(field)):
			print(field[i])
			# print(field[i][1],field,len(field))
			if field[i][1]: #分出无字段类型的
				field_type = field[i][1].split(' ')[0] # 切出字段类型
				if '(' not in field_type: #单字段类型无字符数限制

					if field_type  == "text":
						item =[field[i][0].upper(), "Clob"]
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
				if '(' in field_type:
					# print(field_type)
					num = field_type.split('(')[1].strip(')')  # 切出字段类型的数值
					field_type= field_type.split('(')[0]
					# print(num,field_type)
					if field_type in ["bigint" , "smallint","int"]:
						item = [field[i][0].upper(),'NUMBER({0})'.format(num) ]
						# print("66")

					if  field_type == "varchar" or field_type =="varchar2":
						if int(num) <= 4000:
							item = [field[i][0].upper(), '{0}({1})'.format(field_type, num)]
							# print(8)
						else:
							# print(9)
							item = [field[i][0].upper(),'{0}({1})'.format(field_type,4000) ]
			else:
				item = [field[i][0].upper(), "INT"]
				# print(10)
			print(item)
			new_data.append(item)
			return new_data

def outData(data):
	pass