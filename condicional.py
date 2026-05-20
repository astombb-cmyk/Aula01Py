def formulario():
    idade = input("Qual é a sua idade?: ")

    try:
        idade = int(idade)
    except ValueError:
        print("Idade inválida")
        return

    if idade >= 18:
        print("Autorizado")
    else:
        print("Não autorizado")
        return

    senha = "Lrs12345"
    digitasenha = input("Digite sua senha: ")

    if digitasenha == senha:
        print("Acesso permitido")
    else:
        print("Acesso Negado")

formulario()