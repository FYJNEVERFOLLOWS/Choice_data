# -*- coding:utf-8 -*-
import json
import os
import numpy as np
import pandas as pd
import pymongo
import xlrd


client = pymongo.MongoClient("mongodb://stkemowriter:stkemo@192.168.1.119:27017/")
db = client['zcs']
col = db['factor_stock_maremo_day']

# df = pd.read_excel(r'D:\FYJ\Choice大数据\市场全景数据\市场情绪表.xlsx', engine='openpyxl')
#
# for index, row in df.iterrows():
#     date = row['日（交易时间）']
#     print(date)
#     doc = {
#         'date': str(date)[:10],
#         'rate': row['预估开户变化率'],
#         'trend': row['预估开户变化趋势'],
#         'ratio': row['预估基金申赎比'],
#         'activity': row['市场活跃度']
#     }
#     print(doc)
#     print(json.dumps(doc, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False))
#     # print(col.insert(doc))


folder_name = r'D://FYJ//Choice大数据//市场全景数据'

df1 = pd.read_excel(folder_name + '/first_result_rest.xlsx', engine='openpyxl')
# print(df1)
df2 = pd.read_excel(folder_name + '/second_result.xlsx', engine='openpyxl')
# print(df2)
df3 = pd.read_excel(folder_name + '/third_result.xlsx', engine='openpyxl')
# print(df3)

for index, row in df1.iterrows():
    # 枚举的是(index, row)构成的元组
    # print(row)
    # print(row['代码'])
    # print(str(row['统计日期'])[:10].replace('-', ''))
    date = row['日（交易时间）']
    # print(date)
    # market = df_market[(df_market['代码']==id) & (str(df_market['统计日期']).replace('-', '')==date)]
    # market = df_market[(df_market['代码']==id) & (str(df_market['统计日期']).replace('-', '')==date)]
    second = df2[df2['日（交易时间）'] == date]
    third = df3[df3['日（交易时间）'] == date]

    # print(second['预估基金申赎比'].to_numpy())
    # print(third['市场活跃度'].to_numpy())
    doc = {
        'date': str(date)[:10],
        'rate': row['预估开户变化率'],
        'trend': row['预估开户变化趋势'],
        'ratio': "--" if second.empty else second['预估基金申赎比'].to_numpy()[0],
        'activity': "--" if third.empty else int(third['市场活跃度'].to_numpy()[0])
    }
    print(doc)
    print(json.dumps(doc, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False))
    print(col.insert(doc))
