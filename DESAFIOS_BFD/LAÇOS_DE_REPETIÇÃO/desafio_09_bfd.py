import random

num_aleatorio = random.randint(1,20)

while True:
    sugestao = int(input("Tente advinhar o número que estou pensando entre 1-20: "))
    if sugestao == num_aleatorio:
        print("Parabéns, você acertou!!!")
        print(f"O número era o {num_aleatorio}...")
        break
    elif sugestao != num_aleatorio:
        print("Iiihhhhh, você errou. Tente novamente!")
        continue
    