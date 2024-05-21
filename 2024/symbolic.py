from sympy import Symbol, print_latex, sqrt, simplify
from sympy.solvers import solve
x = Symbol('x')
g = Symbol('\gamma')
s = Symbol('\sigma_\mathrm{th}^2')
e = Symbol('\epsilon')
d = Symbol('\delta')

F = e * x / ( sqrt(s+d*x) + sqrt(s) ) - g
y = solve(F, x)
y1 = y[1]
z = simplify(y1)