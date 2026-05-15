ponto = (1, 2)

print(ponto)

minha_tupla = (1, 2, 3, 2, 4, 2)


print (minha_tupla.index(2)) #Aqui ele vai procurar o número 2 e retornar a posição do primeiro número 2 encontrado, que é a posição 1

print (minha_tupla.index(2, 2))   #Aqui ele vai procurar o número 2 a partir da posição 2, ou seja, ele vai ignorar o número 2 que está na posição 1 e procurar o próximo número 2, que está na posição 3

print (minha_tupla.index(2, 2, 4))   #Aqui ele vai procurar o número 2 a partir da posição 2 até a posição 4, ou seja, ele vai ignorar o número 2 que está na posição 1 e procurar o próximo número 2, que está na posição 3, mas ele não vai considerar o número 2 que está na posição 5, porque ele está fora do intervalo definido
