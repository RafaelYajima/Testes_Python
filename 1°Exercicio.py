nome = (input("Digite o nome: "))
idade = (input("Digite o idade: "))
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))
 
imc = peso / altura**2

print("Ola",nome)
print("Sua idade é de:",idade,"anos")
print("Seu IMC é de:",imc)