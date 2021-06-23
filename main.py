# Задание 1 вариант 2
import sympy as sy
x = sy.symbols('x')
x0 = 10
def derivation (x):
    f = sy.diff(sy.cos(x) + 0.05 * x**3 + sy.log(x**2,2), x)
    return f.subs(x, x0).evalf()
print (round (derivation (x), 2))

# Задание 2
import sympy as sy
x1, x2 = sy.symbols ('x1 x2')
f = x1**2 * sy.cos(x2) + 0.05 * x2**3 + 3 * x1**3 * sy.log(x2**2, 2)
def gradient(f, x, y):
    grad_x1 = sy.diff(f, x1).subs([(x1,x), (x2,y)]).evalf()
    grad_x2 = sy.diff(f, x2).subs([(x1,x), (x2,y)]).evalf()
    return round (grad_x1,2), round (grad_x2, 2)
print (gradient(f, 10, 1))

# Задание 3
import sympy as sy
x = sy.symbols ('x')
x0 = 10
def gradient_optimization_one_dim (x):
    return sy.cos(x) + 0.05 * x**3 + sy.log(x**2, 2)
for i in range(50):
    d = sy.diff(gradient_optimization_one_dim (x), x).subs(x, x0).evalf()
x0 = x0 - 0.001 * d
print (round (d, 2))

# Задание 4
import sympy as sy
x1, x2, x, y = sy.symbols ('x1 x2 x y')
x0 = 4
y0 = 10
def gradient_optimization_multi_dim (x, y):
    return x1**2 * sy.cos(x2) + 0.05 * x2**3 + 3 * x1**3 * sy.log(x2**2, 2)
for i in range(50):
    g_x1 = sy.diff(gradient_optimization_multi_dim (x, y), x1).subs([(x1,x0), (x2,y0)]).evalf()
    g_x2 = sy.diff(gradient_optimization_multi_dim (x, y), x2).subs([(x1,x0), (x2,y0)]).evalf()
    x0 = x0 - 0.001 * g_x1
    y0 = y0 - 0.001 * g_x2
print (round (g_x1, 2), round (g_x2, 2))