#PEÇA 2 Nº AO USUARIO E MOSTRE QUAL É O MAIOR OU SE SÃO IGUAS.

num1 = float(input("Informe o 1º número: "))
num2 = float(input("Informe o 2º número: "))

num1_maior = num1 > num2
num2_maior = num2 > num1
num_igual = num1 == num2

print(f"O número {num1} é maior que o número {num2}? {num1_maior}")
print(f"O número {num2} é maior que o número {num1}? {num2_maior}")
print(f"O número {num1} é igual ao número {num2}? {num_igual}")
