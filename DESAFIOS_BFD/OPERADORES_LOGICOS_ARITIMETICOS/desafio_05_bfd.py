#CALCULE A MEDIA DE 3 NOTAS E VERIFIQUE SE É IGUAL A 7.0

#Entrada das notas pelo usuario
nota1 = float(input("Informe a 1ª nota: "))
nota2 = float(input("Informe a 2ª nota: "))
nota3 = float(input("Informe a 3ª nota: "))

#Calculando a média
media_nota = (nota1 + nota2 + nota3) /3

#Verifica se média é igual a 7
verifica_media_7 = media_nota == 7

print(f"A média do aluno é maior que 7? {verifica_media_7}")
