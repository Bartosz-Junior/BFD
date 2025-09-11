numeros = []
contador = 1
while True:
    num = float(input(f"Informe o {contador}º número:"))
    numeros.append(num)
    contador += 1
    if contador == 5:
        break

print(f"A soma dos números informados é {sum(numeros)}.")
print(f"A mádia dos números informados é {sum(numeros)/4}.")
