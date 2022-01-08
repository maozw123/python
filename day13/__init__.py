import os
def count_file_hang(dirpath):
    count=0
    for i in os.listdir(dirpath):
        path=dirpath+'\\'+i
        if os.path.isfile(path) and path.endswith('.py'):
            f1 = open(path, 'r', encoding='utf-8')
            f1.readline()
            count+=1
            f1.close()
            print(count)
        elif os.path.isdir(path):
            count_file_hang(path)