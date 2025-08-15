#CRIE UM PROGRAMA QUE RECEBA OS VALORES DE TRÊS NOTAS DE UM ALUNO E IMPRIMA A MÉDIA.

#ENTRADA DE DADOS(NOTAS)
nota1 = float(input("Informe a 1ª nota do aluno: "))
nota2 = float(input("Informe a 2ª nota do aluno: "))
nota3 =  float(input("Informe a 3ª nota do aluno: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média das notas do aluno informada é: {media:.2f}.")
