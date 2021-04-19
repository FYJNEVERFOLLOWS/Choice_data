import os
import xlwings as xw  # pip install xlwings


# 1. 获取一个要重命名的文件夹的名称：
folder_name = r'D:\FYJ\Choice大数据\市场关注截面数据'
# 2. 获取那个文件夹中所有的文件名字：
file_names = os.listdir(folder_name)

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