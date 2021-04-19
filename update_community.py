import os
import xlsxwriter
import xlwt
import pandas as pd

# new_df["统计日期"].dt.strftime('%Y-%m-%d')去掉excel中的时分秒


folder_name3 = r'D:\FYJ\Choice大数据\社区活跃度明细查询0331'

df_insert = pd.read_excel(r'D://FYJ//Choice大数据//社区截面数据//20210401截面数据.xls')

# filename = r"000001.SZ-timeseries-20210323.xlsx"
# print(filename.split("-")[0])
# df = pd.read_excel(r"D:\FYJ\Choice大数据\多头潜能明细查询0324\000001.SZ-timeseries-20210323.xlsx",engine='openpyxl')
# insertRow = df_insert[df_insert["代码"].isin([filename.split("-")[0]])]
# print(df_insert[df_insert["代码"].isin([filename.split("-")[0]])])
# new_df = pd.concat([insertRow,df],ignore_index = True)
# new_df.to_excel("D:\FYJ\Choice大数据\多头潜能明细查询0325\{}".format(filename), engine='xlsxwriter')
# new_df.to_excel("D:\FYJ\Choice大数据\多头潜能明细查询0325\{}".format(filename))


file_names1 = os.listdir(folder_name3)
for i, filename in enumerate(file_names1):
    if filename.endswith(".xls"):
        # print(df_insert[df_insert["代码"].isin([filename.split("-")[0]])]) # 输出指定列等于目标值的行
        print(filename.split("-")[0])
        df = pd.read_excel(folder_name3+'//'+filename)
        insertRow = df_insert[df_insert["代码"].isin([filename.split("-")[0]])]
        print(df_insert[df_insert["代码"].isin([filename.split("-")[0]])])
        new_df = pd.concat([insertRow,df],ignore_index = True)
        new_df.to_excel("D:\FYJ\Choice大数据\社区活跃度明细查询0401\{}x".format(filename), engine='xlsxwriter')
    if filename.endswith(".xlsx"):
        print(filename.split("-")[0])
        df = pd.read_excel(folder_name3+'//'+filename, engine='openpyxl')
        insertRow = df_insert[df_insert["代码"].isin([filename.split("-")[0]])]
        print(df_insert[df_insert["代码"].isin([filename.split("-")[0]])])
        new_df = pd.concat([insertRow, df], ignore_index=True)
        new_df.to_excel("D:\FYJ\Choice大数据\社区活跃度明细查询0401\{}".format(filename), engine='xlsxwriter')

# df1 = pd.read_csv(r'D://FYJ//Choice大数据//test//000001.SZ-时间序列-20210323.xls')
# df6 = pd.read_excel(r'D:/source.xlsx', usecols='A:D,H')
