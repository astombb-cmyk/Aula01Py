def formulario( ):

    nome = input("digite seu nome: ")
    idade = int(input("digite sua idade: "))
    sexo = input("digite seu sexo: ")
    profissao = input("digite sua profissão: ")

    
        
    print(f"\nformulario preenchido com sucesso!\n")
    return f'Nome: {nome}\nIdade: {idade}\nSexo: {sexo}\nProfição: {profissao}'



print(formulario())