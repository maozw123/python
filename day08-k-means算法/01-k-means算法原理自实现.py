import pandas as pd
import numpy as np
import matplotlib.pyplot   as plt
from sklearn.cluster import KMeans # 导入k-means


def build_data():
    """
    构建数据
    :return:data
    """
    # (1)加载数据
    data = pd.read_table("./test.txt", sep="\t")
    # print("data:\n", data)
    # print("data的数据类型\n", data.dtypes)
    # (2)转化为矩阵
    data = np.mat(data.values)

    print("data:\n",data)
    print('*'*30)
    return data


def center_init(data, k):
    """
    初始化聚类中心
    :param data: 数据
    :param k: 聚类的类别数量
    :return: center
    """
    # 获取数据的行数
    index_num = data.shape[0]
    # 获取数据的列数
    columns_num = data.shape[1]
    # for i in range(k):
    #     # 随机选择一行所有的数据作为一个中心
    #     # [low,high)
    #     r = np.random.randint(low=0, high=index_num, dtype=np.int32)
    #     print("r:\n",r)
    # 先初始化一个全为0 的聚类中心
    center = np.zeros(shape=(k, columns_num))
    # 设计列表来退出循环
    r_list = []
    # 设计一个计数器来 给聚类中心赋值
    i = 0
    while True:
        #   # 随机选择一行所有的数据作为一个中心
        #   # [low,high)
        r = np.random.randint(low=0, high=index_num, dtype=np.int32)
        if r not in r_list:
            # print("初始化为聚类中心")
            # 给聚类中心进行赋值
            center[i, :] = data[r, :]
            r_list.append(r)
            i += 1
        else:
            continue
        # 如果 随机选择了4个不同的r,那就退出循环
        if len(r_list) == k:
            break

    return center


def distance(v1, v2):
    """
    计算距离
    :param v1:点1
    :param v2: 点2
    :return: 距离dist
    """
    # 法1
    # v1 是矩阵 将矩阵转化数组，再进行降为1维
    # v1 = v1.A[0]
    # print(v1)
    # sum_ = 0
    # for i in range(v1.shape[0]):
    #     sum_ += (v1[i] - v2[i]) ** 2
    # dist = np.sqrt(sum_)
    # print(dist)
    # 法2
    dist = np.sqrt(np.sum(np.power((v1 - v2), 2)))
    return dist


def k_means_owns(data, k):
    """
    自实现k-means
    :param data: 需要的聚类的样本
    :param k: 聚类的类别数目
    :return: None
    """

    # 获取数据的行数
    index_num = data.shape[0]

    # 创建一个new_data 来保存每一个样本的最短距离与属于哪一个聚类中心的簇
    new_data = np.zeros(shape=(index_num, 2))

    # （1）初始化聚类中心--随机在所有样本选择4行样本作为聚类中心
    center = center_init(data, k)
    print("center:\n", center)
    flag = True
    while flag:
        flag = False
        # (2) 计算每一个样本与每一个聚类中心的距离
        for i in range(index_num):
            min_dist = 10000000000000
            min_index = -1
            for j in range(k):
                # 计算距离
                dist = distance(data[i, :], center[j, :])
                print("dist:\n", dist)
                if dist < min_dist:
                    min_dist = dist
                    min_index = j
            if new_data[i, 0] != min_index:
                flag = True
                new_data[i, :] = min_index, min_dist

        if flag:
            # 求取各个簇的中心
            for p in range(k):
                # p   --->0 1 2 3
                p_cluster = data[new_data[:, 0] == p, :]
                # print("第%d簇的样本：" % p)
                # print(p_cluster)
                # 计算新的聚类中心
                center[p, :] = p_cluster[:, 0].mean(), p_cluster[:, 1].mean()

    return new_data, center


def show_res_owns(data, new_data, center):
    """
    结果展示
    :param data: 原数据
    :param new_data: 记录属于哪一类别的数据
    :param center: 聚类中心
    :return: None
    """
    # 1、创建画布
    plt.figure()
    # 2、绘图
    color_list = ["r", "g", "pink", "y"]
    # 散点图
    for i in range(data.shape[0]):
        plt.scatter(data[i, 0], data[i, 1], c=color_list[int(new_data[i, 0])])

    # 绘制标注
    plt.plot(center[:, 0], center[:, 1], "bx", markersize=12)
    # 3、展示
    plt.show()


def show_res(data, y_predict, center):
    """
    结果展示
    :param data: 原数据
    :param y_predict: 预测类别
    :param center: 聚类中心
    :return: None
    """
    # 1、创建画布
    plt.figure()
    # 2、绘图
    color_list = ["r", "g", "pink", "y"]
    # 散点图
    for i in range(data.shape[0]):
        plt.scatter(data[i, 0], data[i, 1], c=color_list[y_predict[i]])

    # 绘制标注
    plt.plot(center[:, 0], center[:, 1], "bx", markersize=12)
    # 3、展示
    plt.show()



def main():
    """
    主函数
    :return: None
    """
    # 1、构建数据
    data = build_data()
    print("data:\n", data)

    # 2、自实现k-means
    # （1）确定聚类的类别数目
    k = 4
    # new_data, center = k_means_owns(data, k)
    #
    # print("new_data:\n", new_data)
    # print("最终的聚类中心：\n", center)

    # 3、结果展示
    # show_res_owns(data, new_data, center)


    # 使用sklearn中的kmeans来实现聚类
    # 1、创建算法实例
    km = KMeans(n_clusters=k)
    # 2、训练数据
    km.fit(data)
    # 3、进行预测
    y_predict = km.predict(data)
    # 获取聚类中心
    center = km.cluster_centers_

    print("预测值：\n",y_predict)
    print("center:\n",center)

    # 进行结果展示
    show_res(data,y_predict,center)


if __name__ == '__main__':
    main()
