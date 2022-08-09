#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
#mostrando uma mensagem de erro e voltando a pedir as informações.
    

def verifica_igualdade(nome, senha):

    _nome   = str(nome)
    _senha  = str(senha)

    i = 0
    while _nome == _senha:
        i=i+1
        print("Digite uma senha diferente! ")

        _nome  = str(input("Digite novamente o nome: "))
        _senha = str(input("Digite novamente a senha: "))

    else:
        print("Senha boa.")


n  = input("Digite um nome: ")
s  = input("Digite uma senha: ")

verificacao = verifica_igualdade(n, s)

