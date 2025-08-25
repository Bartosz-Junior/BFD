#1. Crie uma função saudacao() que receba um nome como parâmetro e exiba "Olá, <nome>!".

def saudacao(nome):
    print(f"Olá, {nome}!")

#2. Escreva uma função soma(a, b) que retorne a soma de dois números.
def soma(a, b,):
    print(a + b)

#3. Faça uma função par_ou_impar(n) que retorne "Par" se o número for par e "Ímpar" caso contrário.

def par_impar(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

#4. Crie uma função dobro_lista(lista) que receba uma lista de números e retorne outra lista 
# com cada número dobrado.

def dobro_lista(lista):
    nova_lista = []
    for numero in lista:
        nova_lista.append(numero * 2)
    print(nova_lista)

#5. Explique, em código, a diferença entre uma 
# variável global e uma variável local.

variavel_global = "A variavel global é acessada em qualquer parte do código"

def teste_var():
    variavel_local = "Váriavel local só acesso dentro desta função, por exemplo."
    print(variavel_global)
    print(variavel_local)

def teste_var_local():
    print(variavel_global)
    print("Aqui não pega a varivel local da outra função ""teste_var_local""")

#6. Crie uma função media(*notas) que receba várias notas
#  (usando parâmetros variáveis) e retorne a média.

def media(*notas):
    media = sum(notas)/len(notas)
    print(media)

#7. Escreva uma função calculadora(a, b, operacao) que receba dois
#  números e uma operação ("+", "-", "*", "/") e retorne o resultado.

def calculadora(a, b, operacao):
    if (operacao == "+"):
        print(f"A soma é {a + b}.")
    elif (operacao == "-"):
        print(f"A subtração é {a - b}.")
    elif (operacao == "/"):
        print(f"A divisão é {a / b}.")
    elif (operacao == "*"):
        print(f"A multiplicação é {a * b}.")

#8. Faça uma função eh_primo(n) que retorne True se o número for primo e 
# False caso contrário

def eh_primo(n):
    pass