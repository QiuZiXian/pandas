# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2019/7/10  21:52
# @abstract    :

users_dict_data = {}
items_dict_data = {}
with open("D:/d/lijuan/ep_ratings.txt", 'r', encoding="utf-8") as f:
	for line in f.readlines():
		# print(line, len(line), type(line))
		# for i in line.split(" "):
		# 	print(i)
		user_item_rating = line.split(' ')
		# 构建用户索引字典，每个用户都评过哪些电影
		if user_item_rating[0] in users_dict_data:
			users_dict_data[user_item_rating[0]].append((user_item_rating[1], user_item_rating[2])) #(电影id，评分)
		else:
			users_dict_data[user_item_rating[0]] = [(user_item_rating[1], user_item_rating[2])]
		# 构建电影索引字典，每部电影都有哪些用户看过
		if user_item_rating[1] in items_dict_data:
			items_dict_data[user_item_rating[1]].append((user_item_rating[0], user_item_rating[2])) #（用户id，评分）
		else:
			items_dict_data[user_item_rating[1]] = [(user_item_rating[0], user_item_rating[2])]

# 分析用户，评分数从1-9，大于10；11种情况
users = users_dict_data.keys() # dict_keys数据格式
user_total = [len(users_dict_data[user_id]) for user_id in users] # 每个有评分的用户，各自评了多少部电影
scatter = [user_total.count(i) for i in range(1, 10)]  # 只评价了一部、2部。。。9部电影的用户各有多少
scatter.append(len(user_total) - sum(scatter)) # 1-9，大于9, 0
scatter.append(40163 - sum(scatter))
print("只评价了1部、2部。。。9部, 大于9, 0 电影的用户各有多少：")
print(scatter)

# 分析项目，对其的评分用户个数从1-9，大于9；11种情况
items = items_dict_data.keys()
item_total = [len(items_dict_data[item_id]) for item_id in items] # 每个有评分的项目，各自有多少用户对其进行评分
scatter = [item_total.count(i) for i in range(1, 10)]  # 只拥有一个、2个、、、9个用户；大于9个用户评分的项目个数
scatter.append(len(item_total) - sum(scatter)) # 1-9，大于9, 0
scatter.append(139738 - sum(scatter))
print("只拥有一个、2个、、、9个用户；大于9个用户评分的项目个数：")
print(scatter)

more_dict = {}
with open("D:/d/lijuan/less_than_5.txt", 'w', encoding="utf-8") as f: #小于5，不包括5
	for user_id in users:
		if len(users_dict_data[user_id]) < 5:
			for item in users_dict_data[user_id]:
				f.write("{0} {1} {2}\n".format(user_id, item[0], item[1]))
		else:
			more_dict[user_id] = users_dict_data[user_id]
print("less_than_5.txt is out over!!")

with open("D:/d/lijuan/more_than_5.txt", 'w', encoding="utf-8") as f:
	for user_id, value in more_dict.items():
			f.write("{0} {1} {2}\n".format(user_id, value[0], value[1]))
print("more_than_5.txt is out over!!")

