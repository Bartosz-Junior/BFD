#PEÇA UM NÚMERO E CALCULE O SEU QUADRADO E SUA RAIZ QUADRADA

#Entrada de dados pelo usuario com os numeros que deseja calcular
num1 = float(input("Informe o número que deseja verificar o quadrado e a raiz quadrada: "))

#Calculando o quadrado e a raiz
quad_num1 = num1 ** 2
raiz_num1 = num1 ** (1/2)

print(f"O quadrado de {num1} é {quad_num1} e sua raiz quadrada é {raiz_num1}.")
