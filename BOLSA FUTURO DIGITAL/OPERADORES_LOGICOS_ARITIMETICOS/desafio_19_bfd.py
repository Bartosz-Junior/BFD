#Peça o salário e verifique se ele está entre 2000 e 5000 ou é exatamente 10000.

#Entrada de dados pelo usuario com o salario
salario = float(input("Informe o salário: "))

#Verifica se o salario obedece o enunciado
verifica_salario_2000_5000 = 2000 <= salario <= 5000
verifica_salario_10000 = salario == 10000

#Imprime se salario é igual a 10000 ou se esta entre 2000 e 5000
print(f"O salario está entre R$2000 e R$5000? {verifica_salario_2000_5000}")
print(f"O salario é igual a R$10000? {verifica_salario_10000}")
