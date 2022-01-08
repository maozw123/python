'''
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
'''
# sum = 0
# for bw in range(1, 5):
#     for sw in range(1, 5):
#         for gw in range(1, 5):
#
#             if bw != sw and bw != gw and sw != gw:
#                 print(bw * 100 + sw * 10 + gw)
#                 sum += 1
# print(sum)


for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+'*'+str(i)+'='+str(i*j),end='\t')
    print(end='\n')


for a in range(1,10):
    for b in range(1,a+1):
        result=a*b
        if b<a:
            print(b,'*',a,'=',result,' ',end='')
        else:
            print(b,'*',a,'=',result,' ')