#Peça a idade de uma pessoa e verifique se ela tem entre 18 e 30 anos (inclusive).

#Entrada de dados do usuario com a idade
idade = int(input("Informe sua idade: "))

#Verifica se esta entre 18 e 30 anos
verificador_idade = idade >= 18 and idade <= 30

#Imprime na tela se a idade está entre 18 e 30 anos
print(f"A idade informada está entre 18 e 30 anos? {verificador_idade}")
