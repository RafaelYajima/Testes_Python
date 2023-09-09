# Programa para calcular juros simples

print("=================================================")
print ("=-=-=-=-= Calculadora de juros simples =-=-=-=-=")
print("=================================================")

p = float(input("Digite o valor principal:"))
tanual = float(input("Digite a taxa de juros anual em porcentagem:"))
tanos = float(input("Digite o tempo em anos:"))

print("=================================================")

montante = p + (p * (tanual/100) * tanos)

print("Seu montante é;",montante)