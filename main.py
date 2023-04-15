import math
import sympy
import sys
'''
函数 b1 b2 N 初值
问题1：
cos(x)-x,1e-6,1e-4,10,0.785398163  
问题2：
exp(-x)-sin(x),1e-6,1e-4,10,0.6
问题3：
x-exp(-x),1e-6,1e-4,10,0.5
问题4：
x*x-2*x*exp(-x)+exp(-2*x),1e-6,1e-4,20,0.5 
'''


def newton():
    print("函数f(x)"'\t'"精度b1"'\t'"精度b2"'\t'"最大迭代次数N"'\t'"初值alpha")
    func_str, b1, b2, N, x0 = input().split(',')
    b1 = float(b1)
    b2 = float(b2)
    N = int(N)
    x0 = float(x0)

    # 将字符串表达式转换为符号表达式
    x = sympy.symbols('x')
    func = sympy.sympify(func_str)

    # 对 func 求一阶导数
    dfunc = sympy.diff(func, x)

    n = 1
    while n <= N:
        F = func.subs(x,x0).evalf()
        DF = dfunc.subs(x,x0).evalf()
        if abs(F) < b1:
            print(x0)
            sys.exit(0)
        if abs(DF) < b2:
            print("失败")
            sys.exit(0)
        x1 = x0 - F/DF
        Tol = abs(x0-x1)
        if abs(Tol) < b1:
            print(x1)
            sys.exit(0)
        n = n + 1
        x0 = x1
    print("失败")
    sys.exit(0)


if __name__ == '__main__':
    newton()
