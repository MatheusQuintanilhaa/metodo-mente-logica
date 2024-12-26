#  operadores aritméticos

a = 5
b = 2

print(a + b)
print(a * b)
print(a / b)

# ** - exponenciação
#  / / - divisão inteira

print( a // b)
print( a / b)
print( a % b)

# operadores de comparação
x = 10
y = 5

print(x > 5)
print(x < 5)
print(x != 5)

print(5 >= 5)
# menor OU igual a outro = TRUE
print(5 <= 1)

# operadores lógicos
# AND, OR e NOT

# unir comparações

idade = 20
possui_carteira = True

pode_dirigir = (idade >= 18) and possui_carteira

print(pode_dirigir)

# AND só é verdadeiro quando ambas operações resultem em TRUE
# OR só é verdadeiro quando pelo menos uma operação é TRUE

eh_estudante = False
idade = 60

#  1 = é atribuição
#  2 == é comparação
meia_entrada = eh_estudante == True or idade >= 60

print(meia_entrada)

# NOT = inverter um booleano

chovendo = True
nao_chovendo = not chovendo

print('Chovendo ', chovendo)
print('Não Chovendo ', nao_chovendo)

# if -> chovendo == False, not chovendo

# revisão
#  nota > 7 e frequencia  > 80%

nota = 8
frequencia = 60

passou_de_ano =( nota > 7 ) and (frequencia >= 80)

print("Passou de ano: ", passou_de_ano)

#  senhas iguais
#  criando um registro de usuário
senha = "teste123"
confirmacao_senha = "teste1234"

aviso_senha_errada = senha != confirmacao_senha

print("A senha não combina? ", aviso_senha_errada)

# mesa de bar
#  123.85
# quanto cada pessoa vai pagar? 3

conta = 123.85
pessoas = 3

parte_de_cada_um = conta / pessoas

print("Cada um tem que pagar: ", parte_de_cada_um)