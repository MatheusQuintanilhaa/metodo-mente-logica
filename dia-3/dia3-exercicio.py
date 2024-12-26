# 1. Calculando o Troco
# Você foi a uma padaria e comprou alguns itens:
# ● Pão: R$3.50
# ● Leite: R$4.20
# ● Café: R$2.80
# Você pagou com uma nota de R$20. Calcule quanto de troco você deve receber.

pao = 3.50
leite = 4.20
cafe = 2.80

total_compra = pao + leite + cafe

valor_pago = 20

troco = valor_pago - total_compra

print("Total da compra: R$", total_compra)
print("Troco a receber: R$", troco)


# 2. Verificando Aprovação em um Exame
# Para ser aprovado em um exame, um estudante precisa ter uma nota média maior ou igual
# a 7.0 e uma frequência maior ou igual a 75%.
# Dados:
# ● Nota média: 8.5
# ● Frequência: 80%
# Verifique se o estudante foi aprovado

nota_media = 8.5
frequencia = 80

aluno_aprovado = (nota_media >= 7) and (frequencia >= 75)

print("O aluno foi aprovado? ", aluno_aprovado)

# 3. Oferta Especial
# Uma loja oferece um desconto se o cliente comprar mais de 10 itens ou se o valor total da
# compra for superior a R$100.
# Dados:
# ● Quantidade de itens: 8
# ● Valor total: R$120
# Verifique se o cliente tem direito ao desconto.

quantidade_itens = 8
valor_total = 120.00

direito_desconto = (quantidade_itens > 10) or (valor_total > 100)

print("O cliente tem direito ao desconto? ", direito_desconto)


# 4. Sistema de Acesso
# Para acessar uma área restrita, o usuário deve inserir a senha correta e não pode estar
# bloqueado.
# Dados:
# ● Senha inserida: "abcd1234"
# ● Senha correta: "abcd1234"
# ● Usuário bloqueado: False
# Verifique se o acesso deve ser concedido.

senha_inserida = "abcd1234"
senha_correta = "abcd1234"
usuario_bloqueado = False

verificar_acesso = (senha_inserida == senha_correta) and not usuario_bloqueado

print("Acesso concedido? ", verificar_acesso)

# 5. Divisão de Tarefas
# Três amigos vão dividir igualmente uma conta de R$150. Verifique quanto cada um deve
# pagar e se a divisão é exata (sem centavos restantes).

conta = 150.00
amigos = 3

valor_por_pessoa = conta / amigos

divisao_exata = (conta % amigos) == 0

print("Cada um deve pagar: R$", valor_por_pessoa)
print("A divisão é exata?", divisao_exata)


# Desafios Extras
# 1. Classificação Etária
# Crie um programa que verifica se uma pessoa pode assistir a um filme classificado como
# "maiores de 16 anos".
# Dados:
# ● Idade da pessoa: Pergunte ao usuário

idade = int(input("Digite a sua idade: "))

pode_assistir = idade >= 16

print("Pode assistir ao filme?", pode_assistir)

# 2. Calculadora de IMC
# O Índice de Massa Corporal (IMC) é calculado dividindo o peso (em kg) pela altura (em
# metros) elevada ao quadrado.
# Crie um programa que calcula o IMC e verifica se a pessoa está dentro do peso ideal (IMC
# entre 18.5 e 24.9).

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = round(peso / (altura ** 2), 2)

peso_ideal = (imc >= 18.5) and (imc <= 24.9)

print("Seu IMC é:", imc)
print("Você está no peso ideal?", peso_ideal)

# 3. Par ou Ímpar
# Crie um programa que solicita um número inteiro ao usuário e verifica se ele é par ou ímpar.

numero = int(input("Digite um numero inteiro: "))

eh_par = (numero % 2) == 0

print("O número é par?", eh_par)