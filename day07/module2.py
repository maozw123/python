"""
封装：
求矩形的周长，矩形的面积
求圆的周长，求圆的面积
"""
__all__ = ['PI']
PI = 3.14
# 求矩形的周长函数
def func1(length,width):
    return (length + width) * 2

# 求矩形的面积函数
def func2(length,width):
    return length * width

# 求圆的周长
def func3(r):
    return  2 * PI * r

# 求圆的面积
def func4(r):
    return PI * r ** 2
# print(type(__name__))
# print(__name__)
# if 如果直接运行的是当前模块:
if __name__ == '__main__':
    print(f'圆周率取值 = {PI}')
    length = eval(input('请输入要求的矩形的长:'))
    width = eval(input('请输入要求的矩形的宽:'))
    print(f'长为{length} 宽为{width} 的矩形的周长为{func1(length,width)}')
    print(f'长为{length} 宽为{width} 的矩形的面积为{func2(length,width)}')
    r = eval(input('请输入要求的圆的半径:'))
    print(f'半径为{r}的圆的周长为{func3(r)}')
    print(f'半径为{r}的圆的面积为{func4(r)}')
