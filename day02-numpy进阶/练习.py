import numpy as np

# arr=np.array([1,2,3,4])
# arr=np.arange(9,3,-1)
# arr=np.arange(6)
# arr=np.arange(0,5,1)
# arr=np.linspace(1,4,5,endpoint=True)
# arr=np.linspace(1,4,5,endpoint=False)

# arr=np.logspace(0,3,3,endpoint=False,base=10)

# arr=np.zeros(shape=(4,5))
# arr=np.zeros(shape=[4,5])
# arr=np.diag([1,2,3,4])
# arr=np.diag([1,2,3,4],k=0)
# arr=np.diag([1,2,3,4],k=6)
# print(arr)
# print('arr的类型:\n',type(arr))
# print("arr的维度ndim：",arr.ndim)
# print("arr的形状shape：",arr.shape)

# arr=np.diag([[1,2,3],[4,5,6]],k=1)
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
# arr=np.random.random(size=10)
# arr=np.random.random(size=(2,3))
# print("arr:\n",arr)
# print("arr的类型：\n",type(arr))
# print("arr的维度ndim：",arr.ndim)
# print("arr的形状shape：",arr.shape)

# arr=np.random.rand(10)
# arr=np.random.rand((2,3))错误的  不能传元祖
# arr=np.random.rand(2,3)
# print("arr:\n",arr)
# print("arr的类型：\n",type(arr))
# print("arr的维度ndim：",arr.ndim)
# print("arr的形状shape：",arr.shape)

# arr = np.random.randint(low=1,high=5,size=10)
# arr = np.random.randint(low=1,high=5,size=(2,3))
# print("arr:\n", arr)
# print("arr 的类型：\n", type(arr))
# print("arr的维度：", arr.ndim)
# print("arr的形状：", arr.shape)

# arr = np.random.uniform(size=10)
arr = np.random.uniform(size=(2,3))
# arr = np.random.uniform(low=2,high=3,size=(2,3))
print("arr:\n", arr)
print("arr 的类型：\n", type(arr))
print("arr的维度：", arr.ndim)
print("arr的形状：", arr.shape)
