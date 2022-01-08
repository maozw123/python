'''
0.掌握所有的课堂案例
基础练习题
在自定义模块中封装如下功能：并完成验证
1.封装自定义函数，功能类似lower(src)
2.封装自定义函数，功能类似upper(src)
3.封装函数，功能类似find(src,sub)
4.封装函数，功能类似rfind(src,sub)
5.封装函数，功能类似isdigit(src)
6.封装函数，功能类似partition(src,sub)
能力提升
7.封装函数，功能类似startswith(src,sub)判断字符串src是否以字符串sub的内容开头
8.封装函数，功能类似endswith(src,sub)判断字符串src是否以字符串sub的内容结尾

综合业务能力：
9.完善双色球的后续功能
'''


# 1.封装自定义函数，功能类似lower(src)
def lower1(str1):
    str2 = ''
    for ch in str1:
        if 'A' <= ch <= 'Z':
            ch = chr(ord(ch) + 32)
            str2 = str2 + ch
        else:
            str2 = str2 + ch
    return str2
# print(lower1("asAWQq"))
# 2.封装自定义函数，功能类似upper(src)
def upper1(str1):
    str2 = ''
    for ch in str1:
        if 'a' <= ch <= 'z':
            ch = chr(ord(ch) - 32)
            str2 = str2 + ch
        else:
            str2 = str2 + ch
    return str2
# print(upper1('ARFqwD'))
# 3.封装函数，功能类似find(src,sub)
def find1(src, sub):
    for i in range(len(src)):
        # str1 = src[i:i + len(sub)]
        if src[i:i+len(sub)] == sub:
            return i
    else:
        return -1
# print(find1('QWEDESAxc','ES'))
# 4.封装函数，功能类似rfind(src,sub)
def rfind1(src, sub):
    for i in range(-1,-(len(src)+1),-1):
        if src[i:i-len(sub):-1] == sub[::-1]:
            return i+len(src)-1
    else:
        return -1
# print(rfind1('dadwawddddsfffffff','ds'))
# print(rfind1('QSdezxzxze','zx'))
def rfind2(src,sub):
    for i in range(len(src)-1,-1,-1):
        if src[i:i-len(sub):-1]==sub[::-1]:
            return i-len(sub)+1
    else:
        return -1
# print(rfind2('dadwawddddsfffffff','ds'))
# print(rfind2('QSdezxzxze','zx'))
# 5.封装函数，功能类似isdigit(src)
def isdigit1(src):
    for i in src:
        if i > '9' or i < '0':
            return False
    else:
        return True
# def isdigit1(src):
#     for i in src:
#         if '0'<=i<='9':
#             continue
#         else:
#             return False
#     else:
#         return True
print(isdigit1('123'))
# print(isdigit1('wqd2W'))
# 6.封装函数，功能类似partition(src,sub)
def partition1(src, sub):
    list1 = []
    for i in range(len(src)):
        if src[i] == sub:
            list1.append(src[0:i])
            list1.append(src[i])
            list1.append(src[i + 1:len(src)])
            tuple1 = tuple(list1)
            break
    else:
        list1.append(src)
        list1.append('')
        list1.append('')
        tuple1 = tuple(list1)
    return tuple1
def partition2(src, sub):
    for i in range(len(src)):
        str1 = src[i:i + len(sub)]
        # print(str1)
        if str1 == sub:
            return (src[:i], sub, src[i + len(sub):])
    return (src, '', '')
# print(partition1('sdcza','c'))
# print(partition1('sdza','c'))
# print(partition2('afdgav','dg'))
# print(partition2('afdgav','dn'))
# 7.封装函数，功能类似startswith(src,sub)判断字符串src是否以字符串sub的内容开头
def starts_with1(src, sub):
    return src[:len(sub)] == sub
# print(starts_with1('ahiygtg','ah'))
# 8.封装函数，功能类似endswith(src,sub)判断字符串src是否以字符串sub的内容结尾
def endswith1(src, sub):
    return src[-len(sub):] == sub
# print(endswith1('agfdtrht', 'rht'))
# print(endswith1('agfdtrht', 'rh'))
