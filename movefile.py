# coding=utf-8
import os
import shutil
import traceback

src_path = 'D://FYJ//Choice大数据//多头潜能明细查询'
dst_path = 'D:\FYJ\Choice大数据//test'
file_names = os.listdir(src_path)

for i, filename in enumerate(file_names):
    # 枚举的是(i, filename)构成的元组
    if filename.endswith("0324.xls"):
        try:
            # cmd = 'chmod -R +x ' + src_path
            # os.popen(cmd)
            f_src = os.path.join(src_path, filename)
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
            f_dst = os.path.join(dst_path, filename)
            shutil.move(f_src, f_dst)
        except Exception as e:
            print
            'move_file ERROR: ', e
            traceback.print_exc()

