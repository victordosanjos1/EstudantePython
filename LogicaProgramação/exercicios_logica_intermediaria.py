# Exercícios de Lógica de Programação Intermediários (10)
#
# Objetivo: treinar lógica com desafios um pouco mais completos.
# Formato sugerido: para cada exercício, implemente em Python usando input/print,
# variáveis, operadores, estruturas condicionais (if/elif/else), laços (for/while)
# e, quando fizer sentido, listas e dicionários.
#
# Como usar:
# - Copie/abra este arquivo e resolva cada exercício.
# - Se preferir, comente a execução final e execute cada exercício isoladamente.


def apresentacao():
    print("Bem-vindo! Estes são 10 exercícios INTERMEDIÁRIOS de lógica para praticar.")
    print("Resolva um por vez. Pense nas entradas, saídas e nas regras.")
    print("\n--- Instrução ---")
    print("Cada exercício abaixo contém enunciado, requisitos e dica.")
    print("\nBoa prática!")


if __name__ == "__main__":
    apresentacao()

# ------------------------------------------------------------------------------
# 1) Validador de senha (com regras)
# Enunciado:
#  - Crie um validador de senha.
#  - O usuário digita uma senha (string).
#  - Regras para ser aceita:
#      * tamanho entre 8 e 20 (inclusive)
#      * deve conter pelo menos 1 letra
#      * deve conter pelo menos 1 número
#      * não pode conter espaços
#  - Se a senha for válida: imprimir "Senha válida"
#  - Caso contrário: imprimir "Senha inválida" e mostrar quais regras falharam.
# Requisitos:
#  - Use if/elif/else e uma ou mais variáveis/condições.
#  - Percorra a string para checar letras/números.
# Dica:
#  - Use str.isalpha() e str.isdigit() para identificar caracteres.
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# 2) Estatísticas de uma lista (mínimo, máximo e média)
# Enunciado:
#  - Peça ao usuário uma lista de números inteiros.
#  - Forma de entrada (exemplo): 1, 5, -2, 10
#  - Calcule:
#      * menor valor
#      * maior valor
#      * média (soma / quantidade)
#  - Mostre em linhas diferentes.
# Requisitos:
#  - Converter entrada de texto para lista (use split).
#  - Percorrer a lista para somar e comparar.
# Dica:
#  - Ao calcular média, trate como float.
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# 3) Número primo (com otimização)
# Enunciado:
#  - Peça um número inteiro N.
#  - Verifique se N é primo.
#  - Mostre "primo" ou "não primo".
# Requisitos:
#  - Use laço para testar divisores.
#  - Otimização: testar divisores até a raiz quadrada de N.
#  - Considere casos especiais: N <= 1.
# Dica:
#  - Use i*i <= N em vez de calcular raiz.
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# 4) Fila de atendimento (simulação)
# Enunciado:
#  - Você recebe uma lista de clientes na fila (inteiros representando prioridade).
#  - O atendente segue a regra:
#      * a cada iteração, ele atende o próximo cliente
#      * se a prioridade do cliente for >= 5, ele ganha 1 ponto extra
#  - O processo continua até a fila acabar.
#  - Mostre:
#      * quantos clientes foram atendidos
#      * quantos tinham prioridade >= 5
#      * a pontuação total
# Requisitos:
#  - Use listas e possivelmente pop(0) (ou índice) para avançar.
#  - Use while para simular.
# Dica:
#  - Evite pop(0) se quiser eficiência; use um índice.
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# 5) Jogo: acertar a sequência (lógica com tentativas)
# Enunciado:
#  - Crie uma sequência secreta de 4 números (ex: [2, 4, 6, 8]).
#  - O usuário tenta adivinhar digitando 4 números.
#  - Para cada tentativa, compare:
#      * quantos números estão na posição correta (acertos de posição)
#      * quantos números existem na sequência, mas em posição diferente (acertos fora)
#  - Mostre o feedback a cada tentativa.
#  - O usuário pode tentar até 5 vezes.
#  - Se acertar tudo, imprimir "Você venceu!" e encerrar.
#  - Se acabar as tentativas, imprimir "Fim do jogo".
# Requisitos:
#  - Use loops, comparações e controle de tentativas com while/for.
#  - Use listas.
# Dica:
#  - Primeiro conte acertos de posição. Depois conte comuns usando contagem.
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# 6) Somador com desconto por faixa
# Enunciado:
#  - Peça ao usuário uma lista de valores (inteiros).
#  - Regras de desconto:
#      * se o valor individual >= 100, desconto de 20%
#      * se o valor individual >= 50 e < 100, desconto de 10%
#      * caso contrário, sem desconto
#  - Calcule:
#      * total antes do desconto
#      * total depois do desconto
#      * desconto total
# Requisitos:
#  - Percorrer a lista e aplicar if/elif/else em cada item.
#  - Trabalhar com floats ou arredondar (decida no seu código).
# Dica:
#  - Trabalhe com total_desconto somando (valor - valor_com_desconto).
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# 7) Mapa de frequências (dicionário)
# Enunciado:
#  - Peça ao usuário uma frase.
#  - Ignore espaços e considere letras (case-insensitive).
#  - Crie um dicionário com a frequência de cada letra.
#  - Mostre as 3 letras mais frequentes (em ordem decrescente).
# Requisitos:
#  - Use dicionário para contagem.
#  - Ordene itens do dicionário.
# Dica:
#  - Use frase.lower() e para cada char que não seja espaço: d[char]+=1.
#  - Ordene com sorted(d.items(), key=lambda x: x[1], reverse=True).
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# 8) Gerador de padrões (controle de linhas/colunas)
# Enunciado:
#  - Peça ao usuário um inteiro N (N >= 1).
#  - Imprima um padrão quadrado de tamanho N:
#      * na borda, mostre "*"
#      * no interior, mostre "-"
#  - Exemplo para N=4:
#      * * * *
#      * - - *
#      * - - *
#      * * * *
#  - (Separar por espaço para ficar legível)
# Requisitos:
#  - Use laços aninhados (for dentro de for).
#  - Use condição para identificar borda.
# Dica:
#  - Uma posição está na borda se i==0 ou j==0 ou i==N-1 ou j==N-1.
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# 9) Caminho em grid (simulação simples com regra)
# Enunciado:
#  - Defina um grid 5x5 (coordenadas 0..4).
#  - O usuário inicia em (0,0).
#  - O usuário digita comandos: U, D, L, R.
#  - Regra:
#      * mover U diminui a linha (se não sair do grid)
#      * mover D aumenta a linha (se não sair do grid)
#      * mover L diminui a coluna (se não sair do grid)
#      * mover R aumenta a coluna (se não sair do grid)
#  - O objetivo é chegar na posição (4,4).
#  - A cada comando inválido (que sair do grid), mostre "Movimento inválido".
#  - Conte quantos comandos o usuário usou até chegar.
#  - Encerre quando chegar.
# Requisitos:
#  - Use while para continuar recebendo comandos.
#  - Use if/elif/else para atualizar posição.
# Dica:
#  - Valide antes de aplicar a mudança (checar se a nova coordenada está dentro de 0..4).
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# 10) Lista de compras com remoção e total
# Enunciado:
#  - Crie uma lista de compras onde o usuário pode:
#      * adicionar item (nome e preço)
#      * remover item pelo nome
#      * listar itens
#      * sair
#  - Faça um menu com opções 1..4.
#  - Imprima o total geral dos preços quando listar.
# Requisitos:
#  - Use lista (para itens) e/ou dicionário (nome->preço).
#  - Use while com menu e validação de opção.
#  - Tratamento: se item não existir, informar.
# Dica:
#  - Um dicionário simplifica remoção por nome: itens[nome]=preço.
# ------------------------------------------------------------------------------


