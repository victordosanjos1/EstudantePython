print("=================================")
print("Exercícios de Lógica Intermediária")
print("=================================")
print("1) Validador de senha (com regras)")

senha = input("Digite uma senha: ")
lersenha = len(senha)
if (lersenha >= 8 and lersenha <= 20):
    if (senha.isalpha() == False and senha.isdigit() == False):
        if (senha.find(" ") == -1):
            print("Senha válida")
        else:
            print("Senha inválida, não pode conter espaços")
    else:
        print("Senha inválida, deve conter pelo menos 1 letra e 1 número")
else:
    print("Senha inválida, deve conter entre 8 e 20 caracteres")
