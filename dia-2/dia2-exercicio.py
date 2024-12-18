# 1 - Crie um programa que declare as seguintes variáveis:
# ● nome: seu nome.
# ● idade: sua idade.
# ● altura: sua altura.
# ● estudante: se você é estudante ou não (True/False).

nome = "Matheus"
idade = 29
altura = 1.75
estudante = True



# 2. Exibindo Informações
# Utilize a função print() para exibir as informações das variáveis criadas no exercício
# anterior.

print("Nome: ",nome)
print("Idade: ", idade)
print("Altura: ", altura)
print("Estudante: ", estudante)

# 3. Operações Simples
# Calcule o ano de nascimento com base na idade (considerando que o ano atual é 2023).

ano_nascimento = 2023 - idade
print("Ano de Nascimento: ", ano_nascimento)

# Verifique se a pessoa é maior de idade (idade >= 18) e armazene o resultado em uma
maior_de_idade = idade >= 18
print("Maior de idade: ", maior_de_idade)

# 4. Manipulação de Strings
# Crie uma variável frase que contenha a mensagem: "Olá, meu nome é [seu nome] e eu
# tenho [sua idade] anos."

frase = "Olá, meu nome é " + nome + " e eu tenho " + str(idade) + " anos."

print(frase)


# 5. Calculadora Simples
# ● Peça ao usuário para inserir dois números e armazene-os em variáveis.
# ● Calcule a soma, subtração, multiplicação e divisão desses números.
# ● Exiba os resultados

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print("Soma: ", soma)
print("Subtração: ", subtracao)
print("Multiplicação: ", multiplicacao)
print("Divisão: ", divisao)


# Desafios Extras

# 1. Conversor de Temperaturas
# Crie um programa que converta uma temperatura de graus Celsius para Fahrenheit.
# ● Fórmula: F = C * 9/5 + 32

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 9/5 + 32

print("A temperatura em Fahrenheit é: ", fahrenheit)


# 2. Calculando a Área de um Círculo
# Crie um programa que calcule a área de um círculo com base no raio fornecido pelo
# usuário.
# ● Fórmula: Área = π * raio²
# ● Use π = 3.14159

raio = float(input("Digite o valor do raio: "))

pi = 3.14159

area = pi * (raio ** 2)

print("A área do círculo é: ", area)