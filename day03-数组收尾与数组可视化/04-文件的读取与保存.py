import numpy as  np


# 二进制文件 ----机器能够识别的文件
# 创建一个数组
# arr = np.arange(16).reshape((4,4))

# 保存单个数组到二进制文件中
# 参数1  文件路径+ 名称，这个名称的后缀名可以省略，默认保存的是以.npy为结尾的文件
# 参数2  需要保存的数组
# np.save("./arr",arr)
# print("单个数组保存完毕")

# 加载.npy文件
# 参数 文件路径+ 名称 ，必须是完整名称
# res = np.load("./arr.npy")
# print(res)

# 多个数组的数组的保存
# arr1 = np.arange(9)
# arr2 = np.arange(16).reshape((4, 4))
#
# print("arr1:\n", arr1)
# print("arr2:\n", arr2)

# 将不同的数组进行保存
# 参数1  文件路径+ 名称，此时也可以省略后缀名，默认保存成以.npz为结尾的文件
# np.savez("./arr", arr1, arr2)
# print("多个数组保存完毕")



# 加载.npz文件
# res = np.load("./arr.npz")
# print(res)  # 返回一个对象，对象内部是以键值对的形式存储
# for tmp in  res :
#     print(tmp)
# print(res["arr_0"])
# print(res["arr_1"])


# 如果需要保存的数组数量过多，读取出来无法区分，可以在保存的时候，指定其key值的形式来保存
# np.savez("./arr", arr1=arr1, arr2=arr2, x=arr1, y=arr2)
# print("保存完毕")

# 加载.npz文件
# res = np.load("./arr.npz")
# print(res)

# 遍历对象来获取保存时 的key
# for  tmp in  res :
#     print(tmp)
# print(res["arr1"])
# print(res["arr2"])
# print(res["x"])
# print(res["y"])



# 文本文件 ---人能看懂的有序的以文本形式存储的文件
# 创建一个数组
# arr = np.arange(16).reshape((4,4))

# 以文本形式保存数组
# 参数1  文件路径+ 名称 后缀不能省略
# 参数2  需要保存的数组
# fmt   保存的格式
# delimiter  保存的分隔符
# np.savetxt("arr.txt",arr,fmt="%d",delimiter=",")
# print("保存完毕")


# 加载文本类型的数据
# 保存的时候 以什么分割，读取的时候必须设置分隔符delimiter
# loadtxt 不能读取含有缺失值的数组
# res = np.loadtxt("./arr.txt",delimiter=",",dtype=np.int32)
# print(res)


# 推荐使用
# 能够读取含有缺失值的数组，会给缺失的位置填值，默认会给一个跟你自身数组可以去区分的值
# 可以自己去filling_values 来指定缺失值的替代值
# res = np.genfromtxt("./arr.txt",delimiter=",",dtype=np.int32,filling_values=-100)
# res = np.genfromtxt("./arr.txt",delimiter=",",dtype=np.int32,filling_values="a") #替代值与数组读出来的值类型不匹配
# print(res)
