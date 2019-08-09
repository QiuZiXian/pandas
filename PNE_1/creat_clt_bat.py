# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2019/8/9  10:06
# @abstract    :

# 批处理control.CLT文件生成

import os
import pandas as pd

# 获取csv文件名
for a, b, c in os.walk("D:/网智天元/after-6-15"):
    file_list = c
    break

#获取csv文件对应的表名
excel_data = pd.read_excel("D:/d/pythonReadData/fj.xlsx", sheet_name = "表索引")
table_oldNew_Name = excel_data.loc[:, ["表名称","原索引", "新索引"]].values # loc 逐行读取
data_dict2 = {item[2]:(item[0],item[1]) for item in table_oldNew_Name}


#获取control文件内对应字段
for file in file_list:
    fi = file.split(".")[0]    # file 带有文件名后缀.csv
    with open("D:/网智天元/after-6-15/{0}".format(file), "r",encoding="utf-8") as f:
        fields = f.readline().split(",") #原先为字符串，需要处理成list
    with open("D:/d/SQL_LOADER/clt/{0}.clt".format(fi), "w", encoding="utf-8") as f:
        f.write("OPTIONS(skip = 1, rows = 64)\n")
        f.write("LOAD DATA\n")
        f.write("INFILE 'D:/d/ANSI/after-6-15/{0}'\n".format(file))
        f.write("BADFILE 'D:/d/SQL_LOADER/bad/{0}.DAT'\n".format(fi))
        f.write("TRUNCATE\n")
        f.write("INTO TABLE {0}\n".format(data_dict2[fi][0].upper()))
        f.write("Fields terminated by ','\n")
        f.write("TRAILING NULLCOLS\n")
        f.write("(\n")
        for i in range(len(fields) - 1):
            f.write("{0},\n".format(fields[i]))
        f.write("{0}\n)".format(fields[len(fields) - 1]))
    print("the clt of {0} is over!!".format(fi))

with open("D:/d/spider/sql_loaders.txt", "w", encoding="utf-8") as f :
    for file in file_list:
        fi = file.split(".")[0]
        f.write("sqlldr oracle/oracle@dbsrv23 control=D:/d/sql_loader/clt/{0}.clt log=D:/d/sql_loader/log/{1}.log\n\n".format(fi,fi))

print("over!!")