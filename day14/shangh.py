'''
left=13446000,right=13448000
top=3706000
buttom=367000

'''
left = 13446000
right = 13448000
top = 3706000
buttom = 367000
list1 = []
list2 = []
for i in range(1, 21):
    list1.append(i)
# print(list1)

for a in range(1, 31):
    list2.append(a)
# print(list1)
# print(list2)

# for i in range(1, 4):
#     for a in range(1, 19):
#         str1 = 'id=' + str(a + 18 * (i - 1)) + ',' + 'left=' + str(left + (i - 1) * 2000) + ',' + 'right=' + str(
#             left + (i) * 2000) + ',' + 'top=' + str(top - (a - 1) * 2000) + ',' + 'buttom=' + str(top - (a) * 2000)
#         # print('id='+str(a+18*(i-1)),'left='+str(left+(i-1)*2000),'right='+str(left+(i)*2000),'top='+str(top-(a-1)*2000),'buttom='+str(top-(a)*2000))
#         print((str(str1)))

# with open('shanghai.txt', 'a', encoding='utf-8') as f:
#     for i in range(1, 4):
#         for a in range(1, 19):
#             str1 = 'id=' + str(a + 18 * (i - 1)) + ',' + 'left=' + str(left + (i - 1) * 2000) + ',' + 'right=' + str(
#                 left + (i) * 2000) + ',' + 'top=' + str(top - (a - 1) * 2000) + ',' + 'buttom=' + str(top - (a) * 2000)
#             # print('id='+str(a+18*(i-1)),'left='+str(left+(i-1)*2000),'right='+str(left+(i)*2000),'top='+str(top-(a-1)*2000),'buttom='+str(top-(a)*2000))
#             print((str(str1)))
#             f.write(str1+'\n')
# def Merge(dict1, dict2):
#     return(dict1.update(dict2))

dict1 = {'type': 'Fshdfjgsdh', 'features': []}
list3 = []
for i in range(1, 4):

    for a in range(1, 19):
        dict2 = {'qeqe': 'kkkk',
                  'properties': {'id': a + 18 * (i - 1), 'left': left + (i - 1) * 2000, 'right': left + (i) * 2000,
                                 'top': top - (a - 1) * 2000, 'bottom': top - (a) * 2000}, 'geo': {'type': 'sfgs',
                                                                                                   'coordi': [[[
                                                                                                                   a + 18 * (
                                                                                                                               i - 1),
                                                                                                                   top - (
                                                                                                                       a) * 2000],
                                                                                                               [1, 1],
                                                                                                               [1, 1],
                                                                                                               [1, 1],
                                                                                                               [1,
                                                                                                                1]]]}}
        # print(str(dict2))
        list3.append(dict2)
print(list3)
dict1['features']=list3
print(dict1)

with open('shanghai.txt', 'a', encoding='utf-8') as f:
    f.write(str(dict1))