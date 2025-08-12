#DESCONTO POR TIPO DE CLIENTE: SOLICITE O NOME DO CLIENTE E O VALOR DA COMPRA
#SE TIPO DO CLIENTE COMUM, VIP E PREMIUM
#VALOR DA COMPRA
#DESCONTO COMUM - 0%, VIP 10%, PREMIUM 20%
#MOSTRA O VALOR FINAL DA COMPRA

#Entrada de dados do cliente(nome e valor da compra)
nome_cliente = str(input("Informe o nome do cliente: ")).upper().strip()
valor_compra = float(input("Informe o valor da compra: R$"))
tipo_cliente = int(input("### Tipo do Cliente ###\n[1] - COMUM\n[2] - VIP\n[3] - PREMIUM\n"))

if (tipo_cliente == 1):
    print(f"Você selecionou o cliente comum, desconto de 0%.\nValor da compra é de R${valor_compra}.")
elif (tipo_cliente == 2):
    valor_compra_vip = valor_compra - (valor_compra * 0.1)
    print(f"Você selecionou o cliente VIP, desconto de 10% aplicado.\nValor da compra é de R${valor_compra_vip}.")
elif (tipo_cliente == 3):
    valor_compra_premium = valor_compra - (valor_compra * 0.2)
    print(f"Você selecionou o cliente PREMIUM, desconto de 20% aplicado.\nValor da compra é de R${valor_compra_premium}.")
