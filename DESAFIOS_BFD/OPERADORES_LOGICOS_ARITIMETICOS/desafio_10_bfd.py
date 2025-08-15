#PEÇA DOIS NUMEROS INTEIROS E MOSTRE O RESULTADO DA DIVISÃO INTEIRA E O RESTO

#Entrada de dados pelo usuario com os numeros inteiros.
num1 = int(input("Informe o 1º valor: "))
num2 = int(input("Informe o 2º valor: "))

#Calculando a divisão inteira e o resto dos numeros informados
divisao_int = num1 // num2
resto_div = num1 % num2

print(f"A divisão inteira de {num1} por {num2} é {divisao_int}.")
print(f"O resto da divisão de {num1} por {num2} é {resto_div}.")
