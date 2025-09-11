#Peça um número inteiro e verifique se ele é par e positivo.

#Entrada de dados do usuario com o numero desejado
num1 = int(input("Informe um número inteiro qualquer: "))

#Verifica se é positivo e par
verifica_num = num1 % 2 == 0 and num1 > 0

#Imprime se o número digitado é par e positivo
print(f"O número {num1} é PAR e POSITIVO? {verifica_num}.")
