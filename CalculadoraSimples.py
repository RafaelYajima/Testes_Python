# Calculadora simples

num1 = float(input("Digite o primeiro numero:"))
num2 = float (input("Digite o segundo numero:"))
operaçao = input("Digite a operaçao da conta:")

if operaçao == "+" :
    result = num1 + num2
elif operaçao == "-" :
    result = num1 - num2
elif operaçao == "*" :
    result = num1 * num2
elif operaçao == "/" :
    result = num1 / num2
else:
    print("Nao é uma operaçao valida")

print("O resultado é:",result)

