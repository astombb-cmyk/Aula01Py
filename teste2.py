def calculator ():
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        operation = input("Digite a operação (+, -, *, /): ")
        
        if operation == "+":
                result = num1 + num2
        elif operation == "-":
                result = num1 - num2
        elif operation == "*":
                result = num1 * num2
        elif operation == "/":
                if num2 != 0:
                 result = num1 / num2
                return "Erro: Divisão por zero não é permitida."
        else:
                return "Operação inválida."
        
         
        print(f"O resultado de {num1} {operation} {num2} é: {result}")
        return result     
              
calculator()