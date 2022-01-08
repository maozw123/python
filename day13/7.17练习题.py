'''基础题：
1.封装自定一个函数，可以将Iterable对象中的所有数据写到目标文件file中，如果Iterable中存储的不是字符串，转换为字符串处理
def write_lines(file,Iterable):
	pass

2.自定义一个函数，可以实现文件的复制（先读取目标文件，然后写入新文件）
比如：def copyfile(file) 将file复制一份，被复制出来的文件名为file_副本.后缀

提升题：

3.打印某个文件夹内所有的的文件名

4.尝试将一个文件夹内所有的.py文件名前都添加上你的名字做前缀(注意文件先备份)
例如：test01.py  ->  xxx_test01.py

5.封装一个函数，可以实现类似操作系统的模糊查询功能(输入一个关键字，可以展示目标文件夹中包含关键字的所有文件)


6.统计某个文件夹内所有.py文件中的代码行数'''
# 1.封装自定一个函数，可以将Iterable对象中的所有数据写到目标文件file中，
# 如果Iterable中存储的不是字符串，转换为字符串处理
def func1(file,Iterable):
    with open("file",mode='a',encoding='utf-8') as f:
        for i in Iterable:
            # print(str(i),end=' ')
            # print(type(str(i)))
            f.write(str(i))
# func1((1,2,'a4',4,'TYU'))

# 2.自定义一个函数，可以实现文件的复制（先读取目标文件，然后写入新文件）
# 比如：def copyfile(file) 将file复制一份，被复制出来的文件名为file_副本.后缀
def copyfile(file):
    f1=open(file,'r',encoding='utf-8')
    t=file.rpartition('.')
    new_name=t[0]+'_副本'+t[1]+t[2]
    f2=open(new_name,'w',encoding='utf-8')
    for i in f1:
        f2.write(i)
    f1.close()
    f2.close()
# copyfile("7.17练习题.py")

# 3.打印某个文件夹内所有的的文件名
import os
def print_file(dirpath):
    for i in os.listdir(dirpath):
        path=dirpath+'\\'+i
        if os.path.isfile(path):
            print(path)
        elif os.path.isdir(path):
            print_file(path)
# print_file('E:\python\study\python基础')
# 4.尝试将一个文件夹内所有的.py文件名前都添加上你的名字做前缀(注意文件先备份)
# 例如：test01.py  ->  xxx_test01.py
def print_file_add_name(dirpath):
    for i in os.listdir(dirpath):
        path=dirpath+'\\'+i
        if os.path.isfile(path) and path.endswith('.py'):
            #在绝对路径里面修改文件名
            os.rename(path,dirpath+'\\'+'梁小秋_'+i)
        elif os.path.isdir(path):
            print_file_add_name(path)
# print_file_add_name('E:\python\study\python基础\day1')

# 5.封装一个函数，可以实现类似操作系统的模糊查询功能
# (输入一个关键字，可以展示目标文件夹中包含关键字的所有文件)
def show_kw_file(kw,dirpath,):
    for i in os.listdir(dirpath):
        path=dirpath+'\\'+i
        if os.path.isfile(path) and path.endswith('.py'):
            f1 = open(path, 'r', encoding='utf-8')
            content=f1.read()
            if kw in i or kw in content:
                print(path)
        elif os.path.isdir(path):
            show_kw_file(kw,path)
# show_kw_file('作业',r'E:\python\study\python基础\day12')

# 6.统计某个文件夹内所有.py文件中的代码行数
import os
# total_count = 0
count_list = []
def show_all_files(dirpath):
    files = os.listdir(dirpath)
    for f in files:
        new_path = dirpath + '/' + f
        if os.path.isfile(new_path) and new_path.endswith('.py'):
            # print(new_path)
            count = get_count(new_path)
            count_list.append(count)
            #调用统计单个文件代码行数的功能
        elif os.path.isdir(new_path):
            show_all_files(new_path)

def get_count(file):
    count = 0
    f = open(file,'r',encoding='utf-8')
    for s in f:
        #单行内容中，带#的不考虑
        # if '#' not in s:
        count += 1
    f.close()
    return count
show_all_files(r'E:\python\study\python基础')
# print(get_count(r'E:\offcn\授课班级\7.系统班0701系统班\Day14代码\test01-知识回顾.py'))
print(f'代码总行数:{sum(count_list)}行')


