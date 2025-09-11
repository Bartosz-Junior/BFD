#PEÇA 2 Nº AO USUARIO, CALCULE A SOMA E VERIFIQUE SE É MAIOR QUE 20.

#Entrada dos numeros pelo usuario
num1 = float(input("Informe o 1º número: "))
num2 = float(input("Informe o 2º número: "))

#Soma do numero 1 e numero 2
soma_num1_num2 = num1 + num2

#verifica se a soma de num1 e num2 é maior que 20 e retorna true ou false
maior_20 = soma_num1_num2 > 20

#imprime se o valor é ou não maior que 20
print(f"A soma dos números {num1} e {num2} é maior que 20? {maior_20}.")
