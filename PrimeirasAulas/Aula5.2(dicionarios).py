import sys
sys.stdout.reconfigure(encoding='utf-8')
pessoa = {"nome": "João", "idade": "20", "cidade": "Joinville"}

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])

print(pessoa.keys()) #Vai imprimir nome, idade, cidade
print(pessoa.values()) #Vai imprimir João, 20, joinville
print(pessoa.items()) #Vai imprimir tudo

pessoa.update({"Profissão": "Jogador"})
print(pessoa)