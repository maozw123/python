def func1(a):
    print(f'a={a}')

import time
def log1(func):
    # 增加日志功能
    f = open('log.txt', mode='a', encoding='utf-8')
    time_str = time.asctime()
    # 通过函数得到函数名__name__
    func_name = func.__name__
    f.write(time_str + '\t' + func_name + '\n')
    f.close()
def funcOut(func):
    def funcIn(a):
        log1(func)
        func(a)
    return funcIn
# @funcOut
# func1 = funcOut(func1(10))
func1(10)