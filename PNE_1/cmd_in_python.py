# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2019/8/9  15:13
# @abstract    :

# cmd

import os
import pandas as pd

def get():
    #获取csv文件对应的表名
    excel_index = pd.read_excel("D:/d/pythonReadData/fj.xlsx", sheet_name = "表索引")
    table_oldNew_Name = excel_index.loc[:, ["表名称","原索引", "新索引"]].values # loc 逐行读取
    data_dict2 = {item[2]:(item[0],item[1]) for item in table_oldNew_Name}


def clt_handls_1():
    with open("D:/d/spider/qixin/sql_loaders.txt", "r", encoding="utf-8") as f:
        sqls = [line for line in f.readlines() if line and line != '\n']
# =============================================================================
# #    for i in range(len(sqls)):
# #        print(i, sqls[i])
# =============================================================================
    i = 4 # 22; 72
    os.chdir("e:/app/admin01/product/11.2.0/dbhome_1/bin")
    os.system("{0} -p ".format(sqls[i])) #macro.mcr
    print("{0}:{1} over!".format(i, sqls[i]))

clt_handls_1()