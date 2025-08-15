positivos = []
negativos = []
zeros = []
contador = 1

while contador < 7:
    numero = float(input(f"Informe o {contador}º número: "))
    contador += 1
    if numero > 0:
        positivos.append(numero)
    elif numero == 0:
        zeros.append(numero)
    elif numero < 0:
        negativos.append(numero)

print(f"Temos um total de {len(positivos)} número(s) positivo(s);\n{len(negativos)} número(s) negativo(s);\ne {len(zeros)} número(s) zero.")
