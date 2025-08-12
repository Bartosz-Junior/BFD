#Solicite um valor e verifique se ele está fora da faixa entre 50 e 100.

#Entrada de dados o usuario com o numero que deseja verificar
num1 = float(input("Digite um número: "))

#Verificando se o numero esta entre 50 e 100
verifica_num = not(50 <= num1 <= 100)

#Imprimindo se o valor esta ou não intervalo desejado
print(f"O valor {num1} esta fora do range 50 a 100? {verifica_num}.")
