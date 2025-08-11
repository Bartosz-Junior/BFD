#UM FUNCIONARIO FOI SORTEADO PARA RECEBER UM AUMENTO DE 15% EM SEU SALARIO. CALCULE O VALOR DO NOVO
#SALARIO DESTE FUNCIONARIO.

#entrada de dados informando o salario do funcionário antes do aumento
salario_antes_aumento = float(input("Informe o salário do funcionário: R$"))

#Calculando o aumento de 15%
salario_depois_aumento = (salario_antes_aumento * 0.15) + salario_antes_aumento

#imprimindo o valor do novo salario
print(f"O salário de R${salario_antes_aumento:.2f} após 15% de aumento é de R${salario_depois_aumento:.2f}. ")
