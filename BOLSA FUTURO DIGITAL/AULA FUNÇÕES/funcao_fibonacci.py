def fibonacci():
    valor_fibo = int(input("Informe um valor para ver a sequencia fibonacci: "))
    anterior = 0
    atual = 1
    for i in range(0, valor_fibo):
        fibonacci = anterior + atual
        anterior = atual
        atual = fibonacci
        print(fibonacci)
