#PEÇA UM NUMERO INTEIRO E  VERIFIQUE SE O RESTO DA DIVISÃO POR 3 É IGUAL A 1.

#Entrada de dados pelo usuario
num1 = int(input("Informe o dividendo: "))

#Resto da divisão de num1 por 3
divisao_3 = num1 % 3

#Verifica se o resto da divisão por 3 é igual a 1
verifica_resto = divisao_3 == 1

print(f"O valor {num1:.2f} dividido por 3 tem resto 1? {verifica_resto}")
