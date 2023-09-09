print("=================================================")
print ("=-=-=-=-= Calculadora de juros simples =-=-=-=-=")
print("=================================================")

p = float(input("Digite o valor principal:"))
tanual = float(input("Digite a taxa de juros anual:"))
tanos = float(input("Digite o tempo em anos:"))

print("=================================================")

montante = p + (p * tanual * tanos)

print("Seu montante é;",montante)