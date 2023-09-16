# Programa pra calcular o valor final da vendo de um produto

produto = float(input("Digite o valor do produto:"))
modo = float(input("Digite o modo de pagamento 1(A vista), 2(A prazo):"))

if modo == 1:
    if produto > 500 :
        result = produto * 0.90
    elif produto > 1000 :
        result = produto * 0.80
    print("O total a pagar é:",result,"reais")

if modo == 2:
    if produto <= 800 :
        print("Pode ser parcelado até 5x")
    elif produto > 800 :
        print("Pode ser parcelado em até 18x")
        print("-----------------------------------------")
        print("Caso seja parcelado em mais do que 10x possui juros")
    numparc = float(input("Digite quantas parcelas ira fazer: "))
    
    if numparc >= 0 and numparc <=18 :
        parcela = produto / numparc
        juros = produto * 0.5
        result2 = parcela * numparc
        if numparc >= 0 and numparc <= 5 :
            print("O total a pagar é: %.2f reais" % result2)
            print("Cada parcela sera de:  %.2f reais" % parcela)
        elif numparc > 10 and numparc <= 18 :
            print("-----------------------------------------")
            print("O total a pagar é:",result2,"reais")
            print("Cada parcela sera de:",parcela,"reais")
else:
    print ("Nao podera fazer parcelas")