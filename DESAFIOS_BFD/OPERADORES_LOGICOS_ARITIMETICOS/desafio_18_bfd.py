#Solicite três números e verifique se pelo menos dois deles são iguais.

#Entrada de dados pelo usuario com 3 numeros quaisquer
num1 = float(input("Informe o 1º número: "))
num2 = float(input("Informe o 2º número: "))
num3 = float(input("Informe o 3º número: "))

#Verificando se pelo menos 2 deles são iguais
verifica_num = num1 == num2 or num2 == num3 or num3 == num1

#Imprime se algum número é igual.
print(f"Algum número digitado se repete? {verifica_num}")
