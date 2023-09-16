# Programa pra calcular o valor final da vendo de um produto

produto = float(input("Digite o valor do produto:"))
modo = float(input("Digite o modo de pagamento 1(A vista), 2(A prazo):"))

if modo == 1:
    print("Pagamento a vista com deconto")
 
    if produto > 500:
        result = produto * 0.90
    elif produto > 1000 :
        result = produto * 0.80

        
    print("-----------------------------------------")
    print("O total a pagar é:",result,"reais")

if modo == 2:
    print("Pagamento feito a prazo")

    if produto >= 800 :
        print("Pode ser parcelado acima de 5x")
    else:
        print("Nao podera fazer parcelas")


    print("-----------------------------------------")


    print("Caso seja parcelado em mais do que 10x possui juros")
    parc = float(input("Digite quantas parcelas ira fazer até 18x: "))

    if parc > 10 and parc < 19:
    
        if parc == 11 :
            juros = produto * 0.05
            parcela = (produto / 11) + juros
            result2 = parcela * 11
        elif parc == 12 :
            juros = produto * 0.05
            parcela = (produto / 12) + juros
            result2 = parcela * 12
        elif parc == 13 :
            juros = produto * 0.05
            parcela = (produto / 13) + juros
            result2 = parcela * 13
        elif parc == 14 :
            juros = produto * 0.05
            parcela = (produto / 14) + juros
            result2 = parcela * 14
        elif parc == 15 :
            juros = produto * 0.05
            parcela = (produto / 15) + juros
            result2 = parcela * 15
        elif parc == 16 :
            juros = produto * 0.05
            parcela = (produto / 16) + juros
            result2 = parcela * 16
        elif parc == 17 :
            juros = produto * 0.05
            parcela = (produto / 17) + juros
            result2 = parcela * 17
        elif parc == 18 :
            juros = produto * 0.05
            parcela = (produto / 18) + juros
            result2 = parcela * 18
        else:
            print ("Nao é um numero de parcelas adequado")


    print("-----------------------------------------")
    

    print("O total a pagar é:",result2,"reais")