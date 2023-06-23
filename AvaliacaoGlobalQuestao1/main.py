from sympy import Symbol, sqrt, limit, oo

# Define a variável simbólica
x = Symbol('x')
c=126%10
# Define a função
f1 = ((c+1)-sqrt(x))/((c+1)**2-x)

# Calcula o limite em infinito
limite1 = limit(f1, x, (c+1)**2)

# Imprime o resultado
print(limite1)

# Define a função
f2 = ((c+1)-sqrt(x))/((c+1)**2-x)

# Calcula o limite em infinito
limite2 = limit(f2, x, oo)

# Imprime o resultado
print(limite2)

# Define a função
f3 = ((c+1)-sqrt(x))/((c+1)**2-x)

# Calcula o limite em infinito
limite3 = limit(f3, x, -oo)

# Imprime o resultado
print(limite3)