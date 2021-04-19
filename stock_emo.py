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

folder_name = r'D://FYJ//Choice大数据//多头截面数据'
market_folder_name = r'D://FYJ//Choice大数据//市场关注截面数据'
commu_folder_name = r'D://FYJ//Choice大数据//社区截面数据'

file_names = os.listdir(folder_name)

for i, filename in enumerate(file_names):

    df = pd.read_excel(folder_name + '//' + filename, skipfooter=6)  # 不对倒数6行进行解析
    # print(df)
    df_market = pd.read_excel(market_folder_name + '//' + filename, skipfooter=6)
    df_commu = pd.read_excel(commu_folder_name + '//' + filename, skipfooter=6)  # 不对倒数6行进行解析
    # print(str(df_market['统计日期']).replace('-', ''))
    for index, row in df.iterrows():
        # 枚举的是(index, row)构成的元组
        # print(row)
        # print(row['代码'])
        # print(str(row['统计日期'])[:10].replace('-', ''))
        id = row['代码']
        date = row['统计日期']
        # market = df_market[(df_market['代码']==id) & (str(df_market['统计日期']).replace('-', '')==date)]
        # market = df_market[(df_market['代码']==id) & (str(df_market['统计日期']).replace('-', '')==date)]
        market = df_market[df_market['代码'] == id]
        # print(market)
        # print(market.iloc[[0], [1]].to_numpy()[0][0]) # 建议用to_numpy()替代values
        # print(market.iloc[[0], [-2]].to_numpy()[0][0]) # 建议用to_numpy()替代values
        commu = df_commu[df_commu['代码'] == id]
        # print("commu")
        # print(commu)
        # print(
        #     "id:{}, name:{}, date:{}, isExchangeDay:{}, industry:{}, select_idx:{}, select_idxrk:{}, select_change:{}, select_changerk:{}, hot_idx:{}, hot_idxrk:{}, hot_change:{}, hot_changerk:{}, "
        #     "access_idx:{}, access_idxrk:{}, access_change:{}, access_changerk:{}, focus_idx:{}, focus_idxrk:{}, focus_change:{}, focus_changerk:{}, "
        #     "bar_idx:{}, bar_idxrk:{}, bar_change:{}, bar_changerk:{}, news_idx:{}, news_idxrk:{}, news_change:{}, news_changerk:{}, notice_idx:{}, notice_idxrk:{}, notice_change:{}, notice_changerk:{}, "
        #     "report_idx:{}, report_idxrk:{}, report_change:{}, report_changerk:{}")

        doc = {
            'code': id,
            'name': row['证券简称'],
            'date': str(date)[:10],  # 去掉replace
            'select_idx': row[3],
            'select_idxrk': np.nan,
            'select_change': row[4],
            'select_changerk': row[5],
            'hot_idx': row[6],
            'hot_idxrk': np.nan,
            'hot_change': row[7],
            'hot_changerk': row[8],
            'access_idx': None if market.empty or type(market.iloc[[0], [3]].to_numpy()[0][0]) == str else float(
                market.iloc[[0], [3]].to_numpy()[0][0]),
            'access_idxrk': np.nan,
            'access_change': None if market.empty or type(market.iloc[[0], [4]].to_numpy()[0][0]) == str else float(
                market.iloc[[0], [4]].to_numpy()[0][0]),
            'access_changerk': None if market.empty or type(market.iloc[[0], [5]].to_numpy()[0][0]) == str else int(
                market.iloc[[0], [5]].to_numpy()[0][0]),
            'focus_idx': None if market.empty or type(market.iloc[[0], [6]].to_numpy()[0][0]) == str else float(
                market.iloc[[0], [6]].to_numpy()[0][0]),
            'focus_idxrk': np.nan,
            'focus_change': None if market.empty or type(market.iloc[[0], [7]].to_numpy()[0][0]) == str else float(
                market.iloc[[0], [7]].to_numpy()[0][0]),
            'focus_changerk': None if market.empty or type(market.iloc[[0], [8]].to_numpy()[0][0]) == str else int(
                market.iloc[[0], [8]].to_numpy()[0][0]),
            'bar_idx': None if commu.empty or type(commu.iloc[[0], [3]].to_numpy()[0][0]) == str else float(
                commu.iloc[[0], [3]].to_numpy()[0][0]),
            'bar_idxrk': np.nan,
            'bar_change': None if commu.empty or type(commu.iloc[[0], [4]].to_numpy()[0][0]) == str else float(
                commu.iloc[[0], [4]].to_numpy()[0][0]),
            'bar_changerk': None if commu.empty or type(commu.iloc[[0], [5]].to_numpy()[0][0]) == str else int(
                commu.iloc[[0], [5]].to_numpy()[0][0]),
            'news_idx': None if commu.empty or type(commu.iloc[[0], [6]].to_numpy()[0][0]) == str else float(
                commu.iloc[[0], [6]].to_numpy()[0][0]),
            'news_idxrk': np.nan,
            'news_change': None if commu.empty or type(commu.iloc[[0], [7]].to_numpy()[0][0]) == str else float(
                commu.iloc[[0], [7]].to_numpy()[0][0]),
            'news_changerk': None if commu.empty or type(commu.iloc[[0], [8]].to_numpy()[0][0]) == str else int(
                commu.iloc[[0], [8]].to_numpy()[0][0]),
            'notice_idx': None if commu.empty or type(commu.iloc[[0], [9]].to_numpy()[0][0]) == str else float(
                commu.iloc[[0], [9]].to_numpy()[0][0]),
            'notice_idxrk': np.nan,
            'notice_change': None if commu.empty or type(commu.iloc[[0], [10]].to_numpy()[0][0]) == str else float(
                commu.iloc[[0], [10]].to_numpy()[0][0]),
            'notice_changerk': None if commu.empty or type(commu.iloc[[0], [11]].to_numpy()[0][0]) == str else int(
                commu.iloc[[0], [11]].to_numpy()[0][0]),
            'report_idx': None if commu.empty or type(commu.iloc[[0], [12]].to_numpy()[0][0]) == str else float(
                commu.iloc[[0], [12]].to_numpy()[0][0]),
            'report_idxrk': np.nan,
            'report_change': None if commu.empty or type(commu.iloc[[0], [13]].to_numpy()[0][0]) == str else float(
                commu.iloc[[0], [13]].to_numpy()[0][0]),
            'report_changerk': None if commu.empty or type(commu.iloc[[0], [14]].to_numpy()[0][0]) == str else int(
                commu.iloc[[0], [14]].to_numpy()[0][0]),
        }
        print(doc)
        print(json.dumps(doc, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False))
        print(col.insert(doc))
