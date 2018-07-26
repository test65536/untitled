import time
import pymysql
global send_times_flag
send_times_flag = 0
conn = pymysql.connect(host="10.0.0.111", user="root", passwd="zong123", db="test")
cursor = conn.cursor()

cursor.execute("select * from addrtable")   # 查询数据
data = cursor.fetchall()

cursor.execute("select time from addrtable")   # 查询time数据
data_time_col = cursor.fetchall()
print(data)   # fetchone 一条数据
print(max(data_time_col)[0])
# FC 05 03 01 FF FF 01 02 03
conn.commit()

time_start = int(time.time())  # 向下取整
while True:
    time_up_addr = []
    time_end = int(time.time())+1
    delta_time = time_end - time_start
    print(delta_time)
    for k in range(0,len(data)):
        if delta_time % data[k][0] == 0:
            print('设备[%02d] time is up, 请给设备[%02d]发消息' % (data[k][1],data[k][1]))
            print('------------------------------------------')
            time_up_addr.append(data[k][1])
            print(time_up_addr)
    if delta_time == max(data_time_col)[0]:
        print("超出最大时间了，请重新计算时间!")
        time_start = time_end
    time.sleep(1)

