import re
# import requests
# reponse=requests.get('http://www.baidu.com')
# print(reponse.status_code)
# # print(reponse.headers)
# # print(reponse.content)
# print(reponse.content.decode('utf-8'))

import time

print(str(time.time()))

'''自定义斐波那契数列'''


def fb(n):
    a, b = 0, 1
    while b<n:
        print(b,end=' ')
        a,b=b,a+b
fb(700)

def fib2(n): # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    # return result
    print(result)

fib2(700)