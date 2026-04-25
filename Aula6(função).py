def saudacoes():
    print("Olá munndo!")

saudacoes()

def bemVindo(nome):
    print(f"Olá {nome}")

bemVindo("João")

def soma(a,b):
    return a + b

resultado = soma(3,5)
print(resultado)

numeros = [5,10,12,15]
def somaLista(numeros):
    total = 0
    for n in numeros:
        total+=n
    return total

print(somaLista(numeros))

def areaQuadrado():
    lado = int(input("Digite o valor do lado do quadrado: "))
    resultado = lado**2
    print(f"O resultado é {resultado}")
    return resultado

areaQuadrado()