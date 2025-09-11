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

feira_mes = ["Feijão", "Arroz", "Carne", "Detegente", 
             "Água Sanitária", "Sabão liquido", "Sabão em pó", "Amaciante", "Sorvete"]

feira_mes.remove("Detegente")
feira_mes.remove("Água Sanitária")
feira_mes.remove("Sabão liquido")
feira_mes.remove("Sabão em pó")
feira_mes.remove("Amaciante")
feira_mes.remove("Sorvete")
print(feira_mes)

lista_num = [21 ,32, 13, 45, 65, 67, 57, 84, 29, 10]

lista_num.sort()
print(lista_num)
lista_num.reverse()
print(lista_num)