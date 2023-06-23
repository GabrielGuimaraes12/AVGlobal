from sympy import Symbol, integrate

# Define a variável simbólica
x = Symbol('x')
mat=126%10
# Define a função da força
F = (x**2)/5 + (x**5/4) + (mat + 3)*x - 10

# Define os limites de integração
x1 = 1  # Posição inicial
x2 = 12  # Posição final

# Calcula o trabalho realizado pela força
trabalho = integrate(F, (x, x1, x2))

# Imprime o resultado
print(trabalho)
