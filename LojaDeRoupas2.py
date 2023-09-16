valor_produtos = float(input("Informe o total em produtos: "))
forma_pagamento = input("Informar a forma de pagamento? (1 vista, 2 prazo): ")
valor_final = 0

if forma_pagamento == '1' :
    valor_final = valor_produtos - valor_produtos * 0.1 
    valor_final -= valor_produtos * 0.5 if valor_produtos > 500 else 0
    valor_final -= valor_produtos * 0.5 if valor_produtos > 1000 else 0

elif forma_pagamento == '2' :
    max_parcelas = "18" if valor_produtos > 800 else '5'
    print(f"voce pode parcelar em até {max_parcelas} vezes.")

    quantidade_parc = int(input("Em quantas parcelas deseja fazer o parcelamento?: /n"))

    if(valor_produtos < 800 and quantidade_parc > 5 or quantidade_parc < 2):
        print("Quantidade nao permitida!")
        possui_erro = True
    elif(quantidade_parc > 18) :
        print("QUantidade nao permitida.")
        possui_erro = True
    else :
        possui_erro = False
        if (quantidade_parc > 10) :
            if quantidade_parc == 11 : juros = 0.05
            elif quantidade_parc == 12 : juros = 0.065
            elif quantidade_parc == 13 : juros = 0.07
            elif quantidade_parc == 14 : juros = 0.09
            elif quantidade_parc == 15 : juros = 0.095
            elif quantidade_parc == 16 : juros = 0.1
            elif quantidade_parc == 17 : juros = 0.113
            elif quantidade_parc == 18 : juros = 0.12

            valor_final = valor_produtos + valor_produtos * (juros * quantidade_parc)
        else :
            valor_final = valor_produtos
        
        valor_parcela = valor_final / quantidade_parc
else :
    print ("Forma de pagamento invalida!")

if not possui_erro:
    if(forma_pagamento == '1') :
        print(f"O valor total da conta é de {valor_final}")
        print("Total de desconto: %.2f", valor_produtos - valor_final)
    else : 
        print("O valor total da comrpaa é de %.2f" % valor_final)
        print("Sera pago em %i de %.2f" % (quantidade_parc, valor_parcela))

print("Obrigado!")

