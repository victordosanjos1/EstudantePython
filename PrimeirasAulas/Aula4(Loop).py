nomes = ["pedro", "joão", "lucas", "mateus", "gabriel"]

for nomes in nomes:
    print(nomes)

contador = 0

while contador < 5:
    print(contador)
    contador += 1

while True:
    print(contador)
    contador += 1
    if(contador == 10):
        break

print("========================================")
for i in range(10):
    if(i % 2 != 0):
        continue
    print(i)