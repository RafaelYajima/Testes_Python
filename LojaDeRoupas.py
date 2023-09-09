# Programa pra calcular o valor final da vendo de um produto

produto = float(input("Digite o valor do produto:"))
modo = float(input("Digite o modo de pagamento 1(A vista), 2(A prazo):"))

if modo == 1:
    print("Pagamento a vista com deconto")
 
    if produto > 500:
        result = produto * 0.90
    elif produto > 1000 :
        result = produto * 0.80

elif modo == 2:
    print("Pagamento feito a prazo")
elif produto >= 800 :
    print("Pode ser parcelado acima de 5x")
else:
    print("Nao podera fazer parcelas")



