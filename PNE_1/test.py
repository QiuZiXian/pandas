# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2019/7/4  0:11
# @abstract    :

# str_test =  [['company_id', 'bigint(20) NULL'], ['category_code' ,'int(4) NULL'], ['status', 'int(3) NULL'], ['gather_time' ,'timestamp NOT NULL'],\
#  ['site_name', 0], ['company_name', 0], ['chanle_id', 0], ['rowkey' ,0], ['company_area_code', 'number']]

# for item in str_test:
# 	print(item)
#
# 	for i in item :
# 		print(i)

# for item in str_test:
# 	if item[1]:
#
# 		if '(' in item[1]:
# 			print((item[1].split(' ')[0].split('(')[1]).rstrip(')'))
# 	else:
# 		print(item)

# print('abcd23jfi'.upper())

# print("wiseweb_company_report_social_security".replace("wiseweb", "wb").replace("company", "cy"))

import pandas as pd

# df = pd.read_excel("D:/d/xingyun/福建企业数据字典.xlsx",None)  # sheet_name 设定为None，通过df.key()返回所有表名，sheet_name为索引数值时，返回该表行标签
# print(df.keys())

#返回所有的表名，list
xl = pd.ExcelFile("D:/d/xingyun/福建企业数据字典.xlsx")
# print(xl.sheet_names)
for sheet in xl.sheet_names:
 sh = xl.parse(sheet)
 print(sh.head())

