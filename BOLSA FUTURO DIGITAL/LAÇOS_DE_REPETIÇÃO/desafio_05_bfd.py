tabuada = int(input("Informe um número para ver sua tabuada: "))
num = 0
print(f"###### TABUADA DO {tabuada} ######")
while num < 11:
    print(f"{num} x {tabuada} = {num*tabuada:^{5}}")
    num += 1
