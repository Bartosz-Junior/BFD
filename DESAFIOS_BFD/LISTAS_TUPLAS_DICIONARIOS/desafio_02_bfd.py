nomes_parentes = ['Bartosz', 'Arthur', 'Camila']
frutas = ['Maça', 'Cajá', 'Uva']
docinhos_festa = ['Brigadeiro', 'Beijinho', 'Surpresa de uva']
ingredientes_feijoada = ['Feijão', 'Calabresa', 'Bacon']

#Concatenando listas
lista_geral = [nomes_parentes,frutas,docinhos_festa,ingredientes_feijoada]

#ADICIONANDO BRIGADEIRO NA LISTA DOCINHOS_FESTA
docinhos_festa.append("brigadeiro")

#ADICIONANDO BEBIDAS NA LISTA GERAL
lista_geral.append("Bebidas")

#IMPRIMINDO A LISTA GERAL
print(lista_geral)

while len(lista_geral) != 0:
    del(lista_geral[-1])
    print(lista_geral)


