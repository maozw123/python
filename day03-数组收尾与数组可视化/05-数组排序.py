import numpy as np

# 创建数组
# arr = np.array([[4, 1, 9], [7, 6, 5]])
# print("arr:\n", arr)
#
# # 进行排序
# # 在列的方向上进行排序
# # arr.sort(axis=-1)
# arr.sort(axis=0)
#
# print("排序之后的结果：\n", arr)

# 间接排序
# arr = np.array([5, 4, 6, 7, 1])
# print("arr:\n",arr)
#
# # 升序排序之后元素原来所处的下标
# res = arr.argsort()
#
# print("res:\n",res)

# arr = np.array([[3, 9, 1], [0, 8, 5]])
# print("arr:\n", arr)
#
# # 按照列的方向排序
# # res = arr.argsort(axis=-1)
# res = arr.argsort(axis=0)
#
# print("res:\n", res)

# lexsort()
a = np.array([3, 2, 6, 4, 5])
b = np.array([50, 30, 40, 20, 10, ])
c = np.array([400, 300, 600, 100, 200])
#
# # 参数 keys  传需要排序的数组的列表，返回值：最后一个数组元素排序之后原来所处的下标
# res = np.lexsort([a, b, c])
#
# print("res:\n", res)
#
# res_a = [a[i] for i in res]
# res_b = [b[i] for i in res]
# res_c = [c[i] for i in res]
#
# print("a 按照c 的规则排序之后的结果：\n",res_a)
# print("b 按照c 的规则排序之后的结果：\n",res_b)
# print("c 按照c 的规则排序之后的结果：\n",res_c)

# 按照c的规则给ab 排序
# res = c.argsort()
# print("res:\n",res)
# res_a = [a[i] for i in res]
# res_b = [b[i] for i in res]
# res_c = [c[i] for i in res]
#
# print("a 按照c 的规则排序之后的结果：\n",res_a)
# print("b 按照c 的规则排序之后的结果：\n",res_b)
# print("c 按照c 的规则排序之后的结果：\n",res_c)