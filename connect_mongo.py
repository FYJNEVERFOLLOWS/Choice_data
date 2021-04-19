# -*- coding:utf-8 -*-
import json
import os
import threading
import time

import numpy as np
import pandas as pd
import pymongo
import xlrd


client = pymongo.MongoClient("mongodb://stkemowriter:stkemo@192.168.1.119:27017/")
db = client['zcs']
col = db['factor_stock_emo_day']
# coll_names = db.list_collection_names(session=None)
# doc = {
#             'id': "111.SZ",
#             'name': '证券简称',
#             'date': '20210312',
#             'isExchangeDay': '是'
# }
# print(col.insert(doc))
# for x in col.find(): # 查询集合中所有数据
#   print(x)

folder_name = r'D://FYJ//Choice大数据//多头潜能明细查询0326'
market_folder_name = r'D://FYJ//Choice大数据//市场关注度明细查询0401'
commu_folder_name = r'D://FYJ//Choice大数据//社区活跃度明细查询0401'
file_names = os.listdir(folder_name)


def func(file_names, start, end):
    for i, filename in enumerate(file_names):
        if i < start:
            continue
        if i >= end:
            break
        id = filename.split("-")[0]

        df = pd.read_excel(folder_name + '//' + filename, skipfooter=6,
                           engine='openpyxl')  # 不对倒数6行进行解析
        # print(df)
        df_market = pd.read_excel(market_folder_name + '//' + filename, skipfooter=6,
                                  engine='openpyxl')
        df_commu = pd.read_excel(commu_folder_name + '//' + filename, skipfooter=6,
                           engine='openpyxl')  # 不对倒数6行进行解析
        # print(str(df_market['统计日期']).replace('-', ''))
        for index, row in df.iterrows():
            # 枚举的是(index, row)构成的元组
            # print(row)
            # print(row['代码'])
            # print(str(row['统计日期'])[:10].replace('-', ''))
            date = row['统计日期']
            # market = df_market[(df_market['代码']==id) & (str(df_market['统计日期']).replace('-', '')==date)]
            # market = df_market[(df_market['代码']==id) & (str(df_market['统计日期']).replace('-', '')==date)]
            market = df_market[df_market['代码'] == id]
            market = market[market['统计日期'] == date]
            # print(market)
            # print(market.iloc[[0], [1]].to_numpy()[0][0]) # 建议用to_numpy()替代values
            # print(market.iloc[[0], [-2]].to_numpy()[0][0]) # 建议用to_numpy()替代values
            commu = df_commu[df_commu['代码'] == id]
            commu = commu[commu['统计日期'] == date]
            # print("commu")
            # print(commu)
            # print(
            #     "id:{}, name:{}, date:{}, isExchangeDay:{}, industry:{}, select_idx:{}, select_idxrk:{}, select_change:{}, select_changerk:{}, hot_idx:{}, hot_idxrk:{}, hot_change:{}, hot_changerk:{}, "
            #     "access_idx:{}, access_idxrk:{}, access_change:{}, access_changerk:{}, focus_idx:{}, focus_idxrk:{}, focus_change:{}, focus_changerk:{}, "
            #     "bar_idx:{}, bar_idxrk:{}, bar_change:{}, bar_changerk:{}, news_idx:{}, news_idxrk:{}, news_change:{}, news_changerk:{}, notice_idx:{}, notice_idxrk:{}, notice_change:{}, notice_changerk:{}, "
            #     "report_idx:{}, report_idxrk:{}, report_change:{}, report_changerk:{}")

            doc = {
                'id': id,
                'name': row['证券简称'],
                'date': str(date)[:10].replace('-', ''), # 去掉replace
                'isExchangeDay': row['是否交易日'],
                'industry': row['申万一级行业分类'],
                'select_idx': row['最新指数'],
                'select_idxrk': row['指数排名'],
                'select_change': row['最新指数变化'],
                'select_changerk': row['指数变化排名'],
                'hot_idx': row['最新指数.1'],
                'hot_idxrk': row['指数排名.1'],
                'hot_change': row['最新指数变化.1'],
                'hot_changerk': row['指数变化排名.1'],
                'access_idx': "--" if market.empty or type(market.iloc[[0], [4]].to_numpy()[0][0]) == str else float(market.iloc[[0], [4]].to_numpy()[0][0]),
                'access_idxrk': "--" if market.empty or type(market.iloc[[0], [-2]].to_numpy()[0][0]) == str else int(market.iloc[[0], [-2]].to_numpy()[0][0]),
                'access_change': "--" if market.empty or type(market.iloc[[0], [5]].to_numpy()[0][0]) == str else float(market.iloc[[0], [5]].to_numpy()[0][0]),
                'access_changerk': "--" if market.empty or type(market.iloc[[0], [6]].to_numpy()[0][0]) == str else int(market.iloc[[0], [6]].to_numpy()[0][0]),
                'focus_idx': "--" if market.empty or type(market.iloc[[0], [7]].to_numpy()[0][0]) == str else float(market.iloc[[0], [7]].to_numpy()[0][0]),
                'focus_idxrk': "--" if market.empty or type(market.iloc[[0], [-1]].to_numpy()[0][0]) == str else int(market.iloc[[0], [-1]].to_numpy()[0][0]),
                'focus_change': "--" if market.empty or type(market.iloc[[0], [8]].to_numpy()[0][0]) == str else float(market.iloc[[0], [8]].to_numpy()[0][0]),
                'focus_changerk': "--" if market.empty or type(market.iloc[[0], [9]].to_numpy()[0][0]) == str else int(market.iloc[[0], [9]].to_numpy()[0][0]),
                'bar_idx': "--" if commu.empty or type(commu.iloc[[0], [4]].to_numpy()[0][0]) == str else float(commu.iloc[[0], [4]].to_numpy()[0][0]),
                'bar_idxrk': "--" if commu.empty or type(commu.iloc[[0], [-4]].to_numpy()[0][0]) == str else int(commu.iloc[[0], [-4]].to_numpy()[0][0]),
                'bar_change': "--" if commu.empty or type(commu.iloc[[0], [5]].to_numpy()[0][0]) == str else float(commu.iloc[[0], [5]].to_numpy()[0][0]),
                'bar_changerk': "--" if commu.empty or type(commu.iloc[[0], [6]].to_numpy()[0][0]) == str else int(commu.iloc[[0], [6]].to_numpy()[0][0]),
                'news_idx': "--" if commu.empty or type(commu.iloc[[0], [7]].to_numpy()[0][0]) == str else float(commu.iloc[[0], [7]].to_numpy()[0][0]),
                'news_idxrk': "--" if commu.empty or type(commu.iloc[[0], [-3]].to_numpy()[0][0]) == str else int(commu.iloc[[0], [-3]].to_numpy()[0][0]),
                'news_change': "--" if commu.empty or type(commu.iloc[[0], [8]].to_numpy()[0][0]) == str else float(commu.iloc[[0], [8]].to_numpy()[0][0]),
                'news_changerk': "--" if commu.empty or type(commu.iloc[[0], [9]].to_numpy()[0][0]) == str else int(commu.iloc[[0], [9]].to_numpy()[0][0]),
                'notice_idx': "--" if commu.empty or type(commu.iloc[[0], [10]].to_numpy()[0][0]) == str else float(commu.iloc[[0], [10]].to_numpy()[0][0]),
                'notice_idxrk': "--" if commu.empty or type(commu.iloc[[0], [-2]].to_numpy()[0][0]) == str else int(commu.iloc[[0], [-2]].to_numpy()[0][0]),
                'notice_change': "--" if commu.empty or type(commu.iloc[[0], [11]].to_numpy()[0][0]) == str else float(commu.iloc[[0], [11]].to_numpy()[0][0]),
                'notice_changerk': "--" if commu.empty or type(commu.iloc[[0], [12]].to_numpy()[0][0]) == str else int(commu.iloc[[0], [12]].to_numpy()[0][0]),
                'report_idx': "--" if commu.empty or type(commu.iloc[[0], [13]].to_numpy()[0][0]) == str else float(commu.iloc[[0], [13]].to_numpy()[0][0]),
                'report_idxrk': "--" if commu.empty or type(commu.iloc[[0], [-1]].to_numpy()[0][0]) == str else int(commu.iloc[[0], [-1]].to_numpy()[0][0]),
                'report_change': "--" if commu.empty or type(commu.iloc[[0], [14]].to_numpy()[0][0]) == str else float(commu.iloc[[0], [14]].to_numpy()[0][0]),
                'report_changerk': "--" if commu.empty or type(commu.iloc[[0], [15]].to_numpy()[0][0]) == str else int(commu.iloc[[0], [15]].to_numpy()[0][0]),
            }
            print(doc)
            print(json.dumps(doc, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False))
            print(col.insert(doc))


if __name__ == "__main__":
    print('======start======' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    thread_1 = threading.Thread(target=func,args=(file_names, 0, 875))
    thread_2 = threading.Thread(target=func, args=(file_names, 875, 1750))
    thread_3 = threading.Thread(target=func, args=(file_names, 1750, 2625))
    thread_4 = threading.Thread(target=func, args=(file_names, 2625, 3467))
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()

    print('======end========' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))