import numpy as np

arr1=np.arange(1,17,1).reshape((4,4))
# print(arr1)
# np.save('arr1',arr1)
# print('文件保存成功')
# set=np.load('./arr1.npy')
# print(set)

arr2=np.arange(1,10).reshape(9)
# print(arr2)
# np.savez('./arr2',arr1,arr2)
# np.savez('./arr2',arr1=arr1,arr2=arr2)
# print('保存成功')

# set=np.load('./arr2.npz')
# print(set)
# #
# for i in set:
#     print(i)
# # print(set['arr_0'])
# # print(set['arr_1'])
# print(set['arr1'])
# print(set['arr2'])


# np.savetxt('arr.txt',arr1)
np.savetxt('arr.txt',arr1,fmt='%d',delimiter=',')
print('保存完毕')