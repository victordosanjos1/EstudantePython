nomes = ["Victor", "Maria", "João", "Ana", "Pedro"]

nomes.append("Lucas") # Adiciona um elemento no final da lista


nomes.insert(2, "Mateus") # Adiciona um elemento em uma posição específica

nomes.remove("Maria") # Remove um elemento da lista

nome_removida = nomes.pop(3) # Remove um elemento em uma posição específica e retorna o elemento removido

nomes.sort() # Ordena a lista em ordem alfabética

nomes.reverse() # Inverte a ordem da lista


numeros = [5, 2, 9, 1, 3]
quadrados = [x**2 for x in numeros] # Cria uma nova lista com os quadrados dos números da lista original
print(quadrados)