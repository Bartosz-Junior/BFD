#1. Calcule a tabuada do 13.
num_tabuada = int(input("Informe um número para ver sua tabuada:"))

#Loop for iterando num range de 0 a 10 onde multiplica pelo vlor informado pelo usuario
for multiplo in range(0, 11):
    print(f"{multiplo} x {num_tabuada} = {multiplo * num_tabuada}")


#2. Ler do teclado uma lista com 5 inteiros e imprimir o menor valor.
lista_01 = []

#Loop for iterando sobre o range de 0 a 4 onde cada iteração é uma
#  entrada de dados que é armazenado na lista 01.

for num in range(0 , 5):
    num_teclado = float(input("Informe um número qualquer: "))
    lista_01.append(num_teclado)

#Função MIN que retorna o menor valor em uma lista.
print(f"O menor número digitado foi {min(lista_01)}.")

#3. Ler do teclado uma lista com 5 inteiros e imprimir True se a lista estiver 
#ordenada de forma crescente ou False caso contrário.

lista_02 = []
contador = 0

#Loop for iterando sobre um range de 0 a 4 e armazenando o valor de entrada na lista 02.
for num01 in range(0,5):
    contador += 1
    num_teclado01 = int(input(f"Informe {contador}º número inteiro: "))
    lista_02.append(num_teclado01)

#Estrutura condicional verifica se a lista digitada na entrada esta em ordem
#crescente

if lista_02 == sorted(lista_02):
    print("True")
else:
    print("False")


#4. Exiba em ordem decrescente todos os números de 500 até 10.

#Range Reverso sendo impresso.
for i in range(500, 9, -1):
    print(i)



#5. Ler do teclado 10 números e imprima a quantidade de números entre 10 e 50.

lista_03 = []

#Loop for para iterar sobre a entrada de dados e adiciona na lista.
for num03 in range(0,10):
    entrada_teclado = float(input(f"Digite o {num03 + 1}º número: "))
    lista_03.append(entrada_teclado)

print("Os números digitados que estão entre 10 - 50 são: ")

#Loop for para iterar sobre a lista e retornar os valores que estão entre 10 e 50
#com um if onde verifica se o valor iterado da lista esta entre 10 e 50

for numlista in lista_03:
    if (numlista >= 10 and numlista <= 50):
        print(numlista)




#6. Ler do teclado a idade e o sexo de 10 pessoas, calcule e imprima:
#a) idade média das mulheres
#b) idade média dos homens
#c) idade média do grupo

#Listas dierentes para cada dado pedido na questão, armazenando o valor das idades de cada sexo
#conforme entrada de dados pelo usuario
mulheres = []
homens = []
media_geral = []

#Loop for para iterar na entrada de dados para não ter que repetir o input X vezes para cada entrada
for dados in range(1, 11):
    idade = int(input(f"Informe a idade da {dados}ª pessoa: "))
    sexo = str(input(f"Informe o sexo da {dados}ª pessoa: ")).lower()
    media_geral.append(idade)
    if (sexo == "f"):
        mulheres.append(idade)
    elif (sexo == "m"):
        homens.append(idade)

print(f"A idade média dos homens é: {sum(homens)/len(homens)}\nA idade média das mulheres é {sum(mulheres)/len(mulheres)}.")
print(f"A média geral é {sum(media_geral)/len(media_geral):.2f}")

#7. Calcule o somatório dos números de 1 a 100 e imprima o resultado.

#Variavel resultado declarada para armazenar o somatório dos valores entre 1 e 100

resultado = 0

for somatorio in range(1,101):
    resultado += somatorio

print(resultado)
