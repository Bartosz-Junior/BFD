#Atividades BFD Moodle - lista 01

#1 - Converta a string "123" para int e depois para float. Imprima os dois resultados

var_str = "123"
var_int = int(var_str)
var_float = float(var_str)
print(var_int)
print(var_float)

# 2 - Dada a string "Python é incrível!", faça o seguinte:
#Conte quantos caracteres ela possui (incluindo espa¸cos)
#Converta toda a string para mai´usculas
#Substitua a palavra ”incr´ıvel”por ”poderoso”

var_python = "Python é incrível!"
quant_caracter = len(var_python)
var_poderoso = var_python.replace("incrível" , "poderoso")
print(quant_caracter)
print(var_python.upper())
print(var_poderoso)

# 3 - Dada a lista numeros = [10, 20, 30, 40, 50], faça:
#Acesse e imprima o terceiro elemento
#Adicione o número 60 no final da lista
#Remova o número 20 da lista

numeros = [10, 20, 30, 40, 50]
print(numeros[2])
numeros.append(60)
numeros.remove(20)
print(numeros)

#4 - Crie um dicionário chamado aluno com:
# "nome": ”Maria”
# "idade": 22
# "curso": ”Engenharia”
#Depois:
# Adicione uma nova chave "notas" com a lista [8.5, 7.0, 9.2]
# Imprima apenas o valor da chave "curso"

aluno = {"Nome" : "Maria" , "Idade" : 22 , "Curso" : "Engenharia"}
aluno["Notas"] = [8.5 , 7.0 , 9.2]
print(aluno["Curso"])

# 5 - Dada a tupla cores = ("vermelho", "verde", "azul", "verde"):
#Converta-a em um conjunto para remover duplicatas
#Adicione a cor "amarelo" ao conjunto

cores = ("vermelho", "verde", "azul", "verde")
conjunto_cores = set(cores)
conjunto_cores.add("amarelo")


#6 - Declare duas variáveis:
# a = 15 (int)
# b = 4 (int)
#Calcule e imprima:
# A divisão inteira de a por b
# O resto da divisão de a por b

a = 15
b = 4
div_a_b_inteira = a // b
resto_div_ab = a % b
print(div_a_b_inteira)
print(resto_div_ab)

# 7 - Dada a lista dados = [42, 3.14, "Python", True, [1, 2]], percorra cada elemento
#e imprima seu tipo.

dados = [42, 3.14, "Python", True, [1, 2]]

for elemento in dados:
    print(type(elemento))

# 8 - Dada a string "programação":
#Inverta a string
#Verifique se a string original ´e igual `a string invertida

var_str_programacao = "programação"
verifica_str = var_str_programacao == var_str_programacao[::-1]
print(var_str_programacao[::-1])
print(verifica_str)

# 9 - Dada a lista matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
#Acesse e imprima o número 5
#Substitua o número 8 por 10

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[1][1])
matriz[2][1] = 10
print(matriz)

# 10 - Crie um dicionário estoque com:
#"macã": 10
#"banana": 5
#"laranja": 8
#Faça o seguinte:
#Adicione "pera" com quantidade 12
#Remova "banana"
#Imprima apenas os nomes dos itens (chaves)

estoque = {"Maça" : 10 , "Banana" : 5 , "Laranja" : 8}
estoque.update({"Pera" : 12})
estoque.pop("Banana")
print(estoque.keys())
