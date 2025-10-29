num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

inicio = min(num1, num2) + 1
fim = max(num1, num2)

if inicio >= fim:
    print("Não há números inteiros entre os valores informados.")
else:
    print(f"Números inteiros entre {num1} e {num2}:")
    for i in range(inicio, fim):
        print(i)
