import numpy as np

# arr=np.array([1,2,3,4])
# print("arr:\n",arr)
# print("arr的类型：\n",type(arr))
#
# arr=np.arange(0,5,1)
# print("arr:\n",arr)
# print("arr的类型：\n",type(arr))

# 生成一个等差数组
# 参数一  开始位置
# 参数二  结束位置
# 参数三 ---生成数组的元素个数
# endpoint=Ture --包含结束位置  默认不写为Ture
# endpoint=False --不包含结束位置
# arr=np.linspace(0,5,6)
# print("arr:\n",arr)
# print("arr的类型：\n",type(arr))

# 生成一个等比数组
# 参数一  开始位置
# 参数二  结束位置
# 参数三 ---生成数组的元素的个数
# endpoint=Ture --包含结束位置
# endpoint=False --不包含结束位置
# base=10.0
# arr=np.logspace(0,2,3)
# arr=np.logspace(0,2,3,base=2)
# print("arr:\n",arr)
# print("arr的类型：\n",type(arr))

# 使用zeros  ones  diag  eye 来创建数组
# 创建一个元素全部为0的数组，参数为数组的形状
# arr=np.zeros(shape=(2,3))
# # arr=np.zeros(shape=[2,3])#形状传递一个列表也是可以的
# print("arr:\n",arr)
# print("arr的类型：\n",type(arr))
# print("arr的维度ndim：",arr.ndim)
# print("arr的形状shape：",arr.shape)


# 创建一个元素全部为1的数组，参数为数组的形状
# arr=np.ones(shape=(2,3))
#
# print("arr:\n",arr)
# print("arr的类型：\n",type(arr))
# print("arr的维度ndim：",arr.ndim)
# print("arr的形状shape：",arr.shape)

# 创建一个类似对角矩阵的数组
# arr=np.diag([1,2,3,4])
# 如果k>0，给定的值在正对角线的位置进行向上偏移k的单位
# 如果k<0，给定的值在正对角线的位置进行向下偏移k的单位
# arr=np.diag([1,2,3,4],k=1)
# print("arr:\n",arr)
# print("arr的类型：\n",type(arr))
# print("arr的维度ndim：",arr.ndim)
# print("arr的形状shape：",arr.shape)


# arr=np.diag([[1,2],[3,4]],k=0)
# print("arr:\n",arr)
# print("arr的类型：\n",type(arr))
# print("arr的维度ndim：",arr.ndim)
# print("arr的形状shape：",arr.shape)


# 生成一个类似单位矩阵的数组
# N  行数
# M   列数  可以省略
# k参考diag的k
# arr=np.eye(N=2,M=2,k=0)
# arr=np.eye(N=2,M=2,k=1)
# arr=np.eye(N=3,k=0)
# print("arr:\n",arr)
# print("arr的类型：\n",type(arr))
# print("arr的维度ndim：",arr.ndim)
# print("arr的形状shape：",arr.shape)


# 创建随机数组
# 生成[0,1)的随机数
# size  可以是生成数组的元素个数
# 也可以是数组的形状
# arr=np.random.random(size=10)
# arr=np.random.random(size=(2,3))
# print("arr:\n",arr)
# print("arr的类型：\n",type(arr))
# print("arr的维度ndim：",arr.ndim)
# print("arr的形状shape：",arr.shape)


# 生成服从均匀分布的随机数[0,1)
# arr=np.random.rand(10)
# # arr=np.random.rand((2,3))错误的  不能传元祖
# arr=np.random.rand(2,3)
# print("arr:\n",arr)
# print("arr的类型：\n",type(arr))
# print("arr的维度ndim：",arr.ndim)
# print("arr的形状shape：",arr.shape)


# 生成一个符合正态分布的数组
# 正态分布
# u ---数学期望---即均值 ----反映到图像上，就是数据的对称位置
# a --- 标准差，反映的数据的离散程度
# a 越大，说明数据越离散，反映到图像上就是图像越平滑
# a 越小，说明数据越聚集，反映到图像上就是图像越陡峭
# 如果均值u = 0.0  标准差a = 1.0，那么此时为标准正态分布
# 正态分布---由大量数据产生的结论，可以应用于少量数据，但是应用的少量数据----->推测不出正态分布
# 生成一个符合标准正态分布的数组
# 参数  可以传生成数组的元素个数，也可以传生成数组的行列数，但是不能传形状
# arr = np.random.randn(10)
# arr = np.random.randn(2,3)
# # arr = np.random.randn((2,3)) # 错误的
# print("arr:\n", arr)
# print("arr 的类型：\n", type(arr))
# print("arr的维度：", arr.ndim)
# print("arr的形状：", arr.shape)


# 创建一个某个区间内，随机整数
# 生成[low,high) 内的指定size 的随机整数数组
# 参数size  可以是生成数组的元素个数，也可以是生成数组的形状
# arr = np.random.randint(low=1,high=5,size=10)
# arr = np.random.randint(low=1,high=5,size=(2,3))
# print("arr:\n", arr)
# print("arr 的类型：\n", type(arr))
# print("arr的维度：", arr.ndim)
# print("arr的形状：", arr.shape)

# 创建一个某个区域内的随机小数数组
# 默认生成[0,1)范围内的随机小数数组，
# 参数size 可以是生成数组的元素个数，也可以是生成数组的形状
# 可以修改low  high 生成小数的范围
# arr = np.random.uniform(size=10)
# arr = np.random.uniform(size=(2,3))
# arr = np.random.uniform(low=2,high=3,size=(2,3))
# print("arr:\n", arr)
# print("arr 的类型：\n", type(arr))
# print("arr的维度：", arr.ndim)
# print("arr的形状：", arr.shape)
