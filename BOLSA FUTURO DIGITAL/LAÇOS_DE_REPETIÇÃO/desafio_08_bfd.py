numeros_digitados = []
contador = 1
while True:
    num_entrada = float(input(f"Informe o {contador}º número: "))
    contador += 1
    if num_entrada > 0:
        numeros_digitados.append(num_entrada)
    elif num_entrada < 0:
        break
print(f"A soma dos números positivos digitados é: {sum(numeros_digitados):.2f}.")
print("************** NÚMEROS DIGITADOS **************")
print(numeros_digitados)
