# 推导式模块
# 列表推导式
lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst_new = [i * i for i in lst if i % 2 == 0 if i > 2]


# lst_new=[i*i for i in lst if i%2==0 and i>2]
# print(lst_new)

def square(num):
    return num * num


new_lst = [square(i) for i in lst]
# print(new_lst)
# print(1 and 2 and 4 and 3)
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in lst:
#     for j in i:
#         print(j)

# a={1:1,9:6,7:8}
# key=a.keys()
# # print(key)
# print(sorted(key))
# for i in sorted(key):
#     print(i,end=',')
# a='xydz'
# for i in sorted(a,reverse=True):
#     print(i,end='')
# a='xyzwd'
# print(a[::2])
# for i in range(2,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=' ')
# 3.一球从100米高度自由落下，每次落地后反跳回原高度的一半，再落下，
# 求球在第10次落地时，共经过多少米？第10次反弹多高？

# a=100
# sum=0
# for i in range(1,5):
#     sum+=2*a
#     a=a/2
# print(sum-100)
# print(a)

# a=100
# i=0
# mi=100
# while i<10:
#     mi+=a#落地的时候加上
#     a=a/2
#     if i!=9:
#         mi+=a#最后一次叹气不加
#     i+=1
# print(mi)
# print(a)

# a=[lambda x:1,2,3]
# print(a)

# a=[]
# i=0
# while i<10:
#     a.append(int(input("请输入第%d个数"%(i+1))))
#     i+=1
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# print(max(a))
# print(min(a))
# print(sum(a))
# print(sum(a)/len(a))

def hi(name="yasoob"):
    return "hi " + name


print(hi())