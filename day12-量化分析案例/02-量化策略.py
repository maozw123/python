# # 可以自己import我们平台支持的第三方python模块，比如pandas、numpy等。
# import numpy  as np
# from sklearn.linear_model import LinearRegression
#
#
# # 在这个方法中编写任何的初始化逻辑。context对象将会在你的算法策略的任何方法之间做传递。
# def init(context):
#     # 初始化股票池
#     context.hs300 = index_components("000300.XSHG")
#     # (9,)
#     # (1,9)
#     weight = np.mat(np.array(
#         [0.02953221, -0.04920124, -0.10791485, 0.00801783, -0.03613599, 0.1310877, -0.03030564, 0.40286239,
#          -0.30166898]))
#
#     context.weight = weight.T
#
#     # 选股 的数量
#     context.stock_num = 20
#
#     # 每月进行一次调仓
#     # 设置定时器
#     # 参数1 每月执行的逻辑--函数
#     # 参数2 tradingday 每月执行逻辑的交易日
#     scheduler.run_monthly(MyLinearRegression, tradingday=1)
#
#
# def three_sigma(data):
#     """
#     基于3sigma原则的离群值处理
#     :param data: 需要处理的数据
#     :return: 处理之后的数据
#     """
#     # 上限
#     up = data.mean() + 3 * data.std()
#     # 下限
#     low = data.mean() - 3 * data.std()
#
#     # 超过上限 变为上限，超过下限变为下限
#     data = np.where(data > up, up, data)
#     data = np.where(data < low, low, data)
#
#     return data
#
#
# def stand_sca(data):
#     """
#     标准差标准化
#     :param data:原数据
#     :return: 标准差之后的数据
#     """
#     data = (data - data.mean()) / data.std()
#
#     return data
#
#
# def deal_data(data):
#     """
#     因子数据处理
#     """
#     # （1）缺失值处理
#     # 直接删除--dropna
#     data.dropna(how="any", axis=0, inplace=True)
#
#     market_cap = data.loc[:, "market_cap"]
#     for column in data.columns:
#         # （2）离群值处理
#         data.loc[:, column] = three_sigma(data.loc[:, column])
#         # （3）标准化处理
#         data.loc[:, column] = stand_sca(data.loc[:, column])
#         if column == "market_cap":
#             continue
#         # （4）市值因子--中性化处理 # market_cap---市值因子
#         # 以市值因子为特征值，其他因子为目标值建立线性关系
#         x = market_cap.values.reshape((-1, 1))
#         y = data.loc[:, column].values
#         # 实例化算法对象
#         lr = LinearRegression()
#         # 构建模型
#         lr.fit(x, y)  # 特征值必须是二维数据，目标值必须是一维的
#         # 进行预测--预测值----受市值影响部分
#         y_predict = lr.predict(x)
#
#         # 不受市值影响的部分  =  其他因子的值 - 受市值影响的部分
#         data.loc[:, column] = data.loc[:, column] - y_predict
#
#     return data
#
#
# def tiaocang(context):
#     """
#     调整仓位
#     """
#     # 获取所有的仓位中的股票
#     for tmp in context.portfolio.positions.keys():
#         # 遍历仓位，如果股票不在stock_list就卖出
#         if tmp not in context.stock_list:
#             order_target_percent(tmp, 0)
#     # 买入
#     for tmp in context.stock_list:
#         order_target_percent(tmp, 1 / len(context.stock_list))
#
#
# def MyLinearRegression(context, bar_dict):  # context此时必须传递
#     """
#     每月执行的逻辑函数
#     """
#     # 1、获取因子数据
#     q = query(
#         fundamentals.eod_derivative_indicator.pe_ratio, fundamentals.eod_derivative_indicator.pb_ratio,
#         fundamentals.eod_derivative_indicator.market_cap, fundamentals.financial_indicator.ev,
#         fundamentals.financial_indicator.return_on_asset_net_profit,
#         fundamentals.financial_indicator.du_return_on_equity, fundamentals.financial_indicator.earnings_per_share,
#         fundamentals.income_statement.revenue, fundamentals.income_statement.total_expense
#     ).filter(
#         fundamentals.stockcode.in_(context.hs300)
#     )
#
#     fund = get_fundamentals(q)
#
#     context.factor = fund.T
#
#     # print(context.factor)
#
#     # 2、因子数据处理
#     context.factor = deal_data(context.factor)
#
#     print("因子处理之后的结果：\n", context.factor)
#
#     # 3、因子 * 权重  + B = 预测收益
#     # (300,9) * (9,1)  = [300,1]
#     context.factor.loc[:, "factor_return"] = np.dot(context.factor, context.weight)
#
#     # 4、将数据以 收益进行降序排序---预测的收益较好的20支股票
#     context.stock_list = context.factor.sort_values(by="factor_return", ascending=False).head(context.stock_num).index
#
#     # 5、调仓
#     tiaocang(context)
#
#
# # before_trading此函数会在每天策略交易开始前被调用，当天只会被调用一次
# def before_trading(context):
#     pass
#
# 
# # 你选择的证券的数据更新将会触发此段逻辑，例如日或分钟历史数据切片或者是实时数据切片更新
# def handle_bar(context, bar_dict):
#     pass
#
#
# # after_trading函数会在每天交易结束后被调用，当天只会被调用一次
# def after_trading(context):
#     pass
