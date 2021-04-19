
import pandas as pd

# with open("D:/FYJ/Choice大数据/third_result.csv", "r+", newline='') as csvfile:
#     lines = csvfile.readlines()  # 得到的是一个列表
#     for line in lines:
#         print(line)

df = pd.read_excel("D:/FYJ/Choice大数据/社区活跃度明细查询0401/000036.SZ-timeseries-20210326.xlsx", skipfooter=6,
                              engine='openpyxl') # 要先去掉首行




for index, row in df.iterrows():
    print(row['统计日期'])