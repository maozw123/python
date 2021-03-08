import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler  # 标准化
from sklearn.model_selection import train_test_split  # 数据集拆分
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score

# 加载数据
data = pd.read_csv("./breast-cancer-wisconsin.data", header=None)
# print("data:\n", data)
# 指定其列索引名称
columns = [
    "Sample code number",
    "Clump Thickness",
    "Uniformity of Cell Size",
    "Uniformity of Cell Shape",
    "Marginal Adhesion",
    "Single Epithelial Cell Size",
    "Bare Nuclei",
    "Bland Chromatin",
    "Normal Nucleoli",
    "Mitoses",
    "Class"
]
# 设置列索引
data.columns = columns
# print("data:\n", data)

# 1、筛选出特征与目标值，将不重要、无关的特征干掉
# 将id_编码 给删除
data = data.iloc[:, 1:]
print("数据集：\n", data)

# 2、检测缺失值，并处理缺失值
# res_null = pd.isnull(data).sum()
# print("检测缺失值的结果：\n", res_null)

# 3、先将"?"替换成np.nan类型
data.replace("?", np.nan, inplace=True)

# 4、检测
res_null = pd.isnull(data).sum()
print("检测缺失值的结果：\n", res_null)

# 5、处理缺失值
# 删除法
# 填充法
# 插值法
# 删除法
data.dropna(how="any", axis=0, inplace=True)
print("删除缺失值之后的结果为：\n", data.shape)

# 数据集拆分---
train_x, test_x, train_y, test_y = train_test_split(data.iloc[:, :9].values, data.iloc[:, 9].values, test_size=0.3,
                                                    random_state=1)

# 6、标准化处理数据
# 标准差标准化
# （1）实例化对象
stand = StandardScaler()
# (2)计算指标并进行数据转化---只需要标准化特征值
train_x = stand.fit_transform(train_x)
test_x = stand.fit_transform(test_x)

# 7、构建逻辑回归模型进行癌症预测
# (1）构建算法实例
lr = LogisticRegression()
# (2)训练数据
lr.fit(train_x, train_y)
# (3)预测
y_predict = lr.predict(test_x)

# 获取准确率
score = lr.score(test_x, test_y)  # 准确率为96.1% # 3.9%错误率

# 获取权重与偏置
weight = lr.coef_
bias = lr.intercept_

print("预测值：\n", y_predict)
print("准确率：\n", score)
print("权重：\n", weight)
print("偏置：\n", bias)
print("*" * 100)

# 癌症患者---去体检---检测为健康---造成结果：错过最佳治疗时间，人命关天。---不能接受的
# 健康的人--体检 ---检测为癌症 ----造成后果：复检。

# 在 二分类情况下，两种结果的重要性程度不一样的情况下，准确率将不再是唯一的评判标准
# 召回率 --对于分类的评估
# 召回率= 预测为正例/真实类别为正例 # 越高越好--查的全
res_report = classification_report(y_true=test_y, y_pred=y_predict, labels=[2, 4], target_names=["良性", "恶性"])
print("res_report:\n", res_report)

# 模型还不错 召回率为0.96  准确率为0.96
# 比如说：样本数据100个样本，1个正常，99个癌症患者-----正例为正常的
# 预测 100个全部为癌症患者 ----准确率99%
# 召回率：0/1 = 0 召回率为0
# 此时以癌症患者为正例：准确率为99% 召回率为 99/99 = 1
# 应用的时候---全部预测为癌症患者

# 样本不均衡情况下，召回率、准确率 又不能完全去衡量 结果
# AUC指标--只用在 样本不均衡的情况
# ROC曲线
# 在不同阈值的情况下，TPR(召回率) 与FPR 描绘出的曲线就是ROC曲线
# AUC ---ROC曲线与TPR与FPR 右下部分组成面积
# 对于好的模型---AUC指标>0.5
# AUC为 1 ，那么预测完全准确，那么这个模型叫最优模型（理想状态下）
# AUC最坏的情况下，AUC=0.5
# AUC --->(0.5,1)
# 意义：随机取一个正样本，预测为正例样本的概率 > 反例样本的概率
# 随机选一个反例样本，预测为正例的概率 < 阈值
# y_true  传真实类别，正例为1 反例为0
# y_score  --预测值
# 可以使用三目表达式
# 参数1  条件
# 参数2  条件成立执行它
# 参数3  条件为假执行它
# test_y = np.where(test_y > 3, 1, 0)
# print("test_y:\n", test_y)
# res_score = roc_auc_score(y_true=test_y, y_score=y_predict)
# print("AUC指标：\n", res_score)  # 0.95

# 假设已经发现样本不均衡----将样本变为均衡的
