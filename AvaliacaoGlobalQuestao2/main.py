from sympy import Symbol, diff, lambdify

# Define a variável simbólica
x = Symbol('x')
mat = 126%10
# Define a função corretamente
s = ((x ** (1/3))/(5)) + ((mat+1)/(x**3)) - ((mat+2)*(x**2)) - 15

# Calcula a derivada da função em relação a x
v = diff(s, x)

# Cria uma função numérica para a derivada (velocidade)
funcao_velocidade = lambdify(x, v)

# Define o valor de x para calcular a velocidade
x_velocidade = 7

# Calcula a velocidade
velocidade = funcao_velocidade(x_velocidade)

# Imprime o resultado da velocidade
print("Velocidade:", velocidade)


# Calcula a segunda derivada da função em relação a x
a = diff(v, x)

# Cria uma função numérica para a segunda derivada (aceleração)
funcao_aceleracao = lambdify(x, a)

# Define o valor de x para calcular a aceleração
x_aceleracao = 2

# Calcula a aceleração
aceleracao = funcao_aceleracao(x_aceleracao)

# Imprime o resultado da aceleração
print("Aceleração:", aceleracao)
