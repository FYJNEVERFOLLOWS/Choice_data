# import csv
# import re
# import pandas as pd
#
#
# re_date = re.compile("\d{4}/\d{1,2}/\d{1,2}")  # 用正则表达式匹配格式为xxxx/xx/xx的日期
# re_percent = re.compile("-?\d+\.\d*%") # 用正则表达式匹配正负百分数
# re_tendency = re.compile("\d{1}\.\d{2}(?!%)") # 用正则表达式匹配格式为x.xx的小数和整数，且该小数后面不能是百分号
#
# # col1 = re.findall(re_date, "日(交易时间):2020/12/30")
# # col2 = re.findall(re_percent, "预估开户变化率:-16.44%")
# # col3 = re.findall(re_tendency, "预估开户变化趋势1.58")
# # print(col1)
# # print(col2)
# # print(col3)
#
# # 将识别结果写入.csv文件
# with open("D:/FYJ/Choice大数据/first_result.csv", "w", newline='') as csvfile:
#     csv.writer(csvfile).writerow(["日（交易时间）", "预估开户变化率", "预估开户变化趋势"])
#
# with open("D:/FYJ/Choice大数据/baiduOCR结果/OCR_results_first.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines() # 得到的是一个列表
#
# last1 = ""
# last2 = ""
# last3 = ""
# with open("D:/FYJ/Choice大数据/first_result.csv", "a", newline='') as csvfile: # 按追加方式写入
#     for line in lines:
#         # print(line)
#         col1 = re.findall(re_date, line)
#         col2 = re.findall(re_percent, line)
#         col3 = re.findall(re_tendency, line)
#
#         try:
#             if col1[0] == last1 and col2[0] == last2 and col3[0] == last3:
#                 continue
#             if col1[0] == last1 and (col2[0] != last2 or col3[0] != last3):
#                 print(line + "\t数据不一致！")
#             last1 = col1[0]
#             last2 = col2[0]
#             last3 = col3[0]
#
#             csv.writer(csvfile).writerow([col1[0], col2[0], col3[0]])
#         except IndexError:
#             print(line + "写入失败！") # 定位错误
#             print(re.findall(re_date, line))
#             print(re.findall(re_percent, line))
#             print(re.findall(re_tendency, line))

####################################################################################################################


# import csv
# import re
#
#
#
# re_date = re.compile("\d{4}/\d{1,2}/\d{1,2}")  # 用正则表达式匹配格式为xxxx/xx/xx的日期
# re_ratio = re.compile("\d+\.\d+") # 用正则表达式匹配格式为x.xx的小数
#
# # col1 = re.findall(re_date, "日交易时间):2021/1/25预估基金申赎比1")
# # col2 = re.findall(re_ratio, "日交易时间):2021/1/25预估基金申赎比15.2211")
# # print(col1)
# # print(col2)
#
# # 将识别结果写入.csv文件
# with open("D:/FYJ/Choice大数据/second_result.csv", "w", newline='') as csvfile:
#     csv.writer(csvfile).writerow(["日（交易时间）", "预估基金申赎比"])
#
# with open("D:/FYJ/Choice大数据/baiduOCR结果/OCR_results_second.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines() # 得到的是一个列表
#
# last1 = ""
# last2 = ""
# last3 = ""
# with open("D:/FYJ/Choice大数据/second_result.csv", "a", newline='') as csvfile: # 按追加方式写入
#     for line in lines:
#         # print(line)
#         col1 = re.findall(re_date, line)
#         col2 = re.findall(re_ratio, line)
#         # print(col1)
#         # print(col2)
#         try:
#             if col1[0] == last1 and col2[0] == last2:
#                 continue
#             if col1[0] == last1 and col2[0] != last2:
#                 print(line + "\t数据不一致！")
#             last1 = col1[0]
#             last2 = col2[0]
#             csv.writer(csvfile).writerow([col1[0], col2[0]])
#         except IndexError:
#             print(line + "写入失败！") # 定位错误
#             print(col1)
#             print(col2)


########################################################################################################
import csv
import re



re_date = re.compile("\d{4}/\d{1,2}/\d{1,2}")  # 用正则表达式匹配格式为xxxx/xx/xx的日期
re_ratio = re.compile("\d+,\d+") # 用正则表达式匹配格式为x.xx的小数

col1 = re.findall(re_date, "日(交易时间):2021/3/4市场活跃度:11,123")
col2 = re.findall(re_ratio, "日(交易时间):2021/3/4市场活跃度:1,23")
print(col1)
print(col2)

# 将识别结果写入.csv文件
with open("D:/FYJ/Choice大数据/third_result.csv", "w", newline='') as csvfile:
    csv.writer(csvfile).writerow(["日（交易时间）", "预估基金申赎比"])

with open("D:/FYJ/Choice大数据/baiduOCR结果/OCR_results_third.txt", "r", encoding="utf-8") as file:
    lines = file.readlines() # 得到的是一个列表

last1 = ""
last2 = ""
last3 = ""
with open("D:/FYJ/Choice大数据/third_result.csv", "a", newline='') as csvfile: # 按追加方式写入
    for line in lines:
        # print(line)
        col1 = re.findall(re_date, line)
        col2 = re.findall(re_ratio, line)
        # print(col1)
        # print(col2)
        try:
            if col1[0] == last1 and col2[0] == last2:
                continue
            if col1[0] == last1 and col2[0] != last2:
                print(line + "\t数据不一致！")
            last1 = col1[0]
            last2 = col2[0]
            csv.writer(csvfile).writerow([col1[0], col2[0]])
        except IndexError:
            print(line + "写入失败！") # 定位错误
            print(col1)
            print(col2)