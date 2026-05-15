# 1) Soma de dois números
# Enunciado:
#  - Peça ao usuário dois números inteiros.
#  - Calcule a soma deles e mostre o resultado.
# Entrada:
#  - n1, n2
# Saída:
#  - "A soma de n1 e n2 é: X"

""" numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))

soma = numero1 + numero2
print(f"A soma de {numero1} + {numero2} é: {soma}")"""

# 2) Verificar se um número é par
# Enunciado:
#  - Peça um número inteiro ao usuário.
#  - Verifique se ele é par (divisível por 2).
#  - Mostre "O número é par" ou "O número é ímpar".

""" numero = int(input("Digite um numero: "))
if(numero % 2 == 0):
    print("Par")
else:
    print("impar") """

# 3) Maior de dois números
# Enunciado:
#  - Peça dois números ao usuário.
#  - Compare e mostre qual é o maior.
#  - Se forem iguais, mostre que são iguais.
# Dica:
#  - Use if/elif/else.

""" numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))

if(numero1 > numero2):
    print(f"{numero1} é maior que {numero2}")
elif (numero2 > numero1):
    print(f"{numero1} é menor que {numero2}")
else:
    print("Eles são iguais") """

# 4) Classificação por idade
# Enunciado:
#  - Peça a idade do usuário.
#  - Classifique:
#       idade >= 18  -> "Maior de idade"
#       idade >= 16  -> "Adolescente"
#       caso contrário -> "Menor de idade"
# Observação:
#  - Ajuste as regras conforme seu aprendizado.

""" idade = int(input("Digite sua idade: "))

if(idade >= 18):
    print("Maior de idade")
elif(idade >= 16):
    print("Adolescente")
else:
    print("Criança") """

# 5) Contar de 1 até N
# Enunciado:
#  - Peça um número inteiro N.
#  - Mostre todos os números de 1 até N (inclusive), um por linha.
# Dica:
#  - Use um laço for.

""" num = int(input("Digite um numero: "))

for i in range(0,num + 1):
    print(i) """

# 6) Fatorial
# Enunciado:
#  - Peça um número inteiro N (assumir N >= 0).
#  - Calcule o fatorial de N (N!):
#       0! = 1
#       1! = 1
#       2! = 2
#       3! = 6
#       ...
# Dica:
#  - Use um laço for.

""" num = int(input("Digite um numero: "))
fatorial = 1
for i in range(1, num +1 ):
    if(i <= num):
        fatorial = i * fatorial

print(fatorial) """

# 7) Tabuada de um número
# Enunciado:
#  - Peça um número inteiro X.
#  - Mostre a tabuada de X de 1 a 10 no formato:
#       X x i = resultado
#    onde i varia de 1 até 10.

""" num = int(input("Digite um numero: "))
print(f"A tabuada do {num} é: ")
for i in range(1,11):
    print(num*i) """

# 8) Soma dos números pares até N
# Enunciado:
#  - Peça um número inteiro N.
#  - Calcule a soma de todos os números pares de 0 (ou 2) até N.
#  - Mostre o resultado.
# Dica:
#  - Combine laço + condição (paridade).

""" num = int(input("Digite um numero: "))
soma = 0
for i in range(1, num):
    if(i % 2 == 0):
        soma += i

print(f"A soma de todos os numeros pares até {num} é: {soma}") """

# 9) Verificar palpite: maior/menor (jogo simples)
# Enunciado:
#  - Defina um número secreto fixo (por exemplo, 7) ou escolha um número secreto manualmente.
#  - Peça ao usuário para tentar adivinhar o número.
#  - Enquanto o usuário não acertar:
#       - Se o palpite for menor, mostre "Tente um número maior".
#       - Se o palpite for maior, mostre "Tente um número menor".
#  - Quando acertar, mostre "Você acertou!" e quantas tentativas foram.
# Dica:
#  - Use um while.
# ------------------

""" sorteado = 5
palpite = int(input("Tente acertar um numero de 0 a 10: "))

while(palpite != sorteado):
    if(palpite < sorteado):
        print("tente um numero maior")
    else:
        print("Tente um numero menor")
    palpite = int(input("Tente acertar um numero de 0 a 10: "))

print("Você acertou") """

# 10) Contagem regressiva (loop)
# Enunciado:
#  - Peça um número inteiro N.
#  - Mostre uma contagem regressiva de N até 0, um por linha.
#  - No final, mostre "Fim!".
# Dica:
#  - Use um laço while ou for.

num = int(input("Digite um numero: "))

for i in reversed(range(num+1)):
    print(i)

print("Fim!")