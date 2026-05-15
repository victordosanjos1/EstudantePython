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

num = int(input("Digite um numero: "))

for i in range(0,num + 1):
    print(i)