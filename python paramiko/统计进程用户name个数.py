# 统计进程个数 用户

import os

# os.system("ls")
# os.popen()
result = {}
with os.popen("ps aux") as f:
    for i in f.readlines():
        # print (i)
        user = i.split(' ', 1) ## split 按照指定字符分割 1 代表分割一次
        print(user[0])
        if len(user) >= 2:
            if user[0] in result:
                result[user[0]] += 1
            else:
                result[user[0]] = 1
print(result)