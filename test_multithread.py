import threading
import os
import time

folder_name = r'D://FYJ//Choice大数据//多头潜能明细查询0326'

file_names = os.listdir(folder_name) # 获取该文件夹下所有文件名，返回一个列表
count = 0
def func(file_names, start, end):
    for i in range(start, end):
        print("i={}".format(i))
        print(file_names[i])
        global count
        count += 1


if __name__ == "__main__":
    print('======start======' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    interval = int(float(len(file_names)) / 4)
    thread_1 = threading.Thread(target=func,args=(file_names, 0, interval))
    thread_2 = threading.Thread(target=func, args=(file_names, interval, 2*interval))
    thread_3 = threading.Thread(target=func, args=(file_names, 2*interval, 3*interval))
    thread_4 = threading.Thread(target=func, args=(file_names, 3*interval, len(file_names)))
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    print("\ncount={}\n".format(count))

    print('======end========' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
