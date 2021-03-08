# 1、加载数据---特征值与目标值
# 2、随机初始化权重与偏置---变量op
# 3、预测--->矩阵相乘
# 4、预测值与真实值 ---损失--均方误差损失
# 5、构建优化算法进行优化损失---设置学习率
# 6、不断优化op
import tensorflow as tf


class MyLinearRegression(object):
    def __init__(self):
        self.learning_rate = 0.1
        # self.learning_rate = 0.01
        # self.learning_rate = 0.00000000001 # 学习率不能过小,会造成梯度消失
        # self.learning_rate = 100  # 学习率过大会造成梯度爆炸

    def build_data(self):
        """
        构建特征与目标值
        :return: x,y
        """
        # 给构建数据 套个命名空间
        with tf.variable_scope("build_data"):
            # 随机初始化特征值[100,1]
            x = tf.random_normal(
                shape=[100, 1],
                mean=0.0,
                stddev=1.0,
                name="x"
            )

            # x [100,1]  * w  + b =  y[100,1]
            # w [1,1]
            # b []
            # 矩阵与 数的相加----与矩阵的每一个元素相加
            y = tf.matmul(x, [[0.7]]) + 0.8

        return x, y

    def get_weight(self, shape):
        """
        生成权重--变量op
        :param shape:生成权重的形状
        :return: weight
        """
        with tf.variable_scope("get_weight"):
            weight = tf.Variable(
                initial_value=tf.random_normal(
                    shape=shape,
                    mean=0.0,
                    stddev=1.0
                ),
                name="w"
            )
        return weight

    def get_bias(self, shape):
        """
        生成偏置--变量op
        :param shape:生成偏置的形状
        :return: bias
        """
        with tf.variable_scope("get_bias"):
            bias = tf.Variable(
                initial_value=tf.random_normal(
                    shape=shape,
                    mean=0.0,
                    stddev=1.0
                ),
                name="b"
            )
        return bias

    def linear_model(self, x):
        """
        构建线性关系
        :param x: 特征值
        :return: 预测值
        """
        with tf.variable_scope("linear_model"):
            # x [100,1] * w[1,1] + b[]  =  y_predict[100,1]
            # w [1,1]
            # y[100,1]
            # b []
            # （1）初始化权重
            self.weight = self.get_weight(shape=[1, 1])
            # （2）初始化偏置
            self.bias = self.get_bias(shape=[])
            # （3）求取预测值
            y_predict = tf.matmul(x, self.weight) + self.bias

        return y_predict

    def losses(self, y_true, y_predict):
        """
        计算均方误差损失
        :param y_true: 真实值[100,1]
        :param y_predict: 预测值[100,1]
        :return: 均方误差损失
        """
        with tf.variable_scope("losses"):
            loss = tf.reduce_mean(tf.square(y_true - y_predict))
        return loss

    def sgd(self, loss):
        """
        使用sgd进行优化损失
        :param loss: 均方误差损失
        :return: 优化op
        """
        with tf.variable_scope("sgd"):
            # GradientDescentOptimizer sgd随机梯度下降优化算法
            # 返回sgd算法对象
            sgd = tf.train.GradientDescentOptimizer(learning_rate=self.learning_rate)
            # 优化均方误差损失-- 损失减小的方向
            train_op = sgd.minimize(loss)

        return train_op

    def train(self):
        """
        进行训练
        :return:None
        """
        with tf.variable_scope("train"):
            # 1、加载数据
            x, y = self.build_data()

            # 2、构建线性模型
            y_predict = self.linear_model(x)

            # 3、计算均方误差损失
            loss = self.losses(y, y_predict)

            # 4、指定sgd优化算法来优化loss
            train_op = self.sgd(loss)

            # 开启会话--执行run--train_op
            with tf.Session() as ss:
                # 显式的初始化w,b
                ss.run(tf.global_variables_initializer())

                # 序列化events
                tf.summary.FileWriter("./tmp/",graph=ss.graph)

                # 不断的run --train_op--循环
                for i in range(500):
                    ss.run(train_op)

                    print("第%d次的损失为%f,权重为%f,偏置为%f" % (
                        i + 1,
                        loss.eval(),
                        self.weight.eval(),
                        self.bias.eval()
                    ))


# 1、实例化对象
lr = MyLinearRegression()
# 2、调用方法
lr.train()
