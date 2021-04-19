import os
import xlsxwriter
import xlwt
import pandas as pd
from threading import Thread

# new_df["统计日期"].dt.strftime('%Y-%m-%d')去掉excel中的时分秒
folder_name3 = r'D:\FYJ\Choice大数据\社区活跃度明细查询'

df_insert = pd.read_excel(r'D://FYJ//Choice大数据//社区截面数据//20210331截面数据.xls')
file_names = os.listdir(folder_name3)


def func1(start, end):
    for i in range(start, end):
        print(i)
        i += 1
        filename = file_names[i]
        if filename.endswith(".xls"):
            # print(df_insert[df_insert["代码"].isin([filename.split("-")[0]])]) # 输出指定列等于目标值的行
            print(filename.split("-")[0])
            df = pd.read_excel(folder_name3+'//'+filename)
            insertRow = df_insert[df_insert["代码"].isin([filename.split("-")[0]])]
            print(df_insert[df_insert["代码"].isin([filename.split("-")[0]])])
            new_df = pd.concat([insertRow,df],ignore_index = True)
            new_df.to_excel(r"D:\FYJ\Choice大数据\test\{}x".format(filename), engine='xlsxwriter')
        if filename.endswith(".xlsx"):
            print(filename.split("-")[0])
            df = pd.read_excel(folder_name3+'//'+filename, engine='openpyxl')
            insertRow = df_insert[df_insert["代码"].isin([filename.split("-")[0]])]
            print(df_insert[df_insert["代码"].isin([filename.split("-")[0]])])
            new_df = pd.concat([insertRow, df], ignore_index=True)
            new_df.to_excel(r"D:\FYJ\Choice大数据\test\{}".format(filename), engine='xlsxwriter')

def func2(start, end):
    for i in range(start, end):
        print(i)
        i += 1
        filename = file_names[i]
        if filename.endswith(".xls"):
            # print(df_insert[df_insert["代码"].isin([filename.split("-")[0]])]) # 输出指定列等于目标值的行
            print(filename.split("-")[0])
            df = pd.read_excel(folder_name3 + '//' + filename)
            insertRow = df_insert[df_insert["代码"].isin([filename.split("-")[0]])]
            print(df_insert[df_insert["代码"].isin([filename.split("-")[0]])])
            new_df = pd.concat([insertRow, df], ignore_index=True)
            new_df.to_excel(r"D:\FYJ\Choice大数据\test\{}x".format(filename), engine='xlsxwriter')
        if filename.endswith(".xlsx"):
            print(filename.split("-")[0])
            df = pd.read_excel(folder_name3 + '//' + filename, engine='openpyxl')
            insertRow = df_insert[df_insert["代码"].isin([filename.split("-")[0]])]
            print(df_insert[df_insert["代码"].isin([filename.split("-")[0]])])
            new_df = pd.concat([insertRow, df], ignore_index=True)
            new_df.to_excel(r"D:\FYJ\Choice大数据\test\{}".format(filename), engine='xlsxwriter')

# 创建线程1，不指定参数
thread_1 = Thread(target=func1(0, 700))
# 启动线程1
thread_1.start()

# 创建线程2，不指定参数
thread_2 = Thread(target=func2(700, 1400))
# 启动线程02
thread_2.start()