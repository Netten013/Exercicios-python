pares = 0
impares = 0

print("Digite 10 números inteiros:")

for i in range(1, 11):
    numero = int(input(f"Número {i}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
