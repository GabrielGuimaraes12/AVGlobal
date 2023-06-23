from sympy import symbols, Eq, solve

# Variáveis simbólicas para as correntes
I1, I2, I3 = symbols('I1 I2 I3')
mat=126%10
# Valores das resistências e tensões
R1 = 25
R2 = 10
R3 = 20
V1 = 7 + (2 * mat)
V2 = 12 + (2 * mat)

# Equações do sistema
eq1 = Eq(25 * I1 + 10 * I2 + 20 * I3, V1)
eq2 = Eq(I1 - (I2 + I3), 0)
eq3 = Eq(10 * I2 + 20 * I3, V2)

# Resolvendo o sistema de equações
sol = solve((eq1, eq2, eq3), (I1, I2, I3))

# Obtendo os valores das correntes
I1_val = sol[I1]
I2_val = sol[I2]
I3_val = sol[I3]

# Imprimindo as correntes
print(f"Corrente I1: {I1_val}")
print(f"Corrente I2: {I2_val}")
print(f"Corrente I3: {I3_val}")
