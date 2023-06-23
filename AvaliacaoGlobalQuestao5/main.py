import sympy as sp

# Definindo as variáveis
x = sp.symbols('x')
c = 126%10

# Equação 1: 𝑒^(-𝑥−1) + 𝑒^(-𝑥−3) + 𝑒^𝑥 = -5(𝑐+1)
equation1 = sp.exp(-x-1) + sp.exp(-x-3) + sp.exp(x) + 5*(c+1)

# Equação 2: (𝑐+2)𝑥^3 - (𝑐+1)𝑥^2 - 5𝑥 = -4𝑐
equation2 = (c+2)*x**3 - (c+1)*x**2 - 5*x + 4*c

# Equação 3: 2sin[4(𝑐−3)𝑥] = 10
equation3 = 2*sp.sin(4*(c-3)*x) - 10

# Resolvendo as equações
solutions1 = sp.solve(equation1, x)
solutions2 = sp.solve(equation2, x)
solutions3 = sp.solve(equation3, x)

print("Soluções da Equação 1:")
for sol in solutions1:
    print("x =", sol.evalf())

print("\nSoluções da Equação 2:")
for sol in solutions2:
    print("x =", sol.evalf())

print("\nSoluções da Equação 3:")
for sol in solutions3:
    print("x =", sol.evalf())
