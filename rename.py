import os
import time

import xlrd
import pandas as pd
import fsspec
import xlwings as xw  # pip install xlwings


# 1. 获取一个要重命名的文件夹的名称：
folder_name = 'D://FYJ//Choice大数据//社区活跃度明细查询0401'
# 2. 获取那个文件夹中所有的文件名字：
file_names = os.listdir(folder_name)

# for i, filename in enumerate(file_names):
#     # 枚举的是(i, filename)构成的元组
#     df = pd.read_excel(folder_name+'/'+filename, engine='openpyxl')
#     fileid = df.iloc[[0], [1]].values[0][0]  # 返回1行1列单元格的值
#     filedate = str(df.iloc[[0], [3]].values[0][0])[:10].replace('-', '') # 建议用to_numpy()替代values
#     print(filename, fileid, filedate)
#     old_file_name = os.path.join(folder_name, filename)
#     new_filename = fileid + '-timeseries-' + filedate + '.xlsx'
#     print(new_filename)
#     new_file_name = os.path.join(folder_name, new_filename)
#     try:
#         os.rename(old_file_name, new_file_name)
#     except FileExistsError:
#         print(new_filename + " exists!")

for i, filename in enumerate(file_names):
    old_file_name = os.path.join(folder_name, filename)
    new_filename = filename.replace("20210401", "20210326")
    print(new_filename)
    new_file_name = os.path.join(folder_name, new_filename)
    os.rename(old_file_name, new_file_name)

