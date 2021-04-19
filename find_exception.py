import os

folder_name = r'D://FYJ//Choice大数据//多头潜能明细查询0326'
market_folder_name = r'D://FYJ//Choice大数据//市场关注度明细查询0401'
commu_folder_name = r'D://FYJ//Choice大数据//社区活跃度明细查询0401'

file_names = os.listdir(folder_name)
for i, filename in enumerate(file_names):
    if not os.path.exists(market_folder_name + '//' + filename):
        print(market_folder_name + '//' + filename + " NOT EXISTS!")

    if not os.path.exists(commu_folder_name + '//' + filename):
        print(commu_folder_name + '//' + filename + " NOT EXISTS!")


