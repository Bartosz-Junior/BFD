#Entrada de numero pelo usuario com o numero que ele quer saber o fatorial
num_fatorial = int(input("Informe um número inteiro para obter seu fatorial: "))
#variavel de controle para armazenar o resultado da multiplicação, recebe valor 1 para funcionar a multiplicação
resultado = 1

#Laço FOR "fatorial" que vai de 1 até o número informado
# pelo usário e multiplica a os valores até acaba a iteração
for fatorial in range(1 , (num_fatorial + 1)):
    resultado *= fatorial
    print(fatorial)

#Imprimi o resultado com o valor do fatorial do número informado na entrada
print(f"O fatorial de {num_fatorial} é {resultado}. ")
