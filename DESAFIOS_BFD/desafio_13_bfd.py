#Solicite dois números e verifique se pelo menos um deles é múltiplo de 5.

#Entrada de dados pelo usuario com dois numeros quaisquer
num1 = float(input("Informe o 1º número: "))
num2 = float(input("Informe o 2º número: "))

#Verifica se pelo menos um dos números informados é multiplo de 5.
verifica_num = num1 % 5 == 0 or num2 % 5 == 0

#Imprime se pelo menos um dos números é multiplo de 5
print(f"Algum dos números informados é multiplo de 5? {verifica_num}")
