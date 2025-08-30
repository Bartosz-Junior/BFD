'''ALGORITMO PARA CONTAR A QUANTIDADE DE DIGITOS REPETIDOS NAS UNIDADES,
    DEZENAS, CENTENAS E MILHARES DOS ULTIMOS RESULTADOS DA FEDERAL.'''

#Lista com resultados da loteria federal.

resultados_federal_str = {"7133", "9368","4964" ,"2570", "0724" , "5122", "2399", "5262" ,"7544",
 "0111", "2244", "5475", "7766", "1186", "1708", "9532", "7130", "4864", "5282", "3475", "8460", 
 "8703", "1742", "7057", "7328", "3803", "7126", "4770", "3869", "9766", "5181", "3218", "9816", 
 "9331", "7180", "9755", "0847", "4085", "4192", "1606", "3309","6340", "1701", "7539", "5868",
 "3582", "6141", "7449", "7026", "7136", "4771", "4044", "3933", "6788", "3946", "5861", "1615",
 "6962", "0675", "4831", "2023", "5817", "1130", "4794", "8695", "9932", "1897", "7035", "0045",
 "6445"}

#Dicionário com as unidades de cada milhar e suas quantidades
quant_unidades = {}

#Dicionário com a quantidade e chave de cada dezena nas milhares de resultado
quant_dezenas = {}

#Dicionário com a quantidade e chave de cada centena nas milhares de resultado
quant_centenas = {}

#Dicionário com a quantidade e chave de cada centena nas milhares de resultado
quant_milhar = {}

#Lista com todos os digitos das unidades de cada milhar.
lista_unidade = []

#Lista de digitos das dezenas
lista_dezenas = []

#Lista de digitos das centenas
lista_centenas = []

#Lista de digitos das centenas
lista_milhar = []

#Loop for para iterar sobre cada milhar.
for milhar in resultados_federal_str:
    
    #Variável para extrair o ultimo digito da milhar(UNIDADE)
    ultimo_elemento = milhar[-1]

    #Lista com todos os digitos das unidades das milhares.
    lista_unidade.extend(ultimo_elemento)
    #Condicional para adicionar cada digito num dicionario e verficar a quantidade.

    #Conta quantas vezes cada digito repete na lista das unidades e armazena no dicionario.
    if ultimo_elemento in quant_unidades:
        quant_repetidas_elemento = lista_unidade.count(ultimo_elemento)
        quant_unidades.update({ultimo_elemento : quant_repetidas_elemento})
    #ELIF para criar no dicionario uma chave caso não exista aquele número.
    elif ultimo_elemento not in quant_unidades:
        quant_unidades.update({ultimo_elemento : 1})

#Ordenar o dicionário por chave em ordem crescente
dicionario_ordem = dict(sorted(quant_unidades.items()))
print("===== UNIDADES =====")
print(dicionario_ordem)

'''TRATAMENTO DAS DEZENAS DE ACORDO COM A LISTA DE RESULTADOS DA FEDERAL ACIMA'''

for milhar_dez in resultados_federal_str:

    digito_dezena = milhar_dez[2]

    #Lista com todos os digitos da casa das dezenas
    lista_dezenas.extend(digito_dezena)
    if digito_dezena in quant_dezenas:
        dezenas_repetidas = lista_dezenas.count(digito_dezena)
        quant_dezenas.update({digito_dezena : dezenas_repetidas})
    elif digito_dezena not in resultados_federal_str:
        quant_dezenas.update({digito_dezena : 1})

#Ordenar o dicionário por chave em ordem crescente
dicionario_ordem_dezenas = dict(sorted(quant_dezenas.items()))
print("===== DEZENAS =====")
print(dicionario_ordem_dezenas)

'''TRATAMENTO DAS CENTENAS'''

for milhar_centena in resultados_federal_str:

    digito_centena = milhar_centena[1]

    #Lista com todos os digitos da casa das centenas
    lista_centenas.extend(digito_centena)
    if digito_centena in quant_centenas:
        centena_repetida = lista_centenas.count(digito_centena)
        quant_centenas.update({digito_centena : centena_repetida})
    elif digito_centena not in resultados_federal_str:
        quant_centenas.update({digito_centena : 1})

dicionario_ordem_centenas = dict(sorted(quant_centenas.items()))
print("===== CENTENAS =====")
print(dicionario_ordem_centenas)


'''TRATAMENTO DAS MILHARES'''

for milhar_milhar in resultados_federal_str:

    digito_milhar = milhar_milhar[0]

    #Lista com todos os digitos da casa das milhares
    lista_milhar.extend(digito_milhar)
    if digito_milhar in quant_milhar:
        milhar_repetida = lista_milhar.count(digito_milhar)
        quant_milhar.update({digito_milhar : milhar_repetida})
    elif digito_milhar not in resultados_federal_str:
        quant_milhar.update({digito_milhar : 1})

dicionario_ordem_milhar = dict(sorted(quant_milhar.items()))
print("===== MILHAR =====")
print(dicionario_ordem_milhar)
