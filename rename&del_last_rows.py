import os
import time

import xlrd
import pandas as pd
import fsspec
import xlwings as xw  # pip install xlwings


# 1. 获取一个要重命名的文件夹的名称：
folder_name = 'D://FYJ//Choice大数据//多头潜能明细查询'
# 2. 获取那个文件夹中所有的文件名字：
file_names = os.listdir(folder_name)

for i, filename in enumerate(file_names):
    # 枚举的是(i, filename)构成的元组
    df = pd.read_excel(folder_name+'/'+filename)
    fileid = df.iloc[[0], [0]].values[0][0]  # 返回1行1列单元格的值
    filedate = str(df.iloc[[0], [2]].values[0][0])[:10].replace('-', '')

    old_file_name = os.path.join(folder_name, filename)
    new_filename = fileid + '-timeseries-' + filedate + '.xls'
    print(new_filename)
    new_file_name = os.path.join(folder_name, new_filename)
    try:
        os.rename(old_file_name, new_file_name)
    except FileExistsError:
        print(new_filename + " exists!")


app = xw.App(visible=True, add_book=False)  # 创建App
# visible参数控制创建文件时可见的属性

app.display_alerts = False  # 警告提示，不显示Excel消息框
app.screen_updating = False  # 关闭屏幕更新,可加快宏的执行速度

for i, filename in enumerate(file_names):
    wb = app.books.open(folder_name+'/'+filename)
    sheet = wb.sheets[0]  # 选中sheet1
    sheet.range('$A$1').api.EntireRow.Delete()
    wb.save()
    wb.close()
app.quit()
# for i, filename in enumerate(file_names):
#     old_file_name = os.path.join(folder_name, filename)
#     new_filename = filename.replace("20210329", "20210330")
#     print(new_filename)
#     new_file_name = os.path.join(folder_name, new_filename)
#     os.rename(old_file_name, new_file_name)
#     time.sleep(0.5)
